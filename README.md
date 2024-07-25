# Wallet Address Clustering

This repository focuses on clustering wallet addresses for cryptocurrencies. The project explores two distinct approaches based on different types of cryptocurrencies:

1. **UTXO-based cryptocurrencies**
2. **Account-based cryptocurrencies**

Currently, the work has begun on account-based cryptocurrencies, utilizing Ethereum data from a public BigQuery dataset.

## Project Status

🚧 **Under Construction** 🚧  
This repository is a work in progress. The development is ongoing, and contributions or suggestions are welcome.

## Purpose

The primary goal of this project is to explore and demonstrate methods for clustering wallet addresses in the crypto ecosystem, providing insights into transaction patterns, user behavior, and network analysis.

## Technologies Used

- **BigQuery**: For data extraction from the public Ethereum dataset.
- **Python**: For data processing, analysis, and modeling.
- **Google Cloud CLI**: Used for authentication and interaction with Google services. Documentation available [here](https://cloud.google.com/docs/authentication/gcloud?hl=es-419#gcloud-credentials).

## Data Source

The Ethereum data used in this project is sourced from the public dataset available on BigQuery. Access the dataset [here](https://console.cloud.google.com/bigquery?ws=!1m4!1m3!3m2!1sbigquery-public-data!2scrypto_ethereum).

## Project Structure

- `account-based-clustering/`: Directory containing the clustering process for account-based cryptocurrencies
- `utxo-based-clustering/`: Directory containing the clustering process for utxo-based cryptocurrencies
- `requirements.txt`: Python requirements

## Current Progress

### Account-based Cryptocurrencies

1. **Data Preprocessing**: Cleaning and preparing data from the Ethereum dataset.
2. **Feature Engineering**: Creating variables to improve the clustering model.
3. **Clustering**: Implementation of the K-means algorithm. The Elbow method will be used to determine the optimal number of clusters.

### Next Steps

1. Finalize feature engineering to enhance the K-means clustering model.
2. Implement the Elbow method to identify the optimal number of clusters.
3. Develop clustering heuristics for UTXO-based cryptocurrencies.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request with your suggestions or improvements.

## Acknowledgements

- **BigQuery Public Datasets**: For providing comprehensive and accessible blockchain data.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Note**: This README will be updated regularly as the project progresses.
