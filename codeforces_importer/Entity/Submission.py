class Submission:
    def __init__(self, id = None, contestId = None, problem = None, verdict = None):
        self.id = id
        self.contestId = contestId
        self.problem = problem
        self.verdict = verdict

    def setId(self, id):
        self.id = id;

    def setContestId(self, contestId):
        self.contestId = contestId

    def setProblem(self, problem):
        self.problem = problem

    def setVerdict(self, verdict):
        self.verdict = verdict
