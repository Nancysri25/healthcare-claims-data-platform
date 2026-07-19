
# 🏥 Healthcare Claims Data Platform

An end-to-end Data Engineering project that simulates a production-grade US Healthcare Claims Processing Platform. The project demonstrates how healthcare insurance claim files are ingested, validated, transformed, and loaded into a dimensional data warehouse for business reporting and analytics.

---

# 📌 Project Objective

Healthcare insurance companies receive millions of claim records every day from hospitals, clinics, pharmacies, and healthcare providers. This project automates the complete lifecycle of healthcare claims processing using modern Data Engineering tools and best practices.

The platform performs:

- Automated ingestion of healthcare claim files
- Data quality validation
- Data transformation and cleansing
- Incremental ETL processing
- Dimensional Data Warehouse loading
- Business KPI generation
- Interactive analytics dashboards

---

# 🏗️ Architecture

```
                    Healthcare Claims Files
                               │
                               ▼
                     Raw Data Landing Zone
                               │
                               ▼
                      Data Validation Layer
                               │
                               ▼
                  Data Transformation Layer
                               │
                               ▼
                 PostgreSQL Data Warehouse
                    Bronze → Silver → Gold
                               │
                               ▼
                      Business Analytics
                               │
                               ▼
                       Power BI Dashboard
```

---

# ⚙️ Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Database | PostgreSQL |
| Workflow Orchestration | Apache Airflow |
| Cloud Storage | AWS S3 |
| Containerization | Docker |
| Analytics | Power BI |
| Version Control | Git & GitHub |
| Testing | Pytest |
| Data Validation | Great Expectations |
| AWS SDK | Boto3 |

---

# 📂 Project Structure

```
healthcare-claims-data-platform/
│
├── airflow/
│   ├── dags/
│   ├── logs/
│   ├── plugins/
│   └── config/
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── archive/
│   └── rejected/
│
├── database/
│   ├── schema/
│   ├── migrations/
│   └── scripts/
│
├── etl/
│   ├── ingestion/
│   ├── validation/
│   ├── transformation/
│   ├── loading/
│   └── utils/
│
├── dashboard/
├── docs/
├── tests/
├── docker/
│
├── docker-compose.yml
├── requirements.txt
├── .env
├── README.md
└── .gitignore
```

---

# 🚀 Planned Features

- Daily Healthcare Claims Ingestion
- Automated ETL Pipelines
- Apache Airflow Scheduling
- AWS S3 Integration
- PostgreSQL Data Warehouse
- Data Quality Validation
- Error Logging
- Incremental Data Loading
- Duplicate Detection
- Healthcare Claims Analytics
- Power BI Dashboard
- Audit Logging
- Unit Testing
- CI/CD using GitHub Actions

---

# 📊 Data Model

The warehouse will include:

### Fact Tables

- Fact Claims

### Dimension Tables

- Members
- Providers
- Diagnosis (ICD-10)
- Procedures (CPT)
- Date
- Insurance Plan

---

# 📈 Business KPIs

The dashboard will provide insights including:

- Total Claims
- Approved Claims
- Denied Claims
- Pending Claims
- Approval Rate
- Denial Rate
- Average Claim Amount
- Total Paid Amount
- Claims by State
- Claims by Provider
- Claims by Diagnosis
- Claims by Insurance Plan

---

# 🔒 Data Quality Checks

The ETL pipeline validates:

- Duplicate Claim IDs
- Missing Member IDs
- Invalid Provider IDs
- Negative Claim Amounts
- Invalid Diagnosis Codes
- Invalid Procedure Codes
- Future Service Dates
- Missing Mandatory Fields

Invalid records are redirected to a rejection table for further analysis.

---

# 🎯 Learning Goals

This project demonstrates practical experience with:

- Data Engineering
- ETL Development
- Data Warehousing
- Apache Airflow
- PostgreSQL
- Docker
- AWS S3
- Python
- SQL Optimization
- Incremental Loading
- Data Quality
- Production-grade Pipeline Design

---

# 🚧 Project Status

> **Currently under active development.**

The project is being built incrementally to simulate a real-world enterprise healthcare claims processing platform.

---

# 👩‍💻 Author

**Nancy Srivastava**

Data Engineer | Python | SQL | AWS | Apache Airflow | PostgreSQL | Power BI
