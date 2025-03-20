from datetime import datetime
from decimal import Decimal
from typing import List
from ..models.transaction import Transaction
from ..config import TX_TYPE_EXTERNAL, TX_TYPE_INTERNAL, TX_TYPE_ERC20, TX_TYPE_ERC721
from web3 import Web3


class TransactionProcessor:
    @staticmethod
    def process_external_tx(tx: dict) -> Transaction:
        return Transaction(
            tx_hash=tx["hash"],
            timestamp=datetime.fromtimestamp(int(tx["timeStamp"])),
            from_address=tx["from"],
            to_address=tx["to"],
            tx_type=TX_TYPE_EXTERNAL,
            value=Decimal(tx["value"]) / Decimal(10**18),  # Convert from Wei to ETH
            gas_fee=Decimal(int(tx["gasUsed"]) * int(tx["gasPrice"])) / Decimal(10**18),
            asset_symbol="ETH",
        )

    @staticmethod
    def process_internal_tx(tx: dict) -> Transaction:
        return Transaction(
            tx_hash=tx["hash"],
            timestamp=datetime.fromtimestamp(int(tx["timeStamp"])),
            from_address=tx["from"],
            to_address=tx["to"],
            tx_type=TX_TYPE_INTERNAL,
            value=Decimal(tx["value"]) / Decimal(10**18),
            gas_fee=Decimal(0),  # Internal transactions don't have separate gas fees
            asset_symbol="ETH",
        )

    @staticmethod
    def process_erc20_tx(tx: dict) -> Transaction:
        decimals = int(tx.get("tokenDecimal", 18))
        return Transaction(
            tx_hash=tx["hash"],
            timestamp=datetime.fromtimestamp(int(tx["timeStamp"])),
            from_address=tx["from"],
            to_address=tx["to"],
            tx_type=TX_TYPE_ERC20,
            value=Decimal(tx["value"]) / Decimal(10**decimals),
            gas_fee=Decimal(int(tx["gasUsed"]) * int(tx["gasPrice"])) / Decimal(10**18),
            asset_contract_address=tx["contractAddress"],
            asset_symbol=tx["tokenSymbol"],
        )
