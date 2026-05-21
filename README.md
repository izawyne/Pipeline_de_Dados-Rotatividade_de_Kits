# End-to-End Data Pipeline with Medallion Architecture and Automated Data Delivery

## 📌 Overview

This project was designed to automate and structure a complete reporting workflow using an end-to-end ETL pipeline with a Medallion Architecture approach (Bronze, Silver, Gold).

The pipeline extracts data from an Oracle ERP system, performs automated transformations and validations using Python, organizes the data into layered processing stages, and automatically delivers updated Power BI dashboards.

---

## 🚀 Main Features

- Automated Oracle ERP data extraction
- End-to-end ETL pipeline using Python
- Medallion Architecture implementation (Bronze, Silver, Gold)
- parquet-based layered data storage
- Automated data validation workflows
- Pipeline orchestration and workflow automation
- Automated Power BI refresh and dashboard delivery
- Reduction of manual reporting workflow from nearly one full workday to less than 6 minutes

---

## 🏗️ Architecture

```text
Oracle ERP
   ↓
Python Extraction
   ↓
Bronze Layer (Raw parquet Data)
   ↓
Silver Layer (Validated & Cleaned Data)
   ↓
Gold Layer (Business-Level Data)
   ↓
Power BI Dashboards
```
---
 
## 📂 Project Structure
```
rotatividade_kits/
│
├── scripts/
│   ├── extract_kits.py
│   ├── transform_kits.py
│   ├── load_kits.py
│   └── main.py
│
├── sql/
│   └── example_query.sql
│
├── bronze/
├── silver/
├── gold/
│
├── data_sample/
│   └── sample_data.csv
│
├── logs/
│
└── dashboard/
```
---

## ⚙️ Tech Stack

- Python (pandas)
- SQL
- Oracle SQL
- parquet
- Power BI
- Pipeline Orchestration
- Workflow Automation
- Windows Task Scheduler
- Power BI Gateway

---

## 🔄 Pipeline Stages
1. Extract

Responsible for:

SQL-based extraction from Oracle ERP sources
Query execution and data ingestion
Initial raw data collection for processing

Script: extract_kits.py

2. Transform

Responsible for:

Column standardization
Date normalization
Data type conversion
Text standardization
Data validation and cleaning

Script: transform_kits.py

3. Load

Responsible for:

Business rule application
GOLD layer generation
Analytical data delivery for Power BI consumption

Script: load_kits.py

---

## 📊 Business Logic
- Applied filtering and validation rules based on operational business requirements
- Standardized and consolidated data from multiple ERP sources
- Implemented layered processing for analytical consumption
- Structured business-ready datasets for dashboard delivery

---

## ⚠️ Technical Challenges
- Handling inconsistent date formats across multiple data sources
- Resolving duplicate records caused by relational joins
- Standardizing inconsistent source data for reliable analytical processing

---

## 🤖 Automation

The pipeline was automated using:

- Python executable (.exe)
- Windows Task Scheduler
- Power BI Gateway integration for automated dashboard refresh

Automated Workflow
```
Windows Task Scheduler
   ↓
Pipeline Execution
   ↓
Data Processing & Layer Updates
   ↓
Power BI Gateway
   ↓
Automated Dashboard Refresh
```
---

## 📈 Results
- Reduced a fully manual reporting workflow from nearly one full workday to less than 6 minutes
- Automated repetitive operational and reporting processes
- Improved reporting reliability and data standardization
- Implemented scalable layered data processing using Medallion Architecture
- Enabled automated Power BI dashboard delivery and refresh

---

## 🔮 Future Improvements
- Airflow orchestration
- Docker containerization
- PostgreSQL integration
- Cloud-based storage and processing

---

## ⚠️ Note

This repository contains an adapted portfolio version of the original project and does not include real business data or sensitive information.
