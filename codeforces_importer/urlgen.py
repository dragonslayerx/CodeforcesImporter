from config import Codeforces


def generate_submission_url(contest_id, submission_id):
    url = Codeforces.BASE_URL + "/contest/" + str(contest_id) + "/submission/" + str(submission_id);
    return url


def generate_problem_url(contest_id, index):
    url = Codeforces.BASE_URL + "/contest/" + str(contest_id) + "/problem/" + str(index);
    return url


def generate_profile_url(handle):
    url = Codeforces.BASE_URL + "/profile/" + handle;
    return url
