from collections import defaultdict
from codeforces_importer import urlgen


class Classifier:
    """Classifies the problem according to their tags.

    Keep relevant information like problem index, associated tags and links.
    Also keep submission-links and local-links mapped to problem-name.
    """

    def __init__(self):
        self.problem_list = set()
        
        self.problem_tags = defaultdict(set)
        self.problem_id = {}
        self.problem_link = {}
        self.submission_link ={}
        self.local_path_link ={}
        self.category_count = defaultdict(int)
        self.category_total_count = defaultdict(int)

    def add(self, problem, submission_id, relative_path):
        """Adds a problem and submission details to Classifier."""

        # Checks if the submission is a resubmission over existing problem
        if problem.name not in self.problem_id:

            problem_url = urlgen.generate_problem_url(problem.contest_id, problem.index)
            submission_url = urlgen.generate_submission_url(problem.contest_id, submission_id)

            self.problem_list.add(problem.name)

            # add to all the tags
            for tag in problem.tags:
                self.problem_tags[tag].add(problem.name)
                self.category_count[tag] += 1

            self.problem_id[problem.name] = str(problem.contest_id) + '-' + problem.index
            self.problem_link[problem.name] = problem_url
            self.submission_link[problem.name] = submission_url
            self.local_path_link[problem.name] = relative_path

    def add_problem_tag(self, problem, tag):
        """Adds problem to category and increment category count by 1"""

        self.category_total_count[tag] += 1;

    def get_sorted_category(self):
        sorted_category_list = []
        for category in self.problem_tags:
            sorted_category_list.append(category)
        sorted_category_list.sort()
        return sorted_category_list
