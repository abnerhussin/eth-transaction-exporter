class EtherscanAPIError(Exception):
    """Raised when Etherscan API returns an error"""

    pass


class TransactionProcessingError(Exception):
    """Raised when processing transactions fails"""

    pass


class CSVWriteError(Exception):
    """Raised when writing to CSV fails"""

    pass


class ValidationError(Exception):
    """Raised when input validation fails"""

    pass
