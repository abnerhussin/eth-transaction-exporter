from web3 import Web3
from ..exceptions import ValidationError


def validate_ethereum_address(address: str) -> bool:
    """Validate Ethereum address format"""
    if not Web3.is_address(address):
        raise ValidationError(f"Invalid Ethereum address: {address}")
    return True


def validate_output_path(path: str) -> bool:
    """Validate output file path"""
    if not path.endswith(".csv"):
        raise ValidationError("Output file must be a CSV file")
    return True
