class Problem:
    def __init__(self):
        self.contestId = None
        self.index = None
        self.name = None
        self.tags = None

    def __init__(self, probdict):
        if type(probdict) is __dict__:
            self.contestId = probdict['id']
            self.index = probdict['index']
            self.name = probdict['name']
            self.tags = probdict['tags']


    # def __init__(self, contestId, index, name, tags):
    #     self.contestId = contestId
    #     self.index = index
    #     self.name = name
    #     self.tags = tags

    def setContestId(self, contestId):
        self.contestId = contestId

    def setIndex(self, index):
        self.index = index

    def setNamem(self, name):
        self.name = name;

    def setTags(self, tags):
        self.tags = tags
