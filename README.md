# Phishing Detection Mini Project

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-green)
![Level](https://img.shields.io/badge/Level-Beginner-orange)
![Focus](https://img.shields.io/badge/Focus-Cybersecurity-red)

## Overview  
This project is a beginner-level cybersecurity implementation using Python.  
It focuses on detecting phishing patterns in emails and identifying suspicious domains using simple logic.  
The main goal is to demonstrate basic programming, logical thinking, and understanding of real-world security problems.

---

## 🗂️ Project Structure

```
phishing-detection/
│
├── email_checker.py      # Checks if email content is phishing
├── domain_checker.py     # Compares domain similarity
└── README.md             # Project documentation
```
---

## Task 1: Basic Email Checker  

### Description  
This program analyzes an email message and checks for common phishing-related keywords.

### Keywords Checked  
- urgent  
- verify  
- password  
- bank  
- click  

### Logic  
- Convert input text to lowercase  
- Check if any risky keyword is present  
- Display a warning if found  

### Example  

**Input:**  
Enter the email content: Please verify your bank password urgently  

**Output:**  
Warning: This email may be risky  

**Input:**  
Enter the email content: Hello, how are you?  

**Output:**  
