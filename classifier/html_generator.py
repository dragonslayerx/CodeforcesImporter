import os
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False
)


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def create_index_html(classifier, dir_path):
    try:
        output_html = dir_path+"\output.html"

        context = {
            'names': classifier.problem_list,
            'links': classifier.problem_link,
            'category': classifier.problem_tags,
            'submission': classifier.submission_link,
            'local': classifier.local_path_link
        }

        with open(output_html, 'w') as output:
            html = render_template('index.html', context)
            html = html.encode('utf-8')
            output.write(html)

    except UnicodeEncodeError as ex:
        print ex


def generate_html(classifier, dir_path):
    create_index_html(classifier, dir_path)
