# QA Automation Framework | Python & Selenium

![Build Status](https://github.com/Cau393/qa-automation-portfolio/actions/workflows/test_pipeline.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-4.0+-green.svg)

## 📌 Project Overview

This repository hosts a scalable **Test Automation Framework** designed to validate critical user flows for e-commerce and ticketing platforms. It utilizes the **Page Object Model (POM)** design pattern to ensure code maintainability and separation of concerns.

The framework is integrated with **GitHub Actions** for Continuous Integration (CI), executing regression tests automatically on every code push, and generates detailed **Allure Reports** for test visualization.

## 🛠 Tech Stack

* **Language:** Python 3.10+
* **Web Driver:** Selenium WebDriver
* **Test Runner:** Pytest
* **Reporting:** Allure Reports
* **CI/CD:** GitHub Actions
* **Utilities:** Python-Dotenv (Environment Management), WebDriver Manager

## 📂 Project Structure

```text
qa-automation-portfolio/
├── .github/
│   └── workflows/
│       └── test_pipeline.yml  # CI/CD Pipeline configuration
├── pages/
│   ├── base_page.py           # Base class with generic Selenium wrappers
│   └── login_page.py          # Page Object for Login screen
├── tests/
│   ├── conftest.py            # Pytest fixtures (Setup/Teardown)
│   └── login_test.py          # Test scenarios
├── .env                       # Environment variables (Ignored by Git)
├── pytest.ini                 # Pytest configuration
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation