from codeforces_importer.Entity.Problem import Problem
from codeforces_importer.urlBuilder import UrlBuilder
from config import Codeforces
from config import UserRequestMethod
from httpRequest import HttpRequest
from Entity.Submission import Submission

class SubmissionImport:

    def __init__(self, handle):
        self.submissions = [];
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

    def getSubmissions(self):
        response = self.importSubmissions();

        if type(response) is __dict__:
            for subdict in response:

                submission = Submission();
                if 'id' in subdict:
                   submission.setId(subdict['id'])
                if 'contestId' in subdict:
                    submission.setContestId(subdict['contestId'])
                if 'problem' in subdict:
                    submission.setProblem(Problem(subdict['problem']));
                if 'verdict' in subdict:
                    submission.setVerdict(subdict['verdict'])

                self.submissions.append(submission);

