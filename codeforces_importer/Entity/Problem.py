class Problem:
    def __init__(self):
        self.contestId = None
        self.index = None
        self.name = None
        self.tags = None

    def __init__(self, prob_dict):
            self.contestId = prob_dict['contestId']
            self.index = prob_dict['index']
            self.name = prob_dict['name']
            self.tags = prob_dict['tags']

    def setContestId(self, contestId):
        self.contestId = contestId

    def setIndex(self, index):
        self.index = index

    def setNamem(self, name):
        self.name = name;

    def setTags(self, tags):
        self.tags = tags
