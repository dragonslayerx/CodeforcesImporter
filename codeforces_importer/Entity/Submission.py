from codeforces_importer.Entity import Problem
import datetime

class Submission:
    """Represents a submission.

    In confirmation to Codeforces API submission object
    See http://codeforces.com/api/help/objects for more help.
    """

    def __init__(self, id=None, contest_id=None, problem=None, verdict=None, prog_lang='unclassified', submission_time=None, submission_time_components=None):
        self.id = id
        self.contest_id = contest_id
        self.problem = problem
        self.verdict = verdict
        self.prog_lang = prog_lang
        self.submission_time = submission_time
        self.submission_time_components = submission_time_components

    def __init__(self, submission_json):
        """Creates a submission instance by parsing submission_json"""

        if 'id' in submission_json:
            self.set_id(submission_json['id'])
        if 'contestId' in submission_json:
            self.set_contest_id(submission_json['contestId'])
        if 'problem' in submission_json:
            self.set_problem(Problem.Problem(submission_json['problem']));
        if 'verdict' in submission_json:
            self.set_verdict(submission_json['verdict'])
        if 'programmingLanguage' in submission_json:
            self.set_prog_lang(submission_json['programmingLanguage'])
        if 'creationTimeSeconds' in submission_json:
            self.set_submission_time(datetime.datetime.fromtimestamp(int(submission_json['creationTimeSeconds'])))
            self.set_submission_time_components(self.submission_time)


    def set_id(self, id):
        self.id = id;

    def set_contest_id(self, contest_id):
        self.contest_id = contest_id

    def set_problem(self, problem):
        self.problem = problem

    def set_verdict(self, verdict):
        self.verdict = verdict

    def set_prog_lang(self, prog_lang):
        self.prog_lang = prog_lang

    def set_submission_time(self, submission_time):
        self.submission_time = submission_time

    def set_submission_time_components(self, submission_time):
        self.submission_time_components = [submission_time.year, submission_time.month-1, submission_time.day]


    def log(self):
        """Prints submissions details."""

        print "[",
        print 'id = ' + str(self.contest_id) + self.problem.index + ', ',
        print 'name = ' + self.problem.name + ', ',
        print 'verdict = ' + self.verdict + ', ',
        print 'submission_id = ' + str(self.id),
        print 'submission_time = ' + str(self.submission_time),
        print "]"
