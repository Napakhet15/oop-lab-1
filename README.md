# OOP Lab 1
# Lab Overview
This lab demonstrates the use of Object-Oriented Programming (OOP) in Python by implementing two classes: DataLoader and Table.
The project focuses on reading, filtering, and aggregating data from a CSV file (Cities.csv).


# Project Structure
oop_lab_1/
│
├── README.md               # This file.
├── Cities.csv              # The data set
└── data_processing.py      # the analysis code

# Design Overview

1. DataLoader Class
Handles loading CSV data files and converting them into a list of dictionaries.


2. Table Class
Represents tabular data and provides methods for filtering and aggregating records.

- filter:
  Returns a new Table object containing only rows that match a given condition (lambda function).

- aggregate():
  Applies an aggregation function (e.g., sum, max, average, or count) to the specified key and returns the result.


# Features
- Load CSV Files: Load structured data using DataLoader.
- Filter Data: Select data based on conditions (e.g., cities from Germany).
- Aggregate Data: Calculate averages, maximums, or count unique items.


# How to Test and Run the Code
1. Ensure you have Python 3.x installed.
2. Place the Cities.csv file in the same directory as data_processing.py.
3. Open the terminal in that directory and run:

```bash
python data_processing.py



