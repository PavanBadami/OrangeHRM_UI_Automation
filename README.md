# OrangeHRM UI Automation Framework

## Overview

This project is a UI Automation Framework developed for OrangeHRM using Python, Selenium, and PyTest.

## Tech Stack

* Python
* Selenium WebDriver
* PyTest
* WebDriver Manager
* PyTest HTML Reports
* Allure Reports

## Project Structure

* config/
* pages/
* tests/
* utilities/

## Run Tests

```bash
pytest
```

## Generate Allure Results

```bash
pytest --alluredir=allure-results
```

## Generate Allure Report

```bash
allure serve allure-results
```
