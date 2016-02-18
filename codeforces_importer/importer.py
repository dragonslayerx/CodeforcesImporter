import file_io

import source_code_extractor
from CodeforcesImporter.classifier import html_generator
from CodeforcesImporter.classifier.classifier import Classifier
from Entity.Submission import log_submission
from submission_importer import SubmissionImport


def import_codes(handle, dir_path='.\log\\', max_sub_lim=10000):
    try:
        importer = SubmissionImport(handle, max_sub_lim)
        try:
            submissions_list = importer.get_submissions()
            if submissions_list is not None:
                classifier = Classifier()
                for submission in submissions_list:
                    try:
                        log_submission(submission)
                        code = source_code_extractor.extract_source_code(str(submission.contest_id), str(submission.id));

                        # generates problem_id
                        problem_id = str(submission.contest_id) + submission.problem.index

                        # generates problem_name
                        problem_name = submission.problem.name
                        problem_name = resolve(problem_name);

                        path = dir_path + '\\' + problem_id + '-' + problem_name + '.txt'

                        # adding problem to classifier
                        classifier.add_to_classifier(submission.problem, submission.id, path);

                        # writing submission to file
                        file_io.write_to_file(path, code);

                        print 'Successfully written submission: ' + str(submission.id) + ' to ' + path
                        print ''

                    except Exception as ex:
                        print ex.message

                html_generator.generate_html(handle, classifier, dir_path)

        except Exception as ex:
            raise ex

    except Exception as ex:
        print 'Error: ' + ex.message
        print 'Unable to fetch your submissions at the moment'

    else:
        print 'Import-Status: Successful'


def resolve(problem_name):
    problem_name = problem_name.replace('/', '').replace('\\', '').replace(' ', '_');
    return problem_name

