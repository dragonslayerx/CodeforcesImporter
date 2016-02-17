import sys
import file_io
import source_code_extractor

from submission_importer import SubmissionImport


def import_codes(handle, dir_path='.\log\\'):

    try:
        importer = SubmissionImport(handle)
        try:
            submissions_list = importer.get_submissions()

            if submissions_list is not None:
                for key in submissions_list:

                    print "[",
                    print 'id = ' + str(key.contest_id) + ',',
                    print 'name =' + key.problem.index + key.problem.name + ',',
                    print 'verdict = ' + key.verdict + ',',
                    print 'submission_id=' + str(key.id),
                    print "]"

                    code = source_code_extractor.extract_source_code(str(key.contest_id), str(key.id));

                    problem_name = key.problem.name

                    problem_name = resolve(problem_name);

                    path = dir_path + '\\' + problem_name + '.txt'

                    print 'Create ' + path

                    file_io.write_to_file(path, code);

        except TypeError as e:
            print e.message
            raise e
    except Exception as e:
        print e
        print 'Unable to fetch your submissions at the moment'
    else:
        print 'Import-Status: Successful'


def resolve(problem_name):
    problem_name = problem_name.replace('/', '').replace('\\', '').replace(' ', '_');
    return problem_name
