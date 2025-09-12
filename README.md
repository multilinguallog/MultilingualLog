# Multilingual Log Parsing Framework

This repository supports the generation of multilingual (translated) log datasets and the evaluation of log parsing tools on these datasets.

## 📁 Folder Structure

- **`data_generation/`**  
  Contains all scripts and utilities for generating translated logs from English log datasets.  
  This includes:
  - Translating log templates using LLMs
  - Extracting and filling dynamic variables
  - Producing synthetic logs in multiple languages

- **`parsing_tool_test/`**  
  Contains scripts for evaluating log parsing tools.  
  This includes:
  - Running existing log parsers on both original and translated logs
  - Comparing the parsing results for consistency and accuracy

- **`downstream_file_generate/`**
  Contain scripts for generating parsing result files that can be used for DeepLog
  This includes:
  - Align the parsing results with timestamp-related information
 
## 🧪 How to Use

### Step 1: Generate Translated Logs
Run translated_file_gerator.py to generate translated template files

Run generator_main.py to generate translated logs

### Step 2: Generate parsing results and evaluate parsing results
Run tokenized_file_generator.py to generate tokenized log file for multilingual logs

Run parse.py to generate parsing result with different log parsers

Run group_result_check.py to generate result for group accuracy and group consistency. Files for manually labeling will also be generated.

 ## Data
 The datasets and intermediate data used in this repo are shown in: https://zenodo.org/records/15577263
