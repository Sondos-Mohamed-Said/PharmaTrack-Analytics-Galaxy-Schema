# 💊 PharmaTrack: Pharmacy Analytics (Galaxy Schema & Synthetic Data)

  

## 📊 Project Overview

**PharmaTrack** is a business intelligence solution designed to simulate and analyze the operations of a pharmacy chain in **Egypt**. It covers three core areas: **Financial Performance**, **Staff Productivity**, and **Inventory Health**.

### Key Technical Highlights:

1.  **Synthetic Data Engineering:** The entire dataset was generated programmatically using a custom **Python script** (`Pharmacy data generator.py`). This script uses the **Faker** library to create realistic scenarios tailored to the Egyptian market.
2.  **Galaxy Schema Modeling:** The data is architected using a **Galaxy Schema (Fact Constellation)**, allowing two distinct Fact tables (`Sales` and `Inventory`) to interact seamlessly through shared Conformed Dimensions.

-----

## 🇪🇬 Egyptian Market Context

The data generation logic was specifically tuned to reflect the unique characteristics of the pharmacy sector in Egypt:

  * **Top Selling Medications:** The product list includes medications heavily used in Egypt for chronic conditions (e.g., *Concor* for hypertension, *Lantus* for diabetes, *Plavix*, *Crestor*).
  * **Payment Behavior:** The data reflects a **cash-dominant economy**, with "Cash" accounting for \~67% of transactions, while "Visa" and "App" payments represent the growing but smaller segment of digital adoption.
  * **Delivery Culture:** The "Home Delivery" and "App" order channels are included to simulate the high demand for pharmacy delivery services in Egyptian urban centers like Maadi and Giza.

-----

## 🐍 Data Generation Logic

Since real-world sensitive data was not used, a Python script was developed to generate realistic retail patterns and export them directly to **Excel**.

### How to Run the Script

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/PharmaTrack.git
    ```
2.  **Install dependencies:**
    ```bash
    pip install pandas faker openpyxl
    ```
3.  **Run the generator:**
    ```bash
    python "Pharmacy data generator.py"
    ```
4.  **Output:**
    The script will generate the following Excel files in the root directory:
      * `Fact_Sales.xlsx` (Transactional data)
      * `Fact_Inventory.xlsx` (Stock levels & Expiry)
      * `Dim_Products.xlsx`, `Dim_Customers.xlsx`, `Dim_Staff.xlsx`, etc.

-----

## 🗂️ Data Architecture: Galaxy Schema

The model connects two different business processes—**Sales Transactions** and **Inventory Snapshots**—using shared dimensions.

  * **Fact Tables:**
      * `Fact_Sales`: Transactional level data (Time, Customer, Amount, Payment Method).
      * `Fact_Inventory`: Batch level data (Expiry Date, Quantity on Hand, Storage Location).
  * **Conformed Dimensions:**
      * `Dim_Products`: The central dimension linking Sales (what sold) to Inventory (what is stored).
      * `Dim_Time` / `Dim_Date`: Standardizes temporal analysis across both facts.

-----

## 📈 Dashboard Features

### 1\. Overview & Financials

**Goal:** High-level executive view of P\&L.

  * **KPIs:** Total Revenue ($411.3K), Profit, Cost, and Transactions.
  * **Time Analysis:** Hourly revenue trends to identify the "Evening Rush" (6 PM - 9 PM), a common pattern in Egyptian retail.
  * **Payment Methods:** Analysis of Cash vs. Digital payments.

### 2\. Products & Staff Performance

**Goal:** Optimize operations and workforce planning.

  * **Pareto Analysis:** A dynamic chart identifying the "Vital Few" products driving 80% of revenue.
  * **Staff Rankings:** Performance evaluation based on revenue generation.
  * **Heatmap:** Visualizing transaction density to assist with shift scheduling.

### 3\. Inventory Management (Expiry Tracking)

**Goal:** Reduce shrinkage and waste.

  * **Expiry Alerts:** Tracks specific `Batch_ID`s with conditional formatting to flag items approaching expiration.
  * **Financial Impact:** Calculates the exact monetary value of "Expired" vs. "Near Expiry" stock.
  * **Storage Analysis:** Inventory levels split by storage condition (Fridge vs. Shelf).

-----

## 🛠️ Tools Used

  * **Python:** Data generation logic (`Faker`, `Pandas`).
  * **Excel:** Source data storage.
  * **Power BI:** Dashboarding, DAX Measures, and UI/UX design.
  * **Power Query:** ETL processes to load and transform Excel outputs.

-----

## 📧 Contact

Feel free to explore the Python scripts to see how the data was created, or check the PBIX file for the DAX measures\!

**[Sondos Mohamed]**
[[Link to your LinkedIn](https://www.linkedin.com/in/sondos-mohamed-said/)]
