import requests;
import sys


def send_get_request(url):
    """Sends get request to the specified url. Get request behavior can be customized using optional args.

    :param url: url for get request
    """

    try:
        response = requests.get(url)
        return response
    except requests.exceptions.Timeout:
        print 'Connection Timed Out'
        sys.exit(1)
    except requests.exceptions.TooManyRedirects:
        print 'Too Many redirects'
        sys.exit(1)
    except requests.exceptions.RequestException:
        print 'Unable to connect.'
        sys.exit(1)

