from collections import defaultdict
from codeforces_importer import urlgen


class Classifier:
    """Classifies the problem according to their tags.

    Keep relevant information like problem index, associated tags and links.
    Also keep submission-links and local-links mapped to problem-name.
    """

    def __init__(self):
        self.problem_list = []
        
        self.problem_tags = defaultdict(set)
        self.problem_id = {}
        self.problem_link = {}
        self.submission_link ={}
        self.local_link ={}
        self.category_count = defaultdict(int)

    def add(self, problem, submission_id, relative_path):
        """Adds a problem and submission details to Classifier."""

        problem_url = urlgen.generate_problem_url(problem.contest_id, problem.index)
        submission_url = urlgen.generate_submission_url(problem.contest_id, submission_id)

        self.problem_list.append(problem.name)

        # add to all the tags
        for tag in problem.tags:
            self.problem_tags[tag].add(problem.name)
            self.category_count[tag] += 1

        self.problem_id[problem.name] = str(problem.contest_id) + '-' + problem.index
        self.problem_link[problem.name] = problem_url
        self.submission_link[problem.name] = submission_url
        self.local_link[problem.name] = relative_path
