# OOP Lab 1

## Lab Overview
This lab demonstrates the use of Object-Oriented Programming (OOP) in Python by implementing two classes: DataLoader and Table.
The project focuses on reading, filtering, and aggregating data from a CSV file **Cities.csv** and **Countries.csv**.

---

## Project Structure

oop_lab_1/
│
├── README.md # Project documentation
├── Cities.csv # The data set
├── Countries.csv # Additional dataset
└── data_processing.py # the analysis code

---

## Design Overview

### 1. DataLoader Class
Responsible for:
- Loading CSV files
- Converting rows into a list of dictionaries  
This makes the datasets easy to process using Python.

---

### 2. Table Class
Represents tabular data and provides methods to transform and analyze it.

#### Methods:
- **filter(condition_function)**  
  Returns a new `Table` containing only rows that satisfy the given condition (usually a lambda expression).

- **aggregate(aggregation_function, key)**  
  Extracts values from the specified key and applies an aggregation function (e.g., `sum`, `max`, `min`, `average`, `len`).

- **join(other_table, key)**  
  Combines two tables based on a matching column.

---

## Features
- **Load CSV Files** using `DataLoader`
- **Filter Data** based on conditions (e.g., cities in Italy)
- **Aggregate Data** such as:
  - Average temperature  
  - Maximum or minimum value  
  - Counting records
- **Join Tables** to combine city + country data

---

## How to Run the Code

1. Make sure Python 3.x is installed.
2. Place `Cities.csv`, `Countries.csv`, and `data_processing.py` in the same directory.
3. Open a terminal in that directory.
4. Run:

```bash
python data_processing.py