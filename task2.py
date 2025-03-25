#  Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#  Load the cleaned dataset
df = pd.read_csv("Cleaned_Dataset_Task1.csv") 

# 1️⃣ 🔢 Determine the Most Common Price Range
most_common_price_range = df["Price range"].mode()[0]
print(f" Most Common Price Range: {most_common_price_range}")

# 2️⃣  Calculate the Average Rating for Each Price Range
avg_rating_per_price_range = df.groupby("Price range")["Aggregate rating"].mean()
print("\n Average Rating for Each Price Range:\n", avg_rating_per_price_range)

# 3️⃣  Identify the Color Representing the Highest Average Rating
highest_avg_rating_price_range = avg_rating_per_price_range.idxmax()
highest_avg_rating = avg_rating_per_price_range.max()

# Define colors for price ranges
price_colors = {1: "red", 2: "orange", 3: "green", 4: "blue"}
highest_avg_color = price_colors.get(highest_avg_rating_price_range, "gray")

print(f"\n Price Range with the Highest Average Rating: {highest_avg_rating_price_range}")
print(f" Color Representing Highest Average Rating: {highest_avg_color}")

# 4️⃣  Visualizing Price Range vs. Average Rating
plt.figure(figsize=(8, 5))
sns.barplot(
    x=avg_rating_per_price_range.index,
    y=avg_rating_per_price_range.values,
    hue=avg_rating_per_price_range.index,  
    palette="coolwarm",
    legend=False
)

plt.xlabel("Price Range")
plt.ylabel("Average Rating")
plt.title("Average Rating by Price Range")
plt.xticks(ticks=avg_rating_per_price_range.index, labels=["1 (Low)", "2", "3", "4 (High)"])
plt.show()

print("\n✅ Price Range Analysis Completed!")
