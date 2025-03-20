# Ethereum Transaction Exporter

A Python tool that exports all types of Ethereum transactions (external, internal, and ERC20 token transfers) for a given wallet address to a CSV file.

## Features

- Fetches external transactions
- Fetches internal transactions
- Fetches ERC20 token transfers
- Sorts all transactions by timestamp
- Exports to CSV with detailed transaction information
- Rate limiting and retry logic for API calls
- Comprehensive test coverage

## Prerequisites

- Python 3.11 or higher
- Poetry for dependency management
- Etherscan API key

## Installation

1. Clone the repository:

```bash
git clone https://github.com/abnerhussin/eth-transaction-exporter.git
cd eth-transaction-exporter
```

2. Install dependencies using Poetry:

```bash
poetry install
```

3. Create a `.env` file in the project root and add your Etherscan API key:

```bash
ETHERSCAN_API_KEY=your_api_key_here
```

## Usage

Run the script with an Ethereum address:

```bash
poetry run python -m src.main 0x742d35Cc6634C0532925a3b844Bc454e4438f44e
```

Optional parameters:

- `--output`: Specify custom output file path (default: transactions.csv)

Example with custom output:

```bash
poetry run python -m src.main 0x742d35Cc6634C0532925a3b844Bc454e4438f44e --output my_transactions.csv
```

## Output Format

The CSV file contains the following columns:

- Transaction Hash
- Date & Time
- From Address
- To Address
- Transaction Type (external/internal/erc20)
- Asset Contract Address
- Asset Symbol / Name
- Token ID
- Value / Amount
- Gas Fee (ETH)

## Project Structure

```
eth-transaction-exporter/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── transaction.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── etherscan_service.py
│   │   └── transaction_processor.py
│   └── utils/
│       ├── __init__.py
│       └── csv_writer.py
├── tests/
│   ├── __init__.py
│   ├── test_etherscan_service.py
│   ├── test_transaction_processor.py
│   └── test_csv_writer.py
├── .env
├── .gitignore
├── pyproject.toml
└── README.md
```

## Testing

Run the test suite:

```bash
poetry run pytest tests/
```

## Rate Limiting

The tool implements rate limiting to comply with Etherscan API limits:

- 200ms delay between requests
- Maximum 3 retries for failed requests
- Exponential backoff between retries

## Error Handling

- Graceful handling of API errors
- Retry mechanism for network issues
- Proper error messages for invalid addresses
- UTF-8 encoding support for CSV output

## Dependencies

- web3: ^6.15.1
- requests: ^2.31.0
- python-dotenv: ^1.0.0
- pandas: ^2.2.1

## Development

1. Install development dependencies:

```bash
poetry install --with dev
```

2. Run tests:

```bash
poetry run pytest
```

3. Format code:

```bash
poetry run black src/ tests/
poetry run isort src/ tests/
```

## Contact Info

- **Email**: [abner04222020@gmail.com](mailto:abner04222020@gmail.com)
- **WhatsApp**: [+63 954 331 2781](https://wa.me/639543312781)
