class RequestFailureException(Exception):
    """Exception to be raised when request to Codeforces API fails."""

    def __init__(self, message):
        self.message = message
