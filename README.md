# API Testing Framework

A Python-based API testing framework built with Pytest and Requests, following DRY and SOLID principles.

![API Testing Demo](calendar_pytest/multimedia/api%20gif.gif)

## Setup Instructions

### 0. Create Virtual Environment (Recommended)

Create and activate a virtual environment to isolate project dependencies:

**Windows:**
```bash
python -m venv .venv
# Windows (cmd)
.\.venv\Scripts\activate

# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

You should see `(.venv)` in your terminal prompt when activated.

### 1. Install Dependencies

Ensure your virtual environment is activated, then install:

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Copy `.env.example` to `.env` and add your API credentials:

```bash
cp .env.example .env
```

Edit `.env` and add your Calendarific API key:

```
CALENDARIFIC_API_KEY=your_actual_api_key_here
```

### 3. Run Tests

Run all tests:
```bash
pytest
```

Run specific test file:
```bash
pytest calendar_pytest/tests/test_name.py
```

Run with verbose output:
```bash
pytest -v
```

Run tests in parallel:
```bash
pytest -n auto
```

Generate HTML report:
```bash
pytest --html=report.html
```

## Framework Features

### DRY Principles
- Shared fixtures in `conftest.py`
- Reusable API client classes
- Common helpers and utilities
- Centralized configuration management

### Key Components

#### 1. Data Models (Dataclasses)
- Type-safe response models
- Automatic validation through type hints
- Easy JSON to Python object conversion
- Located in `calendar_pytest/src/models/`

#### 2. API Clients
- Clean, reusable request methods
- Built-in logging and error handling
- Context manager support
- Located in `calendar_pytest/src/requests/`

#### 3. Configuration Management
- Environment-based configuration
- Centralized in `common/configuration.py`
- API keys never hardcoded

#### 4. Common Utilities
- Logging helpers
- Validation functions
- Response parsing
- Located in `common/helpers.py`


