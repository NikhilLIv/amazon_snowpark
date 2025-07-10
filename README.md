
# Amazon Sales Data Pipeline with Snowflake, Snowpark, and Airflow (Astro)

## 📈 Project Overview

This project demonstrates an **end-to-end data pipeline** using:

- **Airflow (Astro)** for orchestration
- **Snowflake & Snowpark** for scalable data processing
- **Local Amazon sales CSV data** as the source

The pipeline **extracts Amazon sales data from your local system, uploads it to a Snowflake stage, transforms it using Snowpark, and loads it into Snowflake tables for analytics-ready consumption.**

---

## 🛠️ Tech Stack

- **Airflow (Astro CLI)**: Orchestration
- **Snowflake**: Cloud Data Warehouse
- **Snowpark**: In-Snowflake processing
- **Python**: ETL scripts
- **Docker**: Containerization (via Astro)
- **Git**: Version control

---

## 📂 Project Structure

\`\`\`
.
├── dags/
│   └── amazon_sales_pipeline.py        # Airflow DAG for orchestrating the pipeline
├── include/
│   └── sample_amazon_sales.csv         # Sample local sales data
├── plugins/
│   └── snowflake_helpers.py            # Helper functions for Snowflake connection and Snowpark processing
├── requirements.txt                    # Python dependencies
└── README.md                           # Project documentation
\`\`\`

---

## ⚡ Pipeline Flow

1️⃣ **Extract:**  
Load Amazon sales data from local CSV into Snowflake stage using Snowflake Python Connector.

2️⃣ **Transform:**  
Use **Snowpark** to clean, transform, and enrich the data inside Snowflake.

3️⃣ **Load:**  
Load the transformed data into analytics-ready Snowflake tables.

4️⃣ **Orchestrate:**  
The entire workflow is managed by **Airflow (Astro)** for easy scheduling, monitoring, and scaling.

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository

\`\`\`bash
git clone https://github.com/yourusername/amazon-sales-pipeline.git
cd amazon-sales-pipeline
\`\`\`

---

### 2️⃣ Install Astro CLI

Follow official instructions:  
[Astro CLI Installation](https://docs.astronomer.io/astro/cli/install-cli)

---

### 3️⃣ Configure Snowflake Connection

Add your Snowflake connection to Airflow:

\`\`\`bash
astro dev init
\`\`\`

Update your \`airflow_settings.yaml\` or add the connection manually in the Airflow UI:

- **Conn ID:** \`snowflake_conn\`
- **Conn Type:** \`Snowflake\`
- **Account:** \`your_account\`
- **User:** \`your_user\`
- **Password:** \`your_password\`
- **Database:** \`your_database\`
- **Warehouse:** \`your_warehouse\`
- **Schema:** \`your_schema\`

---

### 4️⃣ Start the Astro Dev Environment

\`\`\`bash
astro dev start
\`\`\`

Access Airflow at [http://localhost:8080](http://localhost:8080).

---

### 5️⃣ Trigger the DAG

- Go to the Airflow UI.
- Enable and trigger the \`amazon_sales_pipeline\` DAG.
- Monitor task execution and logs.

---

## 🧪 Testing

- **Unit tests** for Snowflake/Snowpark logic can be added using \`pytest\`.
- Validate the loaded data in Snowflake using SQL Workbench or Snowflake UI.

---

## 📊 Future Enhancements

✅ Add data quality checks using **Great Expectations**  
✅ Parameterize file paths and table names for flexibility  
✅ Integrate **dbt for transformation layer**  
✅ Add **notifications on pipeline failures**  

---

## 🤝 Contributing

PRs are welcome! Please fork the repo and submit pull requests for any improvements.

---

## 📝 License

This project is licensed under the MIT License.

---

## 📬 Contact

For queries or collaborations, reach out via [vatsanikhil@gmail.com](mailto:vatsanikhil@gmail.com) or [LinkedIn](https://www.linkedin.com/in/nikhil-vatsa-29960517b/).

---

### ⭐ If you find this helpful, please consider giving the repository a star!
