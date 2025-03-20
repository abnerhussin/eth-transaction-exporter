import pytest
import csv
import os
from datetime import datetime
from decimal import Decimal
from src.utils.csv_writer import CSVWriter
from src.models.transaction import Transaction


@pytest.fixture
def sample_transactions():
    return [
        Transaction(
            tx_hash="0x123",
            timestamp=datetime(2024, 1, 1, 12, 0),
            from_address="0xabc",
            to_address="0xdef",
            tx_type="external",
            value=Decimal("1.0"),
            gas_fee=Decimal("0.00042"),
            asset_symbol="ETH",
        )
    ]


def test_write_transactions(sample_transactions, tmp_path):
    output_file = tmp_path / "test_transactions.csv"
    CSVWriter.write_transactions(sample_transactions, str(output_file))

    assert os.path.exists(output_file)

    with open(output_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert len(rows) == 1
    assert rows[0]["Transaction Hash"] == "0x123"
    assert rows[0]["Asset Symbol / Name"] == "ETH"
