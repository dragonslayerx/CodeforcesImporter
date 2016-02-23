import httprequest
import urlgen
from lxml import html


def extract_source_code(contest_id, submission_id):
    """Extracts source-code of submission at codeforces.com/contest/'contest_id'/submission/'submission_id'.

    Sends request to url mentioned above. Parses response text/html.
    See lxml library documentation for more help regarding html parsing.

    :param contest_id: contest id where the problem appeared
    :param submission_id: submission id to be fetched
    """

    # generates url for Codeforces submission page for submission#submissions_id
    submission_url = urlgen.generate_submission_url(contest_id, submission_id)

    print submission_url

    # makes a request to Codeforces API for users' submissions list
    response = httprequest.send_get_request(submission_url)

    # parses html at codeforces.com/contest/contest_id/submission/submission_id to extract source_code
    tree2 = html.fromstring(response.text)
    code = tree2.xpath('//*[@id="pageContent"]/div[3]/pre/text()')

    try:
        if len(code) > 0:
            # replaces all '\\r\\n' with '\r\n'
            return fix_eol(code[0])
        else:
            # received empty content. unable to extract submission using html parser
            raise ValueError('Empty Content')

    except ValueError as ex:
        print ex.message


def fix_eol(code):
    """Fix end of line in source code and returns it"""
    code = code.replace('\\r\\n', '\r\n')
    return code
