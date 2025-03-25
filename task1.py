#  Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#  Load the cleaned dataset
df = pd.read_csv("Cleaned_Dataset_Task1.csv")  

# 1️⃣  Determine the percentage of restaurants offering table booking & online delivery
table_booking_percentage = df["Has Table booking"].mean() * 100
online_delivery_percentage = df["Has Online delivery"].mean() * 100

print(f" Percentage of restaurants with table booking: {table_booking_percentage:.2f}%")
print(f" Percentage of restaurants with online delivery: {online_delivery_percentage:.2f}%")

# 2️⃣  Compare average ratings of restaurants with and without table booking
avg_rating_with_booking = df[df["Has Table booking"] == True]["Aggregate rating"].mean()
avg_rating_without_booking = df[df["Has Table booking"] == False]["Aggregate rating"].mean()

print(f"\n Average rating of restaurants with table booking: {avg_rating_with_booking:.2f}")
print(f" Average rating of restaurants without table booking: {avg_rating_without_booking:.2f}")

# Visualizing the comparison
plt.figure(figsize=(6, 4))
sns.barplot(x=["With Table Booking", "Without Table Booking"], 
            y=[avg_rating_with_booking, avg_rating_without_booking], 
            hue=["With Table Booking", "Without Table Booking"],  
            palette=["blue", "red"], legend=False)

plt.title("Average Ratings: Table Booking vs. No Table Booking")
plt.ylabel("Average Rating")
plt.show()

# 3️⃣  Analyze online delivery availability among different price ranges
plt.figure(figsize=(8, 5))
sns.countplot(x="Price range", hue="Has Online delivery", data=df, palette="coolwarm")
plt.title("Online Delivery Availability Across Price Ranges")
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.legend(["No Online Delivery", "Has Online Delivery"])
plt.show()

print("\n Table Booking & Online Delivery Analysis Completed!")
