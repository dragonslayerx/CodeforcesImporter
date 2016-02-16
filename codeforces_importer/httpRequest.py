import requests;

class HttpRequest:

    @staticmethod
    def sendGetRequest(url, args=None):
        return requests.get(url, args);
