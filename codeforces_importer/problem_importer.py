import httprequest
from urlbuilder import Urlbuilder
from config import Codeforces
from config import PublicMethods
from exception import RequestFailureException


def fetch_problems_by_category(classifier):
    """Fetches problems from Codeforces API and perform category-wise count"""

    try:
        url = Urlbuilder(Codeforces.API_URL, PublicMethods.PROBLEM_SET)
        response = httprequest.send_get_request(url.get_url())
        if response is not None:
            json = response.json();
            if 'status' in json:
                if json['status'] == 'OK':
                    result = json['result']
                    problem_list = result['problems']
                    for problem in problem_list:
                        for tag in problem['tags']:
                            classifier.category_total_count[tag] += 1
                else:
                    raise RequestFailureException('Request Failed' + json['comment']);
            else:
                raise RequestFailureException('Request Failed: Invalid response');
    except RequestFailureException as ex:
        print ex.message
