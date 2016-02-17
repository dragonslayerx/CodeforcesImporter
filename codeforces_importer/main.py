import os
import errno

import source_code_extractor
from submission_importer import SubmissionImport


importer = SubmissionImport('dragonslayerx')
submissions_list = importer.get_submissions()

flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY

for key in submissions_list:
    print "{",
    print key.contest_id,
    print key.problem.index,
    print key.problem.name,
    print key.verdict,
    print key.id,
    print "}"

    code = source_code_extractor.extract_source_code(str(key.contest_id), str(key.id));

    problemName = key.problem.name
    print problemName

    path = 'C:\Users\dragonslayer\Desktop\\log\\' + key.problem.name + '.txt'

    print path

    try:
        file_handle = os.open(path, flags)
    except OSError as e:
        if e.errno == errno.EEXIST:
            pass
        else:
            raise
    else:
        with os.fdopen(file_handle, 'w') as file_obj:
            file_obj.write(code)
