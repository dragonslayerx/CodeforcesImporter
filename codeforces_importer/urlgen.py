from config import Codeforces


def generate_submission_url(contest_id, submission_id):
    """generates url for user submissions eg 'codeforces.com/contest/123/submissions/123456' and returns it"""
    url = Codeforces.BASE_URL + "/contest/" + str(contest_id) + "/submission/" + str(submission_id);
    return url


def generate_problem_url(contest_id, index):
    """generates url for problem eg 'codeforces.com/contest/123/problem/A' and returns it"""
    url = Codeforces.BASE_URL + "/contest/" + str(contest_id) + "/problem/" + str(index);
    return url


def generate_profile_url(handle):
    """generates url for profile page eg 'codeforces.com/profile/abcdef' and returns it"""
    url = Codeforces.BASE_URL + "/profile/" + handle;
    return url
