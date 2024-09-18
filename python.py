# -*- coding: utf-8 -*-
"""Untitled12.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HNySJ54xb9N2lTB-HVOXR4KZv8QIhoVY
"""

# Install the corrplot package
install.packages("corrplot")

# Load necessary libraries
library(ggplot2)
library(dplyr)
library(corrplot)

# Load dataset
ted_talks <- read.csv("ted_talks.csv")

# 1. Summary Statistics
summary(ted_talks[c("views", "comments", "duration")])

# 2. Distribution of Views
ggplot(ted_talks, aes(x = views)) +
  geom_histogram(binwidth = 1000000, fill = "blue", color = "black") +
  labs(title = "Distribution of Views", x = "Views", y = "Frequency")

# 3. Top 10 Most Viewed Talks
top_10_talks <- ted_talks %>%
  arrange(desc(views)) %>%
  head(10)

ggplot(top_10_talks, aes(x = reorder(title, views), y = views)) +
  geom_bar(stat = "identity", fill = "darkgreen") +
  coord_flip() +
  labs(title = "Top 10 Most Viewed TED Talks", x = "Talk Title", y = "Views")

# 4. Correlation Matrix of Numerical Variables
cor_matrix <- cor(ted_talks[c("views", "comments", "duration")], use = "complete.obs")
corrplot(cor_matrix, method = "color", addCoef.col = "black", tl.cex = 0.8)

# 5. Distribution of Topics
ted_talks$topic_list <- gsub("[\\[\\]' ]", "", ted_talks$topics)  # Clean the 'topics' column
topic_freq <- table(unlist(strsplit(ted_talks$topic_list, ",")))

topic_df <- as.data.frame(topic_freq)
colnames(topic_df) <- c("Topic", "Frequency")
topic_df <- topic_df %>% arrange(desc(Frequency)) %>% head(10)

ggplot(topic_df, aes(x = reorder(Topic, Frequency), y = Frequency)) +
  geom_bar(stat = "identity", fill = "purple") +
  coord_flip() +
  labs(title = "Top 10 Most Frequent Topics", x = "Topics", y = "Frequency")

# Linear Regression: Views vs Duration and Comments
# Simple Linear Regression: Views ~ Duration
lm_duration <- lm(views ~ duration, data = ted_talks)
summary(lm_duration)

# Scatter plot with regression line for Views vs Duration
ggplot(ted_talks, aes(x = duration, y = views)) +
  geom_point(alpha = 0.5) +
  geom_smooth(method = "lm", se = FALSE, color = "red") +
  labs(title = "Views vs Duration", x = "Duration (seconds)", y = "Views")

# Simple Linear Regression: Views ~ Comments
lm_comments <- lm(views ~ comments, data = ted_talks)
summary(lm_comments)

# Scatter plot with regression line for Views vs Comments
ggplot(ted_talks, aes(x = comments, y = views)) +
  geom_point(alpha = 0.5) +
  geom_smooth(method = "lm", se = FALSE, color = "blue") +
  labs(title = "Views vs Comments", x = "Comments", y = "Views")

# Load necessary libraries
library(ggplot2)

# Load dataset
ted_talks <- read.csv("ted_talks.csv")

# Check structure of the dataset
str(ted_talks)

# Remove rows with missing values in comments
ted_talks_clean <- na.omit(ted_talks[, c("views", "comments", "duration")])

# Linear Regression: Predicting Views based on Duration and Comments
# Multiple Linear Regression: Views ~ Duration + Comments
lm_model <- lm(views ~ duration + comments, data = ted_talks_clean)

# Summary of the model
summary(lm_model)

# Scatter plot with regression line for Views vs Duration
ggplot(ted_talks_clean, aes(x = duration, y = views)) +
  geom_point(alpha = 0.5) +
  geom_smooth(method = "lm", se = FALSE, color = "red") +
  labs(title = "Views vs Duration", x = "Duration (seconds)", y = "Views")

# Scatter plot with regression line for Views vs Comments
ggplot(ted_talks_clean, aes(x = comments, y = views)) +
  geom_point(alpha = 0.5) +
  geom_smooth(method = "lm", se = FALSE, color = "blue") +
  labs(title = "Views vs Comments", x = "Comments", y = "Views")

# Load necessary libraries
install.packages("Metrics")
library(Metrics)

# Load dataset
ted_talks <- read.csv("ted_talks.csv")

# Remove rows with missing values in comments and filter necessary columns
ted_talks_clean <- na.omit(ted_talks[, c("views", "comments", "duration")])

# Fit a multiple linear regression model: Views ~ Duration + Comments
lm_model <- lm(views ~ duration + comments, data = ted_talks_clean)

# Summary of the model (this includes R-squared value)
summary(lm_model)

# Calculate predictions
predicted_values <- predict(lm_model, ted_talks_clean)

# Calculate RMSE
rmse_value <- rmse(ted_talks_clean$views, predicted_values)
cat("RMSE: ", rmse_value, "\n")

# Calculate R-squared manually (though summary(lm_model) already gives R²)
ss_total <- sum((ted_talks_clean$views - mean(ted_talks_clean$views))^2)
ss_residual <- sum((ted_talks_clean$views - predicted_values)^2)
r_squared <- 1 - (ss_residual / ss_total)
cat("R-squared: ", r_squared, "\n")