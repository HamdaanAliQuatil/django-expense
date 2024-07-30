# Expense Sharing App

## Overview

The Expense Sharing App is a Django-based application for managing and sharing expenses. It allows users to create, view, and download expense reports. This document provides instructions on setting up the project, running the app, and using the available APIs.

## Table of Contents

- [Installation](#installation)
- [Setup](#setup)
- [Running the App](#running-the-app)
- [API Endpoints](#api-endpoints)
- [Running Tests](#running-tests)
- [License](#license)

## Installation

### Prerequisites

- Python 3.11 or later
- pip (Python package installer)

### Create and Activate Virtual Environment

1. **Create a virtual environment:**

   ```bash
   python -m venv env
    ```

2. **Activate the virtual environment:**

   - **Windows:**

     ```bash
     .\env\Scripts\activate
     ```

   - **Linux/macOS:**

     ```bash
     source env/bin/activate
     ```

### Install Dependencies
    
    ```bash
    pip install -r requirements.txt
    ```

## Setup

1. Apply Migration

    ```bash
    python manage.py migrate
    ```

2. Create Superuser

    ```bash
    python manage.py createsuperuser
    ```

## Running the App

1. **Run the server:**

    ```bash
    python manage.py runserver
    ```

    The app will be accessible at `http://localhost:8000/`.

    NOTE: All endpoints must end with a `/`. This can be disabled by setting `APPEND_SLASH = False` in `settings.py`.

## API Endpoints

Find the complete updated list of API endpoints in the [Postman API Documentation](https://documenter.getpostman.com/view/21657202/2sA3kbgdTg).

## Running Tests

1. Install pytest and pytest-django (if not already installed):

    ```bash
    pip install pytest pytest-django
    ```
2. Run tests:

    ```bash
    pytest
    ```

## License

This project is licensed under the BSD 3-Clause License. See the [LICENSE](LICENSE) file for more information.
```
