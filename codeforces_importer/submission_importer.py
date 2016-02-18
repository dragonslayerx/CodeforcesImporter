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
        :return:
        """

        self.submissions = []
        self.handle = handle
        self.max_sub_lim = max_sub_lim

    def generate_url(self):
        """generates url Codeforces.API_URL/user.status with appropriate args and returns the url"""
        url = Urlbuilder(Codeforces.API_URL, UserRequestMethod.SUBMISSION_METHOD);
        url.add_param('handle', self.handle)
        url.add_param('from', '1')
        url.add_param('count', str(self.max_sub_lim))
        return url.get_url()

    def import_submissions(self):
        """sends request at Codeforces.API_URL/user.status to fetch submission list and returns the list"""
        url = self.generate_url()
        response = httprequest.send_get_request(url);

        if 'status' in response.json():
            # status == OK, if request succeeds
            if response.json()['status'] == 'OK':
                print 'Connection Status: Successful'
            else:
                # prints why request failed
                print response.json()['comment']
                print 'Connection Refused'
            return response.json()
        else:
            print 'Connection Refused'

    def get_submissions(self):
        response = self.import_submissions()

        if 'status' in response:
            if response['status'] == 'OK':
                # parsing json response.result for submission information
                for submission_dict in response['result']:
                        submission = Submission()
                        if 'id' in submission_dict:
                            submission.set_id(submission_dict['id'])
                        if 'contestId' in submission_dict:
                            submission.set_contest_id(submission_dict['contestId'])
                        if 'problem' in submission_dict:
                            submission.set_problem(Problem(submission_dict['problem']));
                        if 'verdict' in submission_dict:
                            submission.set_verdict(submission_dict['verdict'])

                        # add only 'Accepted' submissions
                        if submission.verdict == 'OK':
                            self.submissions.append(submission)
                return self.submissions

        elif 'comment' in response:
            # prints why request failed
            print response['comment']
            sys.exit(1)
        else:
            print 'Unable to Connect'

