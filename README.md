# CRED Fintech Web App - Stock Portfolio Tracker

## Introduction

Welcome to the CRED Fintech Web App - Stock Portfolio Tracker! This application is designed to help users manage and track their stock investments effectively. Built on Django, PostgreSQL, and psycopg2, it provides a seamless experience for users to add stocks to their portfolio and monitor their progress over time.

## Demo


https://github.com/AjinkyaSalunke22/CRED-Fintech-Investment-Tracking-Feature/assets/114003751/d14b18db-faac-46c3-b8b2-368ae109d63e
  


## Features

- **Stock Portfolio Management**: Ability for users to add, edit, and delete stocks from their portfolio.
- **Portfolio Summary**: View a summary of all stocks in the portfolio including current value and performance.
- **Responsive Design**: User-friendly interface accessible from desktop and mobile devices.

## Installation

To run the application locally, follow these steps:

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/AjinkyaSalunke22/CRED-Fintech-Investment-Tracking-Feature.git
   ```

2. Navigate to the project directory.
   ```bash
   cd CRED
   ```

3. Install the dependencies using pip.
   ```bash
   please read requirements
   ```

4. Configure the PostgreSQL database settings in `settings.py`.

5. Apply migrations to create the necessary database schema.
   ```bash
   python manage.py migrate
   ```

6. Start the development server.
   ```bash
   python manage.py runserver
   ```

7. Access the application by visiting `http://localhost:8000/add_stock` in your web browser.


## Requirements

Django==5.0.2
psycopg2==2.9.9
postgress==16.2
bootstrap==v5.3

## Usage

1. Add stocks to your portfolio by providing the stock symbol/ticker, quantity, purchase price, and purchase date.
2. View your portfolio to see a summary of all stocks, including current value and performance.
3. Edit or delete stocks as needed.
4. Explore additional features such as transaction history and real-time stock data to make informed investment decisions.

## Contributors

- Ajinkya Salunke (@ajinkya salunke) - Backend Developer

## Support

For any inquiries or issues, please contact [support@ajinkya.salunke.official@gmail.com](mailto:ajinkya.salunke.official@gmail.com).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
