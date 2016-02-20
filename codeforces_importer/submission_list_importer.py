import sys
from Entity.Problem import Problem
from urlbuilder import Urlbuilder
from config import Codeforces
from config import UserRequestMethod
from Entity.Submission import Submission
import httprequest


class SubmissionImport:

    def __init__(self, handle, max_sub_lim):
        """Sends request to Codeforces API. Parses response json object for status, comments and result.

        If status equals 'OK', add all submissions to self.submissions. Otherwise prints comment in response json.

        :param handle: user's handle whose submissions are to be imported
        :param max_sub_lim: max #overall_submissions to fetch from submission page
        """

        self.submissions = []
        self.handle = handle
        self.max_sub_lim = max_sub_lim

    def generate_url(self):
        """Generates url Codeforces.API_URL/user.status with appropriate args and returns the url"""

        url = Urlbuilder(Codeforces.API_URL, UserRequestMethod.SUBMISSION_METHOD);
        url.add_param('handle', self.handle)
        url.add_param('from', '1')
        url.add_param('count', str(self.max_sub_lim))
        return url.get_url()

    def import_submissions(self):
        """Sends request at Codeforces.API_URL/user.status to fetch submission list and returns the response json """

        url = self.generate_url()
        response = httprequest.send_get_request(url);

        if 'status' in response.json():
            # status == OK, if request succeeds
            if response.json()['status'] == 'OK':
                print 'Connection Status: Successful'
                return response.json()
            else:
                raise RequestFailureException('Request Failed');
        else:
            raise RequestFailureException('Request Failed');

    @staticmethod
    def parse(submission_json):
        """Parses submission_json and returns a Submission instance.

        :param submission_json: json to be parsed
        :return: Submission
        """

        submission = Submission()
        if 'id' in submission_json:
            submission.set_id(submission_json['id'])
        if 'contestId' in submission_json:
            submission.set_contest_id(submission_json['contestId'])
        if 'problem' in submission_json:
            submission.set_problem(Problem(submission_json['problem']));
        if 'verdict' in submission_json:
            submission.set_verdict(submission_json['verdict'])
        return submission

    def get_submissions(self):
        """Import user's submission-list using Codeforces API."""

        try:
            response = self.import_submissions()
        except RequestFailureException as ex:
            if 'comment' in response:
                # prints why request failed
                print response['comment']
            else:
                # request failed due to unknown reason
                print ex.message
            sys.exit(1)
        else:
            # parsing json response.result for submission information
            for submission_dict in response['result']:
                submission = SubmissionImport.parse(submission_dict);
                # add only 'Accepted' submissions
                if submission.verdict == 'OK':
                    self.submissions.append(submission)
            return self.submissions


class RequestFailureException:
    """Exception to be raised when request to Codeforces API fails."""

    def __init__(self, message):
        self.message = message
