import requests;


def send_get_request(url, args=None):
    return requests.get(url, args);
