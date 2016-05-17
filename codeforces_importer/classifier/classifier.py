from collections import defaultdict
from codeforces_importer import urlgen


class Classifier:
    """Classifies the problem according to their tags.

    Keep relevant information like problem index, associated tags and links.
    Also keep submission-links and local-links mapped to problem-name.
    """

    """Submission-wise categorization"""

    def __init__(self):

        self.problems = set()
        self.submissions = set()

    def add_submission(self, submission, relative_path):
        """Adds submission details to Classifier."""

        problem = submission.problem
        submission_url = urlgen.generate_submission_url(problem.contest_id, submission.id)

        if submission not in self.submissions:
            self.submissions.add((submission, submission_url, relative_path))

    """extracts submission details from self.submissions"""

    def get_submission_url(self):
        submission_url = defaultdict()
        for submission_details in self.submissions:
            submission = submission_details[0]
            url = submission_details[1]
            submission_url[submission.problem.name] = url
        return submission_url

    def get_local_link(self):
        local_link = defaultdict()
        for submission_details in self.submissions:
            submission = submission_details[0]
            link = submission_details[2]
            local_link[submission.problem.name] = link
        return local_link

    def get_submission_tag_count(self):
        tag_count = defaultdict(int)
        for submission_details in self.submissions:
            submission = submission_details[0]
            problem = submission.problem
            # add to all the tags
            for tag in problem.tags:
                tag_count[tag] += 1
        return tag_count

    """Problem-wise categorization"""

    def add_problem(self, problem):
        """Adds problem to category."""

        problem_url = urlgen.generate_problem_url(problem.contest_id, problem.index)
        self.problems.add((problem, problem_url))

    """extracts problem details from self.problems"""

    def get_problem_list(self):
        problem_list = set()
        for problem_details in self.problems:
            problem = problem_details[0]
            problem_list.add(problem.name)
        return problem_list

    def get_problem_id(self):
        problem_id = defaultdict()
        for problem_details in self.problems:
            problem = problem_details[0]
            problem_id[problem.name] = str(problem.contest_id) + '-' + problem.index
        return problem_id

    def get_problem_url(self):
        problem_url = defaultdict()
        for problem_details in self.problems:
            problem = problem_details[0]
            problem_url[problem.name] = problem_details[1]
        return problem_url

    def get_tagged_problems(self):
        problem_tags = defaultdict(set)
        for submission_details in self.submissions:
            submission = submission_details[0]
            problem = submission.problem
            # add to all the tags
            for tag in problem.tags:
                problem_tags[tag].add(problem.name)
        return problem_tags

    def get_category_count(self):
        category_count = defaultdict(int)
        for problem_details in self.problems:
            problem = problem_details[0]
            for tag in problem.tags:
                category_count[tag] += 1
        return category_count

    def get_sorted_category(self):
        sorted_category_list = []
        for category in self.get_category_count():
            sorted_category_list.append(category)
        sorted_category_list.sort()
        return sorted_category_list
