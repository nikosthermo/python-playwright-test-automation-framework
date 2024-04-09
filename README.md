# Python Test Automation Project

This project is a test automation suite for an e-commerce website, utilizing Playwright with Python and pytest. The tests are structured around the Page Object Model (POM) for better maintainability and readability.

## Project Structure

The project structure is as follows:

```
python-playwright-test-automation-framework/
│
├── .gitignore # Specifies intentionally untracked files to ignore
├── README.md # Project description and documentation
├── requirements.txt # Python dependencies for the project
│
├── pages/ # Page objects
│ ├── init.py
│ ├── login_page.py
│ ├── products_page.py
│ └── cart_page.py
│
└── tests/ # Test cases
├── init.py
├── test_login.py
├── test_products_page.py
└── test_cart_page.py
```

## Setup Instructions

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**

- **git clone https://github.com/nikosthermo/python-playwright-test-automation-framework.git**

2. **Navigate to the project directory**

- **cd python-playwright-test-automation-framework**

3. **Create and activate a virtual environment**

- **Linux/macOS**

  ```
  python3 -m venv venv
  source venv/bin/activate
  ```
  
4. **Install the dependencies**

  ```
  pip install -r requirements.txt
  ```

5. **Set up environment variables**

Create a `.env` file in the project root directory and add the following variables:

```
USERNAME=<your_username>
PASSWORD=<your_password>
```

6. **Run the tests**

To run all tests, execute the following command from the project root directory:

- **pytest**


### Additional Information

- **Using Playwright**: This project utilizes Playwright for browser automation. For more detailed documentation on Playwright, visit [Playwright Documentation](https://playwright.dev/python/docs/intro).

- **Page Object Model (POM)**: This design pattern is used to enhance test maintenance and reduce code duplication. Each page object class represents a page in the web application, encapsulating all functionalities and elements of that page.

## Contributing

Contributions are welcome! Please read the contributing guidelines before submitting pull requests to the project.

## License

MIT License
