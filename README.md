# Industrial Sensor Data Analysis & Monitoring

## 1. Project Overview

This project aims to develop a Python-based workflow for preparing, validating, analyzing, and visualizing industrial sensor data.

The goal is to transform raw sensor measurements into structured, reliable datasets that can be used for exploratory analysis and monitoring through Power BI.

The project combines data analysis, data quality testing, and business intelligence in a practical industrial use case.

## 2. Objectives

 - Explore and understand the structure of an industrial sensor dataset.
 - Load, inspect, clean, and transform data using Python and pandas.
 - Develop reusable data quality validation checks.
 - Test validation logic using pytest.
 - Analyze sensor measurements and component condition data where appropriate.
 - Prepare structured datasets for Power BI.
 - Document the workflow to make it reproducible and understandable.

 ## 3. Data Source

**Dataset:** Condition Monitoring of Hydraulic Systems
<br>
**Source:** UCI Machine Learning Repository
<br>
**Dataset URL:** https://archive.ics.uci.edu/dataset/447/condition+monitoring+of+hydraulic+systems 

The dataset will be inspected before defining the final data preparation and validation rules.

This is a public research dataset. I do not claim ownership of the original dataset. It is used for educational and portfolio purposes in accordance with the applicable license and attribution requirements.

## 4. Tools and Technologies

**Python**: data processing and analysis.
<br>
**pandas**: data inspection, transformation, and aggregation.
<br>
**pytest**: automated testing of data validation logic
<br>
**PowerBI**: data visualization and dashboard development

## 5. Project Workflow

### Phase 1: Data Understanding

- Inspect the source files and their structure.
- Identify relevant columns, data types, and measurement formats.
- Explore basic statistics and potential data quality issues.

### Phase 2: Data Preparation

- Load and organize the raw data.
- Standardize column names and data types where necessary.
- Create useful sensor summaries and aggregates.
- Combine relevant datasets when their structures allow it.

### Phase 3: Data Quality Validation

- Check required columns and expected data types.
- Identify missing values.
- Validate numerical ranges where justified.
- Check for unexpected duplicates and other consistency issues.
- Write automated tests using pytest.

### Phase 4: Data Analysis and Visualization

- Explore sensor measurements and trends.
- Compare measurements with component condition information where appropriate.
- Prepare clean, structured outputs for Power BI.
- Develop a dashboard based on verified findings.

### Phase 5: Documentation and Presentation

- Document the setup and workflow.
- Explain data quality rules and design decisions.
- Present key findings and limitations.
