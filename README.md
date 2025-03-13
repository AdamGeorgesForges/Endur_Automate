# Endur Automate Project

## Project Overview
This project includes scripts for setting up and interacting with a local SQLite database that simulates the functionality needed to integrate and test with the Endur trading and risk management platform. The primary goal is to demonstrate how to automate data extraction, analysis, and visualization tasks using Python and SQLite, which can be adapted for similar purposes in trading environments.

## Prerequisites
Before you begin, you will need:
- Python 3.8 or higher
- Required Python libraries: `pandas`, `sqlalchemy`, and `matplotlib`. You can install these using pip:
  ```
  pip install pandas sqlalchemy matplotlib
  ```

## Setup Instructions
To get started with this project, follow these setup instructions:

### Clone the Repository
If available, clone the repository using Git:
```
git clone <repository-url>
cd <repository-directory>
```

### Install Dependencies
Ensure all required Python libraries are installed:
```
pip install -r requirements.txt
```

## How to Run

### Running the Database Creation Script
Navigate to the directory containing `create_sqlite_database.py` and execute the script:
```
python create_sqlite_database.py
```
This will create a SQLite database named `dummy_database.db` and populate it with initial trading data.

### Running the Data Analysis Script
To run the data analysis and visualization script, use the following command:
```
python data_pull_poc.py
```
This script will connect to the `dummy_database.db`, fetch data for a specified date range, generate a summary report, and visualize the data using a bar chart.

## Script Functionalities

### `create_sqlite_database.py`
- Creates a SQLite database and a table named `Trades`.
- Populates the `Trades` table with sample trading data.
- Features error handling to manage database connection issues and SQL execution errors.

### `data_pull_poc.py`
- Connects to the `dummy_database.db` SQLite database.
- Fetches trade data based on a specified date range.
- Generates a summary of trades, including total quantities and average prices by commodity.
- Visualizes the trading data using a bar chart.
- Includes error handling for scenarios such as no data returned or database connection failures.

## Troubleshooting
- **Database Connection Issues**: Ensure the SQLite database path in the scripts is correct and accessible.
- **Library Dependencies**: If you encounter errors related to missing libraries, confirm that all required Python packages are installed.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your enhancements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.