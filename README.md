# 🛡️ Cyber Lab – Web Security & Python Fundamentals

A hands-on repository dedicated to learning web application cybersecurity and **Python** programming. This project combines practical implementation of web vulnerabilities with secure coding best practices and containerization.

---

## 🚀 Tech Stack & Tools

* **Programming Language:** Python 3.11+
* **Web Framework:** Flask
* **Database:** SQLite3
* **Containerization:** Docker
* **Operating System:** Fedora Linux
* **IDE / Environment:** VS Code (`venv`, Pylance)

---

## 🛠️ Laboratory Features (`app.py`)

1. **SQL Injection (SQLi) & Mitigation (`/login`)**
   * Demonstrates security risks associated with unstripped string concatenation in SQL queries.
   * Secures the login form using **parameterized queries (Prepared Statements)**.

2. **Reflected XSS & Mitigation (`/xss_page`)**
   * Illustrates Reflected Cross-Site Scripting (XSS) vulnerability via GET parameters.
   * Mitigates the risk by sanitizing special HTML characters using **`html.escape()`**.

3. **Python Fundamentals Course**
   * `lekcja1.py` – User input (`input`), type casting (`int`), f-strings, and dynamic calculations.
   * `lekcja2.py` – Conditional statements (`if`, `elif`, `else`) and decision-making logic.

---

## 🐳 Running with Docker

To run the full laboratory environment in an isolated Docker container:

1. **Build the Docker image:**
   ```bash
   docker build -t vulnerable-web .
