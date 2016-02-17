import requests
from urlBuilder import UrlBuilder
from config import Codeforces
from config import PublicMethods
from httpRequest import HttpRequest

# # url = UrlBuilder(Codeforces.API_URL, PublicMethods.PROBLEM_SET);
# # url.addParam('tags', 'dp')
#
# print url.getUrl()

from SubmissionImporter import SubmissionImport
importer = SubmissionImport('dragonslayerx');

submissions_list = importer.getSubmissions()

for key in submissions_list:
    print "{",
    print key.contestId,
    print key.problem.index,
    print key.problem.name,
    print key.verdict,
    print key.id,
    print "}"



