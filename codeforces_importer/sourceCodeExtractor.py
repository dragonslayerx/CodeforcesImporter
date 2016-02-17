from config import Codeforces
from httpRequest import HttpRequest
from lxml import html


class SourceCodeExtractor:

    @staticmethod
    def generateSubmissionUrl(contestId, submissionid):
        url = Codeforces.BASE_URL + "/contest/" + str(contestId) + "/submission/" + str(submissionid);
        return url


    @staticmethod
    def extractSourceCode(contestId, submissionid):
        submissionUrl = SourceCodeExtractor.generateSubmissionUrl(contestId, submissionid)
        response = HttpRequest.sendGetRequest(submissionUrl)

        tree2 = html.fromstring(response.text)
        code = tree2.xpath('//*[@id="pageContent"]/div[3]/pre/text()')
        return str(code);

