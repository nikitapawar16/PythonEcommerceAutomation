# PythonEcommerceAutomation

## Overview
This project is an **automation testing framework** for an e-commerce website built using **Python** and **Selenium WebDriver**. It demonstrates end-to-end testing of login functionalities and other critical flows.

## Features
- Automation of login scenarios (valid and invalid credentials)
- Structured **Page Object Model (POM)** design
- Integration with **pytest** for test execution
- Dynamic waiting using **WebDriverWait** and **Expected Conditions**
- Reusable driver setup using a **driver factory**

## Project Structure
DreamPortalAutomationTesting-Python
│
├── .venv # Python virtual environment
├── tests # Test cases
│ ├── test_login.py
│ └── test_invalid_login.py
├── pages # Page objects
│ └── login_page.py
├── utils # Utility scripts
│ └── driver_factory.py
├── requirements.txt # Python dependencies
└── pytest.ini # Pytest configuration


## Installation
1. Clone the repository:
```bash
git clone https://github.com/nikitapawar16/PythonEcommerceAutomation.git
```

2. Navigate to project folder:
```bash
cd PythonEcommerceAutomation
```

3. Create and activate virtual environment:
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python -m venv .venv
source .venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests
To execute all tests using pytest:
```bash
python -m pytest -v
```

This will open the browser, perform login tests, and report results in the terminal.

## Key Technologies
- Python 3.x
- Selenium WebDriver
- pytest
- Page Object Model (POM)
- WebDriver Manager

## Author
Nikita Pawar
