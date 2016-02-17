from config import Codeforces
import httprequest
from lxml import html


def generate_submission_url(contest_id, submission_id):
    url = Codeforces.BASE_URL + "/contest/" + str(contest_id) + "/submission/" + str(submission_id);
    return url


def extract_source_code(contest_id, submission_id):
    submission_url = generate_submission_url(contest_id, submission_id)

    print submission_url

    response = httprequest.send_get_request(submission_url)

    tree2 = html.fromstring(response.text)
    code = tree2.xpath('//*[@id="pageContent"]/div[3]/pre/text()')

    return fix_eol(str(code));


def fix_eol(code):
    print code
    size = len(code);
    fixed_code = ''
    i = 0
    while i < size:
        if i+1 < size:
            if code[i] == '\\' and code[i+1] == 'r':
                fixed_code += '\r'
                i += 1
            elif code[i]== '\\' and code[i+1] == 'n':
                fixed_code += '\n'
                i += 1
            else:
                fixed_code += code[i]
        else:
            fixed_code += code[i]
        i += 1

    return fixed_code