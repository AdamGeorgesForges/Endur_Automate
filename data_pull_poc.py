#This script assumes that you have access to Endur's database via an API or direct SQL access. It will extract trade data for a specific date range, perform some basic analysis, and then save a report to a CSV file.

import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plt

def connect_to_database():
    # This connection string will depend on your database setup
    # Currently connecting to dummy database
    try:
        #Connection string for SQLite database
        connection_string = "sqlite:///dummy_database.db" # Ensure this path is correct
        engine = sqlalchemy.create_engine(connection_string)
        return engine
    except sqlalchemy.exc.SQAlchemyError as e:
        print(f"Error connecting to the database:{e}")
        return None
    connection_string = "sqlite:///dummy_database.db" 
    engine = sqlalchemy.create_engine(connection_string)
    return engine

def fetch_trade_data(engine, start_date, end_date):
    query = f"""
    SELECT TradeID, TradeDate, Commodity, Quantity, Price
    FROM Trades
    WHERE TradeDate BETWEEN '{start_date}' AND '{end_date}'
    """
    return pd.read_sql(query, engine)

def generate_report(trade_data):
    summary = trade_data.groupby('Commodity').agg(Total_Quantity=('Quantity', 'sum'), Average_Price=('Price', 'mean'))
    print("Trade Summary:")
    print(summary)

    # Plotting
    summary['Total_Quantity'].plot(kind='bar', title='Total Quantity Traded by Commodity')
    plt.xlabel('Commodity')
    plt.ylabel('Total Quantity')
    plt.show()

def main():
    engine = connect_to_database()
    start_date = '2025-01-01'
    end_date = '2025-01-31'
    
    trade_data = fetch_trade_data(engine, start_date, end_date)
    generate_report(trade_data)

if __name__ == "__main__":
    main()
