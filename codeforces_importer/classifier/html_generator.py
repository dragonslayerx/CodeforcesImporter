import sys
import os
from jinja2 import Environment, FileSystemLoader
from CodeforcesImporter.codeforces_importer import urlgen

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False
)


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def generate_html(handle, classifier, dir_path):
    """Creates a html page for classified problems"""

    create_index_html(handle, classifier, dir_path)


def create_index_html(handle, classifier, dir_path):
    """Creates a html page for classified problems"""

    try:
        output_html = dir_path+"\classified-problems.html"

        # python variables to be mapped with html page
        # see jinja2 library documentation for more help
        context = {
            'names': classifier.problem_list,
            'links': classifier.problem_link,
            'category': classifier.problem_tags,
            'submission': classifier.submission_link,
            'local': classifier.local_path_link,
            'index': classifier.problem_index,
            'submission_count': len(classifier.problem_list),
            'handle': handle,
            'handle_link': urlgen.generate_profile_url(handle)
        }

        # writes the html file to classified-problems.html
        with open(output_html, 'w') as output:
            html = render_template('index.html', context)
            html = html.encode('utf-8')
            output.write(html)

    except UnicodeEncodeError as ex:
        print ex.message
    except (OSError, IOError) as ex:
        print ex.message
