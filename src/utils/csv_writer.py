import csv
from typing import List
from ..models.transaction import Transaction


class CSVWriter:
    @staticmethod
    def write_transactions(transactions: List[Transaction], filename: str):
        fieldnames = [
            "Transaction Hash",
            "Date & Time",
            "From Address",
            "To Address",
            "Transaction Type",
            "Asset Contract Address",
            "Asset Symbol / Name",
            "Token ID",
            "Value / Amount",
            "Gas Fee (ETH)",
        ]

        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for tx in transactions:
                writer.writerow(
                    {
                        "Transaction Hash": tx.tx_hash,
                        "Date & Time": tx.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                        "From Address": tx.from_address,
                        "To Address": tx.to_address,
                        "Transaction Type": tx.tx_type,
                        "Asset Contract Address": tx.asset_contract_address or "",
                        "Asset Symbol / Name": tx.asset_symbol or "",
                        "Token ID": tx.token_id or "",
                        "Value / Amount": str(tx.value),
                        "Gas Fee (ETH)": str(tx.gas_fee),
                    }
                )
