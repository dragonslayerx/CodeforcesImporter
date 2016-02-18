import httprequest
import urlgen
from lxml import html


def extract_source_code(contest_id, submission_id):
    submission_url = urlgen.generate_submission_url(contest_id, submission_id)

    print submission_url

    response = httprequest.send_get_request(submission_url)

    tree2 = html.fromstring(response.text)
    code = tree2.xpath('//*[@id="pageContent"]/div[3]/pre/text()')

    try:
        if len(code) > 0:
            return fix_eol(str(code[0]));
        else:
            raise ValueError('Empty Content')
    except ValueError as e:
        print e.message


def fix_eol(code):
    code = code.replace('\\r\\n', '\r\n')
    return code
