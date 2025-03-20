import time
from typing import List, Dict
import requests
from ..config import ETHERSCAN_API_KEY, ETHERSCAN_API_URL, REQUEST_DELAY, MAX_RETRIES


class EtherscanService:
    def __init__(self):
        self.api_key = ETHERSCAN_API_KEY
        self.base_url = ETHERSCAN_API_URL

    def _make_request(self, params: Dict) -> Dict:
        """Make API request with retry logic and rate limiting"""
        for attempt in range(MAX_RETRIES):
            try:
                response = requests.get(
                    self.base_url, params={**params, "apikey": self.api_key}
                )
                response.raise_for_status()
                time.sleep(REQUEST_DELAY)  # Rate limiting
                return response.json()
            except requests.exceptions.RequestException as e:
                if attempt == MAX_RETRIES - 1:
                    raise Exception(
                        f"Failed to fetch data after {MAX_RETRIES} attempts: {str(e)}"
                    )
                time.sleep(1 * (attempt + 1))  # Exponential backoff
        return {}

    def get_external_transactions(self, address: str) -> List[Dict]:
        params = {
            "module": "account",
            "action": "txlist",
            "address": address,
            "startblock": "0",
            "endblock": "99999999",
            "sort": "asc",
        }
        return self._make_request(params)["result"]

    def get_internal_transactions(self, address: str) -> List[Dict]:
        params = {
            "module": "account",
            "action": "txlistinternal",
            "address": address,
            "startblock": "0",
            "endblock": "99999999",
            "sort": "asc",
        }
        return self._make_request(params)["result"]

    def get_erc20_transfers(self, address: str) -> List[Dict]:
        params = {
            "module": "account",
            "action": "tokentx",
            "address": address,
            "startblock": "0",
            "endblock": "99999999",
            "sort": "asc",
        }
        return self._make_request(params)["result"]

    def get_erc721_transfers(self, address: str) -> List[Dict]:
        params = {
            "module": "account",
            "action": "tokennfttx",
            "address": address,
            "startblock": "0",
            "endblock": "99999999",
            "sort": "asc",
        }
        return self._make_request(params)["result"]
