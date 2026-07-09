# AI Assisted QA Bug Analyzer

This project demonstrates a QA automation framework developed with Python, Selenium WebDriver and Pytest to practice modern UI automation techniques and structured bug analysis.

The project demonstrates modern QA Automation practices, including:

* End-to-End UI testing.
* Data-driven testing using `pytest.mark.parametrize`.
* Reusable Pytest fixtures.
* Automatic screenshot capture on test failures.
* Automatic bug report generation.
* Extensible bug analysis module designed for future AI integration.

---

## Features

* ✅ Selenium Web UI Automation.
* ✅ Pytest Test Framework.
* ✅ Page Object Model (POM).
* ✅ Positive and Negative test scenarios.
* ✅ Data-driven testing with `pytest.mark.parametrize`.
* ✅ Reusable Pytest fixtures.
* ✅ Automatic screenshot capture on failed tests.
* ✅ Automatic bug report generation.
* ✅ Automatic collection of browser and URL information.
* ✅ Extensible bug analysis layer (currently rule-based).

---

## Project Architecture

The framework separates responsibilities into dedicated layers:

* **Pages** – Encapsulate UI interactions.
* **Tests** – Contain business scenarios and assertions.
* **Fixtures** – Manage browser lifecycle and login setup.
* **Utilities** – Handle screenshots, bug reports, and analysis logic.
* **Pytest Hooks** – Automatically collect artifacts when a test fails.

---

## Project Structure

```text
AI_Assisted_QA_Bug_Analyzer/
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── checkout_overview_page.py
│
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── utils/
│   ├── screenshot_helper.py
│   ├── bug_report_generator.py
│   └── ai_bug_analyzer.py
│
├── reports/
│   ├── screenshots/
│   └── bug_reports/
│
└── README.md
```

> The `reports/` directory is automatically generated during test execution and is excluded from version control via `.gitignore`.

---

## Running the Project

### Install dependencies

```bash
uv sync
```

### Run all tests

```bash
uv run pytest -v
```

### Run a specific test file

```bash
uv run pytest -v tests/test_checkout.py
```

---

## Automatic Failure Workflow

The framework automatically performs the following actions when a test fails:

1. Detects the failure using a Pytest hook.
2. Captures a browser screenshot.
3. Generates a structured bug report.
4. Records browser and current URL information.
5. Performs a basic rule-based bug analysis.

The generated artifacts are stored under the `reports/` directory during runtime.

---

## Bug Analysis Module

The project currently includes a rule-based bug analysis component designed as a foundation for future AI integration.

The project includes an extensible bug analysis component (`ai_bug_analyzer.py`).

The current implementation uses a lightweight **rule-based approach** to classify common Selenium failures (such as `NoSuchElementException`, `AssertionError`, and `TimeoutException`) and provide basic troubleshooting suggestions.

The architecture was intentionally designed to allow future replacement of this module with an LLM-powered solution (e.g., OpenAI API) without changing the surrounding framework.

---

## Future Improvements

* Integration with an LLM API for AI-powered bug analysis.
* HTML reporting (Allure / pytest-html).
* CI/CD integration with GitHub Actions.
* Automatic Jira ticket draft generation.
* Cross-browser execution support.

---

## Technologies Used

* Python 3.12
* Selenium WebDriver
* Pytest
* WebDriver Manager
* Pytest Fixtures
* Pytest Hooks
* Git & GitHub
* UV Package Manager
