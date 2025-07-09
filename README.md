Amazon Sales Data Pipeline with Snowflake, Snowpark, and Astro (Airflow)
📈 Project Overview
This repository contains an end-to-end data engineering pipeline using:

Snowflake (data warehousing, staging, transformation)

Snowpark (Python-based transformations inside Snowflake)

Astro (Astronomer Airflow) for robust orchestration and scheduling

The pipeline ingests Amazon Sales Data from local CSV files for:

India (amazon_sales_india.csv)

France (amazon_sales_france.csv)

US (amazon_sales_us.csv)

and transforms them into a curated star schema for analytics and reporting.

🗂️ Pipeline Stages
Ingestion:

Local Amazon sales CSV files are uploaded to a Snowflake stage.

Loading to Source Table:

Data is loaded from the stage into raw source tables in Snowflake.

Curated Transformations:

Data is cleaned, enriched, and unified across India, France, and US datasets using Snowpark Python scripts.

Star Schema Creation (Consumption Layer):

Transformed data is loaded into fact and dimension tables:

fact_sales

dim_customer

dim_product

dim_date

Orchestration with Astro Airflow:

The pipeline is orchestrated using Astro (Astronomer):

Automated DAG scheduling and execution

Logging, monitoring, and observability

Clear separation of ingestion, transformation, and loading tasks

🛠️ Tech Stack
Snowflake: Data warehouse for staging, storage, and transformation

Snowpark (Python): In-database scalable transformations

Astro (Astronomer): Managed Airflow orchestration

Python: Snowpark scripts, utility scripts, and DAG development

🚀 Setup Instructions
1️⃣ Prerequisites
Snowflake account with appropriate roles (SYSADMIN, ACCOUNTADMIN, or pipeline-specific role)

Astro CLI installed (curl -sSL https://install.astronomer.io | sh)

Astronomer workspace with Airflow deployment

Python 3.8+ locally for development

Snowflake connection credentials ready

2️⃣ Snowflake Configuration
Create a stage in Snowflake for file ingestion.

Create databases and schemas for:

SOURCE

CURATED

CONSUMPTION

Set up Snowflake connection in Astro Airflow UI or in your connections.toml for local development.

3️⃣ File Structure
kotlin
Copy
Edit
.
├── dags/
│   └── amazon_sales_pipeline_dag.py
├── include/
│   ├── ingest_india.py
│   ├── ingest_france.py
│   ├── ingest_us.py
│   ├── transform_curated.py
│   └── build_star_schema.py
├── data/
│   ├── amazon_sales_india.csv
│   ├── amazon_sales_france.csv
│   └── amazon_sales_us.csv
├── Dockerfile
├── requirements.txt
└── README.md
4️⃣ Running the Pipeline with Astro
🔹 Clone and initialize Astro
bash
Copy
Edit
git clone <repo-url>
cd <repo-folder>
astro dev init
🔹 Start Astro Airflow locally
bash
Copy
Edit
astro dev start
This will:

Start Airflow in your local environment using Docker.

Expose the Airflow UI at http://localhost:8080.

🔹 Load your CSV files
Place your CSV files into the data/ folder.

🔹 Trigger the DAG
Open http://localhost:8080

Enable and trigger amazon_sales_pipeline_dag

The DAG will:
✅ Upload data to Snowflake stage
✅ Load to source tables
✅ Run Snowpark transformations
✅ Load curated tables
✅ Build star schema in the consumption layer

📊 Expected Outputs
✅ Curated clean tables in Snowflake
✅ Star Schema in CONSUMPTION Layer:

fact_sales

dim_customer

dim_product

dim_date

✅ Fully automated Astro Airflow orchestration for your Amazon sales data pipeline

🧩 Key Features
✅ End-to-end ELT pipeline using Snowflake, Snowpark, and Astro Airflow
✅ Modular and reusable Snowpark transformation scripts
✅ Airflow DAG orchestration with clear task separation
✅ Scalable and easy local development using Astro CLI
✅ Multi-region dataset integration (India, France, US)
✅ Star schema design for reporting and analytics

🤝 Contributing
Contributions to enhance:

Unit tests with pytest

dbt integration

Data quality checks (e.g., Great Expectations)

CI/CD with Astro Cloud and GitHub Actions

are welcome. Please open an issue or submit a PR.
