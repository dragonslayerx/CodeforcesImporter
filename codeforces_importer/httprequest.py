import requests;
import sys


def send_get_request(url, args=None):
    """Sends get request to the specified url. Get request behavior can be customized using optional args.

    :param url: url for get request
    :param args: optional args to customize get requests. See 'requests' library for more help.
    """

    try:
        #response = requests.get(url, args);
        response = requests.get(url);
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

