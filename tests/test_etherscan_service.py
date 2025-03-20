import pytest
from unittest.mock import patch, MagicMock
from src.services.etherscan_service import EtherscanService
from src.config import ETHERSCAN_API_KEY
import requests


@pytest.fixture
def etherscan_service():
    return EtherscanService()


@pytest.fixture
def mock_response():
    mock = MagicMock()
    mock.json.return_value = {
        "status": "1",
        "result": [
            {
                "hash": "0x123",
                "from": "0xabc",
                "to": "0xdef",
                "value": "1000000000000000000",
                "timeStamp": "1234567890",
                "gasUsed": "21000",
                "gasPrice": "20000000000",
            }
        ],
    }
    return mock


def test_get_external_transactions(etherscan_service, mock_response):
    with patch("requests.get", return_value=mock_response):
        transactions = etherscan_service.get_external_transactions("0x123")
        assert len(transactions) == 1
        assert transactions[0]["hash"] == "0x123"
        assert transactions[0]["from"] == "0xabc"


def test_get_internal_transactions(etherscan_service, mock_response):
    with patch("requests.get", return_value=mock_response):
        transactions = etherscan_service.get_internal_transactions("0x123")
        assert len(transactions) == 1
        assert transactions[0]["hash"] == "0x123"


def test_get_erc20_transfers(etherscan_service, mock_response):
    with patch("requests.get", return_value=mock_response):
        transactions = etherscan_service.get_erc20_transfers("0x123")
        assert len(transactions) == 1
        assert transactions[0]["hash"] == "0x123"


def test_make_request_retry(etherscan_service):
    mock_response = MagicMock()
    mock_response.json.return_value = {"result": []}

    with patch(
        "requests.get",
        side_effect=[
            requests.exceptions.RequestException("Network error"),
            mock_response,  # Second call succeeds
        ],
    ):
        result = etherscan_service._make_request({"module": "test"})
        assert result == {"result": []}
