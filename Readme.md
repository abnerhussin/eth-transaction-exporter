# Ethereum Transaction Exporter

This tool exports transaction history for Ethereum wallet addresses to CSV format, including external transfers, internal transfers, and token transfers.

## Features

- Fetches external ETH transfers
- Fetches internal ETH transfers
- Fetches ERC-20 token transfers
- Fetches ERC-721 NFT transfers
- Exports all transactions to CSV with detailed information

## Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/eth-transaction-exporter.git
cd eth-transaction-exporter
```

2. Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with your Etherscan API key:
