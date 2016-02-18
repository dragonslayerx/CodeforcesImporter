#!/usr/bin/env python

import os
from jinja2 import Environment, FileSystemLoader
from config import Codeforces
#https://pythonadventures.wordpress.com/2014/02/25/jinja2-example-for-generating-a-local-file-using-a-template/

problem_tags = {}
problem_link = {}
problem_list = []
submission_link ={}
PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
                                   trim_blocks=False)


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def temp(problems, id , path):
        contest = problems.contest_id
        tags = problems.tags
        name = problems.name
        index = problems.index
        base = Codeforces.BASE_URL;

        base_problem = str(base) + "/contest/" + str(contest) + "/" + "problem/" + str(index)
        submission_base = str(base) + "/contest/" + str(contest) + "/submission/" + str(id)

        for s in tags:
            problem_tags.setdefault(s,[]).append(name)

        problem_link[name] = base_problem
        submission_link[name] = submission_base
        problem_list.append(s)



def create_index_html():
    #print problem_link["Greg's Workout"]
    fname = "output.html"
    context = {
        'names': problem_list,
        'links': problem_link,
        'category': problem_tags,
        'submission' : submission_link
    }
    #
    with open(fname, 'w') as f:
        html = render_template('index.html', context)
        f.write(html)


def main():
    create_index_html()

########################################

if __name__ == "__main__":
    main()