import pandas as pd
from google.cloud import bigquery
from google.api_core.exceptions import GoogleAPIError
from google.oauth2 import service_account  # type: ignore
import googleapiclient.discovery  # type: ignore


def get_bigquery_client() -> bigquery.Client:
    """Initializes and returns a BigQuery client."""

    try:
        return bigquery.Client()
    except GoogleAPIError as e:
        print(f"Error initializing BigQuery client: {e}")
        raise


def execute_query(client: bigquery.Client, query: str) -> pd.DataFrame:
    """Executes a SQL query using BigQuery client and returns the result as a DataFrame."""

    try:
        query_job = client.query(query)
        return query_job.to_dataframe()
    except GoogleAPIError as e:
        print(f"Error executing query: {e}")
        raise


def process_data(df: pd.DataFrame) -> pd.DataFrame:
    """Processes the DataFrame by cleaning and transforming data."""

    df = df.drop(columns=['column_to_exclude'])
    df['decimals'] = pd.to_numeric(df['decimals'], errors='coerce')
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    df['value'] = df['value'] / (10 ** df['decimals'])
    df['block_timestamp'] = pd.to_datetime(df['block_timestamp'])
    df['tx_month'] = df['block_timestamp'].dt.month
    df['tx_year'] = df['block_timestamp'].dt.year
    return df


def main():
    """Main function to execute ETL process."""

    query = '''
    WITH transfers AS (
    SELECT 
      block_timestamp, 
      from_address, 
      to_address, 
      token_address, 
      value  
    FROM `bigquery-public-data.crypto_ethereum.token_transfers`  
    WHERE TIMESTAMP_TRUNC(block_timestamp, DAY) = TIMESTAMP("2024-07-22"))
    SELECT
      t.block_timestamp,
      t.from_address,
      t.to_address,
      t.value,
      tok.name,
      tok.symbol,
      tok.decimals,
      tok.total_supply
    FROM transfers t
    LEFT JOIN `bigquery-public-data.crypto_ethereum.tokens` tok ON t.token_address = tok.address
    '''

    client = get_bigquery_client()
    raw_data = execute_query(client, query)
    processed_data = process_data(raw_data)

    print(processed_data.head())


if __name__ == "__main__":
    main()
