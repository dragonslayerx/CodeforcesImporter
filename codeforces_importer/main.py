import requests
from urlBuilder import UrlBuilder
from config import CODEFORCES_API_URL
from config import UserRequestMethod
from config import PublicMethods
from httpRequest import HttpRequest

url = UrlBuilder(CODEFORCES_API_URL, PublicMethods.PROBLEM_SET);
url.addParam('tags', 'dp')

print url.getUrl()

response = HttpRequest.sendGetRequest(url.getUrl());

print response.text



