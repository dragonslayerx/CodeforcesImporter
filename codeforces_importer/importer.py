import os, sys
import file_io
import source_code_extractor
import problem_importer
from codeforces_importer.classifier.classifier import Classifier
from codeforces_importer.classifier import html_generator
from submission_list_importer import SubmissionImport
from cfi_ignore import CfiIgnore
from get_extension import get_extension

def import_codes(handle, dir_path='.\log\\', fetch_submission_flag=True, max_sub_lim=10000):
    """Calls modules to import user-submissions-list, extract source-code, adding problems to classifier and write to file.

    :param handle: user's handle whose submissions are to be imported
    :param dir_path: local directory path where submissions are saved
    :param max_sub_lim: max #overall_submissions to fetch from submission page
    """

    try:
        # fetch user's submissions-list using Codeforces API
        importer = SubmissionImport(handle, max_sub_lim)
        submissions_list = importer.get_submissions()

        print 'Fetching submission list: Success\n'

        # read cfiignore file in the dir_path directory and ignores pre-fetched submissions
        cfi_ignore = CfiIgnore(dir_path);

        if submissions_list is not None:

            # instance of classifier for storing problem_name, associated_tags information
            classifier = Classifier()

            # fetch problems from Codeforces API
            problem_list = problem_importer.fetch_problems_by_category()
            for problem in problem_list:
                for tag in problem['tags']:
                    classifier.add_problem_tag(problem, tag)

            # ensures directory creation
            ensure_dir_creation(dir_path)

            for submission in submissions_list:
                try:

                    # print submission_details
                    submission.log()

                    # get problem_details
                    problem_id, problem_name = get_problem_details(submission)

                    # file path for cloned file
                    file_name = get_file_name(problem_id, problem_name, submission.prog_lang)
                    absolute_path = os.path.join(dir_path, file_name)
                    relative_path = os.path.join('.//', file_name)

                    # adds problem to classifier
                    classifier.add(submission.problem, submission.id, relative_path)

                    # fetch_submission_flag = True if user desires to import submissions
                    if fetch_submission_flag:

                        # check if the submission is pre-fetched
                        if cfi_ignore.ignore(problem_id) is False and is_gym(problem_id) is False:

                            # extracts the source code at the submission id
                            code = source_code_extractor.extract_source_code(str(submission.contest_id), str(submission.id))

                            # writing submission to file
                            file_io.write_to_file(absolute_path, code)

                            # add problem to ignore-list so that it is not fetched next time
                            cfi_ignore.add(problem_id)

                            print 'Successfully written submission: ' + str(submission.id) + ' to ' + absolute_path

                        else:
                            print 'ignoring submission. cfiignore suggests it has been fetched earlier'

                # ignore any exception in parsing source_code
                except Exception as ex:
                    print ex.message

                print ''

            # construct date vs count
            date_vs_info = {}
            for submission in submissions_list:
                submission_date = submission.submission_time.strftime("%Y-%m-%d")
                submission_data = date_vs_info.get(submission_date, [submission.submission_time_components, 0])
                submission_data[1] += 1
                date_vs_info[submission_date] = submission_data


            try:
                # generates html file
                html_generator.generate_html(handle, classifier, dir_path, "classification")

                # generates html file for data visualization
                html_generator.generate_html(handle, classifier, dir_path, "visualization", date_vs_info.values())

                # writes cfi ignore
                cfi_ignore.write_ignore_list()

            except Exception as ex:
                print ex.message
                print 'Error generating html file'

    except Exception as ex:
        print 'Error: ' + ex.message
        print 'Unable to fetch your submissions at the moment.'

    else:
        print 'Import-Status: Successful.'


def ensure_dir_creation(directory):
    """Ensures directory creation before importing submissions"""

    if not os.path.exists(directory):
        try:
            os.mkdir(directory)
        except OSError as ex:
            print ex.strerror
            sys.exit(1)


def get_problem_details(submission):
    """Extracts problem identifier and name from submission and returns it"""

    # generates problem_id
    problem_id = str(submission.contest_id) + submission.problem.index
    # generates problem_name
    problem_name = resolve(submission.problem.name)
    return problem_id, problem_name


def get_file_name(problem_id, problem_name, prog_lang):
    """Generate desired file_name for problem and returns it"""

    # path of local file where submission has to be saved
    file_name = problem_id + '-' + problem_name + '.' + get_extension(prog_lang);
    return file_name


def resolve(problem_name):
    """Removes symbols from problem_name inappropriate for file-name"""

    problem_name = problem_name.replace('/', '').replace('\\', '').replace(' ', '_').replace(':', '').replace(':','')
    problem_name = problem_name.replace('?', '').replace('<', '').replace('>', '').replace('"', '').replace('*', '');
    return problem_name


def is_gym(problem_id):
    """Checks if the problem belongs to a gym contest. If True, gym problems are usually unclassified and sols aren't public

    Assumption: gym contest_id is typically 6 characters in length
    """

    return len(problem_id) >= 6
