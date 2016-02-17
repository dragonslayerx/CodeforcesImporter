import requests;
import sys


def send_get_request(url, args=None):
    try:
        response = requests.get(url, args);
        return response
    except requests.exceptions.Timeout:
        print 'Connection Timed Out'
        sys.exit(1)
    except requests.exceptions.TooManyRedirects:
        print 'Too Many redirects'
        sys.exit(1)
    except requests.exceptions.RequestException:
        print 'Unable to connect'
        sys.exit(1)

