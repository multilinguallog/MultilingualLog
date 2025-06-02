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

 ## data
 The datasets and intermediate data used in thie repo is shown in
