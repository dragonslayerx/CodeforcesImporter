class Submission:
    def __init__(self, id=None, contest_id=None, problem=None, verdict=None):
        self.id = id
        self.contest_id = contest_id
        self.problem = problem
        self.verdict = verdict

    def set_id(self, id):
        self.id = id;

    def set_contest_id(self, contest_id):
        self.contest_id = contest_id

    def set_problem(self, problem):
        self.problem = problem

    def set_verdict(self, verdict):
        self.verdict = verdict
