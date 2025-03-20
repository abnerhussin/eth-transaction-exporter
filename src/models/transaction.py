from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional


@dataclass
class Transaction:
    tx_hash: str
    timestamp: datetime
    from_address: str
    to_address: str
    tx_type: str
    value: Decimal
    gas_fee: Decimal
    asset_contract_address: Optional[str] = None
    asset_symbol: Optional[str] = None
    token_id: Optional[str] = None
