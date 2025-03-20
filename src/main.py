import argparse
from src.services import EtherscanService, TransactionProcessor
from src.utils import CSVWriter


def main():
    parser = argparse.ArgumentParser(
        description="Export Ethereum wallet transactions to CSV"
    )
    parser.add_argument("address", help="Ethereum wallet address")
    parser.add_argument(
        "--output", default="transactions.csv", help="Output CSV file path"
    )
    args = parser.parse_args()

    try:
        # Initialize services
        etherscan = EtherscanService()
        processor = TransactionProcessor()

        print(f"Fetching transactions for address: {args.address}")

        # Fetch all transaction types
        transactions = []

        # External transactions
        print("Fetching external transactions...")
        external_txs = etherscan.get_external_transactions(args.address)
        transactions.extend([processor.process_external_tx(tx) for tx in external_txs])

        # Internal transactions
        print("Fetching internal transactions...")
        internal_txs = etherscan.get_internal_transactions(args.address)
        transactions.extend([processor.process_internal_tx(tx) for tx in internal_txs])

        # ERC20 transfers
        print("Fetching ERC20 transfers...")
        erc20_txs = etherscan.get_erc20_transfers(args.address)
        transactions.extend([processor.process_erc20_tx(tx) for tx in erc20_txs])

        # Sort transactions by timestamp
        transactions.sort(key=lambda x: x.timestamp)

        # Write to CSV
        print(f"Writing {len(transactions)} transactions to {args.output}")
        CSVWriter.write_transactions(transactions, args.output)

        print("Export completed successfully!")

    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)


if __name__ == "__main__":
    main()
