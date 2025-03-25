#  Task 2: Price Range Analysis

## 📝 Objective  
This task focuses on analyzing restaurant price ranges and their impact on ratings. The objectives include:  
- Identifying the most common price range among restaurants.  
- Calculating the average rating for each price range.  
- Determining the color associated with the highest-rated price range.  

## 📂 Files  
- `task2.py` → Python script for price range analysis.  
- `Cleaned_Dataset_Task1.csv` → Preprocessed dataset used for analysis.  

## 📊 Analysis Performed  
### 1️⃣ **Most Common Price Range**  
- Used the **mode()** function to identify the most frequently occurring price range.  
- Printed the most common price range.  

### 2️⃣ **Average Rating for Each Price Range**  
- Grouped data by **Price Range** and calculated the **mean rating** for each category.  
- Displayed the average ratings per price range.  

### 3️⃣ **Highest Rated Price Range & Associated Color**  
- Identified the **price range with the highest average rating**.  
- Assigned colors to each price range:  
  - **1 → Red**  
  - **2 → Orange**  
  - **3 → Green**  
  - **4 → Blue**  
- Displayed the **color representing the highest-rated price range**.  

### 4️⃣ **Data Visualization**  
- Used **Seaborn** to create a **bar plot** showing the average rating for each price range.  
- Applied a color palette to differentiate price ranges.  
- Set appropriate **labels and titles** for clarity.  

## 🔍 Key Findings  
- The **most common price range** was **1 (Lowest Price Range)**.  
- Higher price ranges generally had **higher average ratings**.  
- The **highest-rated price range** was **4 (Highest Price Range)**, represented by the color **blue**.  

## 🚀 How to Run  
1. Ensure you have the necessary libraries installed:  
   ```bash  
   pip install pandas matplotlib seaborn  
