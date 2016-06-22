import requests
import sys
from codeforces_importer.exception import RequestFailureException


def send_get_request(url):
    """Sends get request to the specified url. Get request behavior can be customized using optional args.

    :param url: url for get request
    """

    try:
        response = requests.get(url)
        return response
    except requests.exceptions.Timeout:
        raise RequestFailureException('Connection Timed Out')
    except requests.exceptions.TooManyRedirects:
        raise RequestFailureException('Too Many Redirects')
    except requests.exceptions.RequestException:
        raise RequestFailureException('Unable To connect')

