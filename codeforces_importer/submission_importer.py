from codeforces_importer.Entity.Problem import Problem
from codeforces_importer.urlbuilder import Urlbuilder
from config import Codeforces
from config import UserRequestMethod
from Entity.Submission import Submission
import httprequest


class SubmissionImport:

    def __init__(self, handle):
        self.submissions = [];
        self.handle = handle;

    def generate_url(self):
        url = Urlbuilder(Codeforces.API_URL, UserRequestMethod.SUBMISSION_METHOD);
        url.add_param('handle', self.handle)
        url.add_param('from', '1')
        url.add_param('count', '1000');
        return url.get_url()

    def import_submissions(self):
        url = self.generate_url()
        print url
        response = httprequest.send_get_request(url);
        return response.json()

    def get_submissions(self):
        response = self.import_submissions();

        for submission_dict in response['result']:

                submission = Submission();
                if 'id' in submission_dict:
                   submission.set_id(submission_dict['id'])
                if 'contestId' in submission_dict:
                    submission.set_contest_id(submission_dict['contestId'])
                if 'problem' in submission_dict:
                    submission.set_problem(Problem(submission_dict['problem']));
                if 'verdict' in submission_dict:
                    submission.set_verdict(submission_dict['verdict'])

                if submission.verdict == 'OK':
                    self.submissions.append(submission);

        return self.submissions
