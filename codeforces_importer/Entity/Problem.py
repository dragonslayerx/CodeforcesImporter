class Problem:
    def __init__(self, contest_id=None, index=None, name=None, tags=None):
        self.contest_id = contest_id
        self.index = index
        self.name = name
        self.tags = tags

    def __init__(self, prob_dict):
            self.contest_id = prob_dict['contestId']
            self.index = prob_dict['index']
            self.name = prob_dict['name']
            self.tags = prob_dict['tags']

    def set_contest_id(self, contestId):
        self.contest_id = contestId

    def set_index(self, index):
        self.index = index

    def set_name(self, name):
        self.name = name;

    def set_tags(self, tags):
        self.tags = tags
