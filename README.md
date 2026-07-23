# 👨‍💼 Employee JSON ETL Pipeline

A modular ETL (Extract, Transform, Load) pipeline built using **pure Python** for processing employee data stored in JSON format.

This project demonstrates how JSON data can be extracted, cleaned, transformed, analyzed, and exported while generating business insights. The project is designed following clean code principles and modular programming practices commonly used in Data Engineering.

---

# Project Overview

Many modern applications expose their data through REST APIs, and the responses are typically in JSON format. Before this data can be loaded into databases or data warehouses, it must be cleaned and validated.

This project simulates that workflow by processing employee records from a JSON file.

```text
employees.json
      │
      ▼
 Read JSON Data
      │
      ▼
 Clean Employee Data
      │
      ▼
 Generate Business Metrics
      │
      ▼
Write Clean JSON
      │
      ▼
clean_employees.json
```

---

# Features

* Reads employee records from a JSON file
* Cleans employee names
* Cleans city names
* Calculates total employees
* Calculates total salary
* Calculates average salary
* Identifies the highest-paid employee
* Counts employees by city
* Exports cleaned employee records to a new JSON file
* Uses modular helper functions for maintainability

---

# Project Structure

```text
employee-json-etl-pipeline/
│
├── data/
│   ├── employees.json
│   └── clean_employees.json
│
├── screenshots/
│   └── output.png
│
├── employee_json_etl.py
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

# Technologies Used

* Python 3
* JSON Module
* File Handling
* Dictionaries
* Functions
* Modular Programming
* ETL Concepts

No external libraries are required.

---

# Input Dataset

The input JSON file contains employee records with the following fields:

| Field      | Description     |
| ---------- | --------------- |
| id         | Employee ID     |
| name       | Employee Name   |
| department | Department      |
| salary     | Employee Salary |
| city       | Employee City   |

---

# Data Cleaning

The pipeline standardizes employee information by:

* Removing leading and trailing spaces
* Converting employee names to Title Case
* Converting city names to Title Case

Example:

```text
"  pavan "
```

↓

```text
"Pavan"
```

---

# ETL Workflow

## Extract

* Read employee records using `json.load()`

## Transform

* Clean employee names
* Clean city names

## Analyze

Generate business metrics including:

* Total Employees
* Total Salary
* Average Salary
* Highest Paid Employee
* Employee Count by City

## Load

Write the cleaned employee records to:

```text
clean_employees.json
```

using `json.dump()` with formatted indentation.

---

# Code Architecture

The project follows a modular structure.

```text
Helper Functions
│
├── cleaned_name()
└── cleaned_city()

        │
        ▼

Read JSON
        │
        ▼

Process Employee Records
        │
        ▼

Generate Summary
        │
        ▼

Write Clean JSON
        │
        ▼

Display Results
```

---

# Sample Console Output

```text
Total Employees: 4

Total Salary: 224000

Average Salary: 56000

Highest-paid Employee: Pavan

Employee Count by City

{
    'Hyderabad': 1,
    'Delhi': 1,
    'Chennai': 1,
    'Bangalore': 1
}
```

---

# Learning Outcomes

This project demonstrates practical understanding of:

* JSON Processing
* File Handling
* Data Cleaning
* Dictionary Aggregation
* Business Metric Generation
* Modular Python Programming
* ETL Workflow Design

---

# Future Improvements

Planned enhancements include:

* JSON Schema Validation
* Exception Handling
* Logging
* Configuration Files
* PostgreSQL Integration
* REST API Data Extraction
* Unit Testing
* Apache Airflow Integration

---

# Author

**Pavan Sai Merugumala**

Aspiring Data Engineer

Building end-to-end Data Engineering projects using Python, SQL, PostgreSQL, ETL pipelines, and cloud technologies.
