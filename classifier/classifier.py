from CodeforcesImporter.codeforces_importer import urlgen


class Classifier:

    def __init__(self):
        self.problem_tags = {}
        self.problem_link = {}
        self.problem_list = []
        self.submission_link ={}
        self.local_path_link ={}

    def add_to_classifier(self, problem, submission_id, local_path):
        print 'adding problem to classifier'

        problem_url = urlgen.generate_problem_url(problem.contest_id, problem.index)
        print problem_url

        submission_url = urlgen.generate_submission_url(problem.contest_id, submission_id)
        print submission_url

        for tag in problem.tags:
            self.problem_tags.setdefault(tag, []).append(problem.name)

        self.problem_link[problem.name] = problem_url
        self.submission_link[problem.name] = submission_url
        self.problem_list.append(problem.name)
        self.local_path_link[problem.name] = local_path

