# PROJECT_CONTEXT.md

# Project 2: AI SQL Analyst

## Date

Project Initialization

---

# Project Goal

Build an AI-powered SQL Analyst that allows users to upload structured datasets (CSV files), ask questions in natural language, automatically generate SQL queries using a local LLM, execute those queries on a SQLite database, and present results with tables, charts, and business insights.

This project focuses on understanding how LLMs interact with structured data rather than unstructured documents.

---

# Long-Term Roadmap

```text
CSV Upload
      ↓
SQLite Database
      ↓
Database Schema
      ↓
Prompt Construction
      ↓
Ollama (Phi-3)
      ↓
SQL Generation
      ↓
SQL Execution
      ↓
DataFrame
      ↓
Visualization
      ↓
Business Insights
```

---

# Learning Objectives

This project is intended to teach:

* SQLite
* Database design
* SQL
* Prompt Engineering
* LLM structured output
* Query validation
* Data visualization
* AI-assisted analytics

Unlike Project 1 (RAG), this project centers around structured data and SQL generation.

---

# Project Structure

```text
AI_SQL_Analyst/

├── app.py
├── requirements.txt
├── README.md
├── PROJECT_CONTEXT.md
├── .gitignore
│
├── data/
│   ├── raw/
│   └── database.db
│
├── sample_data/
│
├── screenshots/
│
├── tests/
│
└── src/
    ├── __init__.py
    ├── database.py
    ├── schema.py
    ├── prompt.py
    ├── llm.py
    ├── sql_generator.py
    ├── sql_executor.py
    ├── visualizer.py
    ├── insights.py
    └── utils.py
```

---

# Architecture Decisions

## 1. Source of Truth

The CSV file is only an import format.

After upload, the SQLite database becomes the single source of truth.

Future modules will read schema information directly from SQLite instead of repeatedly inspecting the uploaded CSV.

---

## 2. Data Flow

```text
Upload CSV
      ↓
Load into SQLite
      ↓
Read Database Schema
      ↓
Build Prompt
      ↓
Generate SQL
      ↓
Execute SQL
      ↓
Display Results
```

---

## 3. Module Responsibilities

### database.py

Responsible for:

* Creating SQLite connection
* Creating database
* Loading CSV into SQLite
* Listing available tables
* Database management

---

### schema.py

Responsible for:

* Reading database schema
* Listing tables
* Listing columns
* Reading column data types

This module should only inspect the database and should not generate SQL.

---

### llm.py

Responsible only for communicating with Ollama.

It should not contain SQL generation logic.

---

### sql_generator.py

Responsible for converting:

Natural Language

↓

SQL Query

using the database schema and the LLM.

---

### sql_executor.py

Responsible for:

* Executing SQL
* Returning results
* Handling SQL errors safely

---

### visualizer.py

Responsible for generating charts from query results.

---

### insights.py

Responsible for generating business insights from the returned data.

---

# Product Decisions

Initially considered automatically using the CSV filename as the SQLite table name.

Potential issue:

```
doc_728t412_fb.csv
```

creates a poor table name.

Current plan:

Use the filename as a suggested default while allowing the user to edit the table name before importing.

This provides a better user experience without requiring unnecessary manual input.

---

# Tomorrow's Goal

Build **database.py**.

Target functionality:

```text
Upload sales.csv

↓

Connect to SQLite

↓

Create database

↓

Create table

↓

Insert rows

↓

Return:

Database Connected ✓

Table Created ✓

Rows Inserted: N
```

No LLMs yet.

Tomorrow is entirely focused on understanding SQLite and loading structured data correctly.

---

# Success Criteria

By the end of the next session, we should be able to:

* Import any CSV into SQLite.
* Verify the table exists.
* Verify the data was inserted successfully.
* Inspect the database manually.

Once this is working, we will begin building `schema.py`.

---

# Key Takeaway

Project 1 taught how LLMs retrieve knowledge from unstructured text.

Project 2 begins with teaching an LLM how to reason over structured data by leveraging SQL databases.
