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
This email looks safe  

---

## Task 2: Domain Check  

### Description  
This program checks whether a website is safe or potentially suspicious by comparing it with a list of trusted domains.

### Logic Used  
- Accepts a single website input  
- Converts it to lowercase (case-insensitive handling)  
- Uses a predefined list of trusted domains:  
  - google.com  
  - chatgpt.com  
  - facebook.com  
  - amazon.com  

- Applies normalization to detect phishing tricks:  
  - 0 → o  
  - 1 → l  

- Compares:  
  - Exact match → Safe  
  - Match after normalization → Suspicious  
  - No match → Unknown  

---

### Example Explanations  

**Exact Match (Safe)**  
Input: google.com  
Output: Domain is safe  

**Phishing Attempt (Similar Domain)**  
Input: g00gle.com  
Process: g00gle.com becomes google.com after normalization  
Output: Suspicious domain  

**Unknown Website**  
Input: mysite123.com  
Output: Unknown domain  

**Case Variation (Safe)**  
Input: gOOgle.com  
Output: Domain is safe  

---

## Task 3: Use Case  

This system can be used as a background security tool in apps.  
It can be used in browsers to warn users before opening fake websites.  
It can also be built as a website where users can check links for safety.  
Companies can use it to protect user accounts and sensitive data.  
It helps users avoid scams and improve online security.  
It is an effective technique that helps prevent attacks before they reach the user.

---

## Key Learnings  

- Importance of input validation  
- Basic understanding of phishing attacks  
- Applying simple logic to real-world problems  
- Improving basic ideas into practical solutions  

---

## Future Improvements  

- Add more phishing patterns (such as rn → m, vv → w)  
- Use machine learning for better detection  
- Build a web interface using Flask or Django  
- Create a browser extension  
- Integrate real-time URL checking APIs  

---

## Conclusion  

This project shows how simple logic can be used to detect phishing attempts.  
Even though it is basic, it gives a good foundation for building more advanced security systems.

---

## Author  

- Santhosh U  
- Student | AI & ML Enthusiast  
