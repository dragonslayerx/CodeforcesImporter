from codeforces_importer.urlBuilder import UrlBuilder
from config import Codeforces
from config import UserRequestMethod
from httpRequest import HttpRequest


class SubmissionImport:

    def __init__(self, handle):
        self.Submission = [];
        self.handle = handle;

    def generateUrl(self):
        url = UrlBuilder(Codeforces.API_URL);
        url.addParam(UserRequestMethod.SUBMISSION_METHOD, self.handle)
        url.addParam('from', '1')
        url.addParam('count', '1000');
        return url.getUrl()

    def importSubmissions(self):
        url = self.generateUrl()
        response = HttpRequest.sendGetRequest(url);
        return response.json()