# py-test-training

A comprehensive Python testing training project designed to teach pytest fundamentals through practical examples. This repository contains multiple modules covering different aspects of Python development, each with corresponding test suites to demonstrate pytest best practices, fixtures, mocking, and testing patterns.

## Project Structure

```
py-test-training/
├── README.md
├── requirements.txt
├── 01_basic_calculator/
│   ├── __init__.py
│   ├── calculator.py
│   └── test_calculator.py
├── 02_string_processing/
│   ├── __init__.py
│   ├── text_utils.py
│   └── test_text_utils.py
├── 03_data_structures/
│   ├── __init__.py
│   ├── custom_list.py
│   └── test_custom_list.py
├── 04_file_operations/
│   ├── __init__.py
│   ├── file_manager.py
│   └── test_file_manager.py
├── 05_web_scraping/
│   ├── __init__.py
│   ├── scraper.py
│   └── test_scraper.py
└── 06_networking/
    ├── tcp_client.py
    ├── tcp_server.py
    ├── tcp_socket.py
    ├── crypto_tcp_client.py
    ├── crypto_tcp_server.py
    ├── crypto_utils.py
    ├── test_tcp_socket.py
    ├── test_crypto_tcp.py
    └── test_crypto_utils.py
```

## Modules Overview

### 01_basic_calculator
Learn fundamental testing concepts with a simple calculator module. Practice testing mathematical operations, edge cases, and error handling.

### 02_string_processing
Explore text manipulation functions and advanced string testing techniques including parameterized tests and assertion methods.

### 03_data_structures
Test custom data structures and collections. Learn about testing class methods, properties, and complex data operations.

### 04_file_operations
Master file I/O testing with temporary files, mocking filesystem operations, and testing file manipulation functions safely.

### 05_web_scraping
Practice testing web scraping functionality using mocking techniques to simulate HTTP requests and responses without external dependencies.

### 06_networking (Optional)
Advanced networking concepts including TCP client/server testing. This module demonstrates testing network protocols and socket operations.

## Getting Started

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   # or .venv\Scripts\activate  # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run all tests:
   ```bash
   pytest
   ```

4. Run tests for a specific module:
   ```bash
   pytest 01_basic_calculator/
   ```

## Learning Objectives

- Understanding pytest fundamentals and test discovery
- Writing effective test cases and assertions
- Using fixtures for test setup and teardown
- Parameterized testing for multiple test scenarios
- Mocking external dependencies and APIs
- Testing exceptions and error conditions
- Code coverage analysis and reporting