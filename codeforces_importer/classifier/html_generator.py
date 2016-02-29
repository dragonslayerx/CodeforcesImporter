import os
from jinja2 import Environment, FileSystemLoader
from codeforces_importer import urlgen
import shutil as File

WRITE_FLAGS = os.O_CREAT | os.O_WRONLY

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False
)


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def generate_html(handle, classifier, dir_path, output_type, submission_data=None):
    """Creates a html page for classified problems"""
    try:
        output_type_vs_output_file = {
            "classification": "classified-problems.html",
            "visualization": "visualization.html"
        }
        output_type_vs_template_file = {
            "classification": "index.html",
            "visualization": "submissions_visualization.html"
        }
        output_html = os.path.join(dir_path, output_type_vs_output_file[output_type])
        file_handle = os.open(output_html, WRITE_FLAGS)

        # python variables to be mapped with html page
        # see jinja2 library documentation for more help
        context = {
            'names': classifier.problem_list,
            'links': classifier.problem_link,
            'sorted_category': classifier.get_sorted_category(),
            'category': classifier.problem_tags,
            'submission': classifier.submission_link,
            'local': classifier.local_path_link,
            'index': classifier.problem_id,
            'submission_count': len(classifier.problem_list),
            'handle': handle,
            'handle_link': urlgen.generate_profile_url(handle),
            'category_counter': classifier.category_count,
            'category_total_counter': classifier.category_total_count,
            'submission_data': submission_data
        }

        # writes the html file to classified-problems.html
        with os.fdopen(file_handle, 'w') as output:
            html = render_template(output_type_vs_template_file[output_type], context)
            html = html.encode('utf-8')
            output.write(html)

        # copy .css file to output directory
        File.copy('codeforces_importer/classifier/templates/style.css', dir_path)

    except UnicodeEncodeError as ex:
        print ex.message
    except (OSError, IOError) as ex:
        print ex.strerror

