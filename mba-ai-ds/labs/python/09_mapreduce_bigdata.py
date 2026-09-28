# %% [markdown]
# # Lab 09 · Big Data thinking: MapReduce & Spark (Module M21)
# 🧒 10,000 kids each count words in one book (MAP), then we add all their counts together (REDUCE).

# %% Setup
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

import pandas as pd

from _paths import DATA

reviews = pd.read_csv(DATA / "reviews.csv").text.tolist()
# Pretend each chunk lives on a different computer
chunks = [reviews[i:i + 100] for i in range(0, len(reviews), 100)]
print(f"{len(reviews)} reviews split into {len(chunks)} chunks ('machines')")

# %% 1. MAP: each machine turns its reviews into (word, 1) pairs
def map_chunk(chunk):
    pairs = []
    for text in chunk:
        for word in text.lower().replace(",", " ").replace(".", " ").split():
            pairs.append((word, 1))
    return pairs


with ThreadPoolExecutor() as pool:                   # run the machines in parallel
    mapped = list(pool.map(map_chunk, chunks))
print("Machine 1's first pairs:", mapped[0][:5])

# %% 2. SHUFFLE: send every pair for the same word to the same place
shuffled = defaultdict(list)
for machine_output in mapped:
    for word, one in machine_output:
        shuffled[word].append(one)

# %% 3. REDUCE: add up each word's list
counts = {word: sum(ones) for word, ones in shuffled.items()}
top = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:10]
print("Top 10 words:", top)

# %% 4. The same thing in Spark (run in Google Colab after `!pip install pyspark`, or in Databricks Free Edition)
try:
    from pyspark.sql import SparkSession, functions as F

    spark = SparkSession.builder.appName("lab09").getOrCreate()
    sdf = spark.read.csv(str(DATA / "reviews.csv"), header=True)
    words = sdf.select(F.explode(F.split(F.lower(F.regexp_replace("text", "[,.]", "")), " ")).alias("word"))
    words.filter(F.col("word") != "").groupBy("word").count().orderBy(F.desc("count")).show(10)

    # Spark SQL feels just like PostgreSQL:
    sdf.createOrReplaceTempView("reviews")
    spark.sql("SELECT topic, sentiment, COUNT(*) AS n FROM reviews GROUP BY topic, sentiment ORDER BY n DESC").show()
    spark.stop()
except ImportError:
    print("PySpark not installed. That's fine. Run this part in Colab (`!pip install pyspark`) or Databricks.")

# %% 5. File formats: why Parquet beats CSV for analytics
# df.to_parquet("reviews.parquet")   (needs `pip install pyarrow`) stores data by COLUMN, compressed:
# reading one column no longer means reading the whole file.

# %% Your turn
# a) Change map_chunk to ignore short words (len < 4). How does the top-10 change?
# b) Explain in 2 lines why MAP can run on 1,000 machines at once but SHUFFLE needs the network.
