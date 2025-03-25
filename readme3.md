## 📌 Level 2 - Task 3: Feature Engineering

### 📝 Objective

This task focuses on performing feature engineering to enhance the dataset by extracting and encoding additional features. The goals are:

- Extract new features such as the length of restaurant names and addresses.
- Create new categorical features like "Has Table Booking" and "Has Online Delivery" by encoding existing data.

### 📂 Files

- **task3.py** → Python script performing feature engineering.
- **Cleaned_Dataset_Task1.csv** → Input dataset used for analysis.
- **Enhanced_Dataset_Task3.csv** → Output dataset with additional features.

### 📊 Analysis Performed

#### 1️⃣ Extracting Additional Features

- Calculated the length of restaurant names (**Restaurant_Name_Length**).
- Calculated the length of restaurant addresses (**Address_Length**).

#### 2️⃣ Creating New Categorical Features

- Encoded **"Has Table Booking"** as **1 (Yes)** or **0 (No)**.
- Encoded **"Has Online Delivery"** as **1 (Yes)** or **0 (No)**.

#### 3️⃣ Saving the Enhanced Dataset

- The modified dataset with new features is saved as **Enhanced_Dataset_Task3.csv**.

### 🔍 Key Findings

- The dataset now includes additional insights based on feature extraction.
- New categorical features allow for better analysis and model training.

### 🚀 How to Run

Ensure you have the necessary libraries installed:

```bash
pip install pandas numpy
```

Run the script using:

```bash
python task3.py
```

The enhanced dataset will be generated and saved as **Enhanced_Dataset_Task3.csv**.