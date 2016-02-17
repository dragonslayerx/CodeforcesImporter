import requests
from urlBuilder import UrlBuilder
from config import Codeforces
from config import PublicMethods
from httpRequest import HttpRequest

# # url = UrlBuilder(Codeforces.API_URL, PublicMethods.PROBLEM_SET);
# # url.addParam('tags', 'dp')
#
# print url.getUrl()

response = HttpRequest.sendGetRequest(url.getUrl());



