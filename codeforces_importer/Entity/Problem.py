class Problem:
    def __init__(self, contestId=None, index=None, name=None, tags=None):
        self.contestId = contestId
        self.index = index
        self.name = name
        self.tags = tags

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
