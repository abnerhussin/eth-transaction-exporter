import os
from dotenv import load_dotenv

load_dotenv()

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")
ETHERSCAN_API_URL = "https://api.etherscan.io/api"

# Rate limiting parameters
REQUEST_DELAY = 0.2  # 200ms delay between requests
MAX_RETRIES = 3

# Transaction types
TX_TYPE_EXTERNAL = "external"
TX_TYPE_INTERNAL = "internal"
TX_TYPE_ERC20 = "erc20"
TX_TYPE_ERC721 = "erc721"
TX_TYPE_ERC1155 = "erc1155"
