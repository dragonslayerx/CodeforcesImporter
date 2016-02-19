import file_io

import source_code_extractor
from CodeforcesImporter.classifier import html_generator
from CodeforcesImporter.classifier.classifier import Classifier
from Entity.Submission import log_submission
from submission_list_importer import SubmissionImport


def import_codes(handle, dir_path='.\log\\', max_sub_lim=10000):
    """Calls modules to import user-submissions-list, extract source-code, adding problems to classifier and write to file.

    Imports user's-submissions-list using Codeforces API.
    Extracts source-code using lxml library.
    Adds problems and associated tags to Classifier.
    Writes source-code to file.

    :param handle: user's handle whose submissions are to be imported
    :param dir_path: local directory path where submissions are saved
    :param max_sub_lim: max #overall_submissions to fetch from submission page
    """

    try:
        importer = SubmissionImport(handle, max_sub_lim)
        try:
            # fetch user's submissions-list using Codeforces API
            submissions_list = importer.get_submissions()

            if submissions_list is not None:
                # instance of classifier for storing problem_name, associated_tags information
                classifier = Classifier()

                for submission in submissions_list:
                    try:
                        # print details about the submission
                        log_submission(submission)

                        # extracts the source code at the submission id
                        code = source_code_extractor.extract_source_code(str(submission.contest_id), str(submission.id));

                        # generates problem_id
                        problem_id = str(submission.contest_id) + submission.problem.index

                        # generates problem_name
                        problem_name = submission.problem.name
                        problem_name = resolve(problem_name);

                        # path of local file where submission has to be saved
                        path = dir_path + '\\' + problem_id + '-' + problem_name + '.txt'

                        # adds problem to classifier
                        classifier.add_to_classifier(submission.problem, submission.id, path);

                        # writing submission to file
                        file_io.write_to_file(path, code);

                        print 'Successfully written submission: ' + str(submission.id) + ' to ' + path
                        print ''

                    except Exception as ex:
                        print ex.message

                # generates html file
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

