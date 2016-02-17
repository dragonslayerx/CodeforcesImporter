class Submission:
    def __init__(self):
        self.id = None
        self.contestId = None
        self.problem = None
        self.verdict  = None

    def __init__(self, id, contestId, problem, verdict):
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
