import pytest
from datetime import datetime
from decimal import Decimal
from src.services.transaction_processor import TransactionProcessor
from src.config import TX_TYPE_EXTERNAL, TX_TYPE_INTERNAL, TX_TYPE_ERC20


@pytest.fixture
def processor():
    return TransactionProcessor()


def test_process_external_tx(processor):
    tx = {
        "hash": "0x123",
        "timeStamp": "1234567890",
        "from": "0xabc",
        "to": "0xdef",
        "value": "1000000000000000000",
        "gasUsed": "21000",
        "gasPrice": "20000000000",
    }
    result = processor.process_external_tx(tx)
    assert result.tx_hash == "0x123"
    assert result.tx_type == TX_TYPE_EXTERNAL
    assert result.value == Decimal("1.0")  # 1 ETH
    assert result.gas_fee == Decimal("0.00042")  # 21000 * 20000000000 / 1e18


def test_process_internal_tx(processor):
    tx = {
        "hash": "0x123",
        "timeStamp": "1234567890",
        "from": "0xabc",
        "to": "0xdef",
        "value": "1000000000000000000",
    }
    result = processor.process_internal_tx(tx)
    assert result.tx_hash == "0x123"
    assert result.tx_type == TX_TYPE_INTERNAL
    assert result.value == Decimal("1.0")
    assert result.gas_fee == Decimal("0")


def test_process_erc20_tx(processor):
    tx = {
        "hash": "0x123",
        "timeStamp": "1234567890",
        "from": "0xabc",
        "to": "0xdef",
        "value": "1000000",
        "tokenDecimal": "6",
        "contractAddress": "0xtoken",
        "tokenSymbol": "USDT",
        "gasUsed": "21000",
        "gasPrice": "20000000000",
    }
    result = processor.process_erc20_tx(tx)
    assert result.tx_hash == "0x123"
    assert result.tx_type == TX_TYPE_ERC20
    assert result.value == Decimal("1.0")  # 1 USDT (6 decimals)
    assert result.asset_symbol == "USDT"
    assert result.asset_contract_address == "0xtoken"
