#  Import necessary libraries
import pandas as pd

#  Load the cleaned dataset
df = pd.read_csv("Cleaned_Dataset_Task1.csv")  

# 1️⃣  Extracting Additional Features
# Extract the length of the restaurant name
df["Restaurant_Name_Length"] = df["Restaurant Name"].astype(str).apply(len)

# Extract the length of the address
df["Address_Length"] = df["Address"].astype(str).apply(len)

# 2️⃣  Creating New Features
# Function to safely convert categorical values to binary encoding
def encode_binary(value):
    return 1 if str(value).strip().lower() == "yes" else 0

# Apply encoding to Table Booking and Online Delivery
df["Has_Table_Booking"] = df["Has Table booking"].apply(encode_binary)
df["Has_Online_Delivery"] = df["Has Online delivery"].apply(encode_binary)

# 3️⃣  Save the modified dataset
df.to_csv("Enhanced_Dataset_Task3.csv", index=False)

# ✅ Feature Engineering Completed!
print("\n Feature Engineering Completed! The updated dataset is saved as 'Enhanced_Dataset_Task3.csv'.")
