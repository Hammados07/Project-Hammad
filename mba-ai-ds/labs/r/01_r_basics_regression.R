# Lab R-01 · R basics, dplyr, ggplot2 and regression (Modules M14, M13)
# 🧒 R is Python's cousin raised by statisticians. Same questions, different words.
# Run line by line in RStudio (Ctrl+Enter) or Posit Cloud. Set the working directory to the `labs` folder:
#   Session → Set Working Directory → Choose Directory… → pick mba-ai-ds/labs
# First time only: install.packages(c("dplyr", "ggplot2"))

library(dplyr)
library(ggplot2)

# ---- 1. Basics: vectors and data frames -------------------------------------
calls_per_hour <- c(80, 120, 150, 110, 90)      # a vector (like a Python list)
mean(calls_per_hour); max(calls_per_hour); length(calls_per_hour)
calls_per_hour[1]                                # R counts from 1 (Python counts from 0!)

agent <- list(name = "Asha", team = "Billing", aht_sec = 298)   # like a Python dict
agent$name

sla_status <- function(sla, target = 80) {
  if (sla >= target) "Green" else if (sla >= target - 10) "Amber" else "Red"
}
sapply(c(91, 76, 65), sla_status)

# ---- 2. Load data -------------------------------------------------------------
calls <- read.csv("data/call_centre_intervals.csv")
cust  <- read.csv("data/customers.csv")
str(calls)          # structure: like df.info()
summary(calls$aht_sec)

# ---- 3. dplyr verbs = English ------------------------------------------------
by_day <- calls |>
  group_by(queue, day_of_week) |>
  summarise(calls = sum(calls_offered),
            sla_pct = round(100 * sum(answered_within_20s) / sum(calls_offered), 1),
            avg_aht = round(mean(aht_sec), 1),
            .groups = "drop") |>
  arrange(queue, sla_pct)
print(by_day)

calls <- calls |>
  mutate(hour = as.integer(substr(interval_start, 1, 2)),
         workload_per_agent = calls_offered * aht_sec / 1800 / agents_staffed)

# ---- 4. ggplot2: data + aesthetics + geometry ---------------------------------
p <- calls |>
  group_by(hour, queue) |>
  summarise(sla = mean(sla_pct, na.rm = TRUE), .groups = "drop") |>
  ggplot(aes(x = hour, y = sla, colour = queue)) +
  geom_line(linewidth = 1) +
  geom_hline(yintercept = 80, linetype = "dashed", colour = "red") +
  labs(title = "Average SLA % by hour", x = "Hour of day", y = "SLA %") +
  theme_minimal()
dir.create("output", showWarnings = FALSE)
ggsave("output/lab_r01_sla_by_hour.png", p, width = 8, height = 4)

# ---- 5. Hypothesis test (M12): is Billing AHT different from Tech Support? ----
t.test(aht_sec ~ queue, data = calls)

# ---- 6. Linear regression (M13) -----------------------------------------------
lin <- lm(sla_pct ~ workload_per_agent + queue + day_of_week, data = calls)
summary(lin)        # same numbers as Python's statsmodels summary()

# ---- 7. Logistic regression (M13) ---------------------------------------------
set.seed(42)
train_rows <- sample(nrow(cust), 0.75 * nrow(cust))
train <- cust[train_rows, ]; test <- cust[-train_rows, ]
logit <- glm(churned ~ tenure_months + complaints_6m + monthly_charges + contract_type,
             data = train, family = binomial)
summary(logit)
round(exp(coef(logit)), 3)                       # odds ratios

prob <- predict(logit, newdata = test, type = "response")
pred <- ifelse(prob >= 0.5, 1, 0)
table(actual = test$churned, predicted = pred)   # confusion matrix
cat("Accuracy:", round(mean(pred == test$churned), 3), "\n")

# ---- Your turn -------------------------------------------------------------
# a) Which day has the lowest SLA for Tech Support? (filter + arrange)
# b) Make a histogram of aht_sec coloured by queue: ggplot(calls, aes(aht_sec, fill = queue)) + geom_histogram()
# c) Compare with Python Lab 04. Coefficients are close but not identical: the random train/test split differs.
