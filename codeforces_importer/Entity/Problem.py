class Problem:
    """Represents a problem.

    In confirmation to Codeforces API problem object
    See http://codeforces.com/api/help/objects for more help.
    """

    def __init__(self, contest_id=None, index=None, name=None, tags=None):
        self.contest_id = contest_id
        self.index = index
        self.name = name
        self.tags = tags

    def __init__(self, prob_json):
        """Creates a problem instance by parsing prob_json"""

        if 'contestId' in prob_json:
            self.contest_id = prob_json['contestId']
        if 'index' in prob_json:
            self.index = prob_json['index']
        if 'name' in prob_json:
            self.name = prob_json['name']
        if 'tags' in prob_json:
            self.tags = prob_json['tags']

    def set_contest_id(self, contestId):
        self.contest_id = contestId

    def set_index(self, index):
        self.index = index

    def set_name(self, name):
        self.name = name;

    def set_tags(self, tags):
        self.tags = tags

    def log(self):
        """Prints problem details."""

        print "[",
        print 'id = ' + str(self.contest_id) + self.problem.index + ', ',
        print 'name = ' + self.name + ', ',
        print 'verdict = ' + self.tags + ', ',
        print "]"
