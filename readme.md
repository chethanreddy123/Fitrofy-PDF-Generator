# README.md

## Introduction

This repository contains a FastAPI application that provides an endpoint to generate a PDF document based on user details and diet plans. Additionally, it includes instructions on installing a necessary component called Playwright.

## Installation

To install the required components, follow these steps:

1. Install the Playwright component by running the following command:

    ```bash
    playwright install
    ```

2. Install the Python dependencies using `pip`. You can create a virtual environment first if needed:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### FastAPI Endpoint: `/get_user_and_diet_pdf`

This FastAPI endpoint generates a PDF document containing user details and diet plans.

#### Request

- **Method:** GET
- **Path:** `/get_user_and_diet_pdf`
- **Query Parameters:**
  - `auth_token` (str): Authentication token.
  - `date_range` (int): Date range for diet plans.
  - `date` (str): Date for diet plans.

#### Example Request

```bash
curl -X 'GET' \
  'http://localhost:8000/get_user_and_diet_pdf?auth_token=YOUR_AUTH_TOKEN&date_range=7&date=24012024' \
  -H 'accept: application/pdf'
```

#### Response

The endpoint returns a PDF document containing user details and diet plans.

### Playwright Installation

Playwright is a component that might be required for this application. Install it by running the following command:

```bash
playwright install
```

This command ensures the necessary dependencies are installed for Playwright to function correctly.

## Additional Notes

- Ensure that the required dependencies are installed by following the provided installation instructions.
- The FastAPI application uses the provided `fetch_user_details` and `get_diet_plans` functions from the `helper` module to retrieve user details and diet plans.
- Logging is implemented using the Loguru library. Log messages can be found in the application's logs.
- The Playwright component is crucial for the proper functioning of the application and should be installed as instructed.

Feel free to adapt and modify the code as needed for your specific use case. If you encounter any issues or have questions, refer to the provided information or reach out for assistance.