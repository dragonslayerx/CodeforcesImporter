import sys
import codeforces_importer.importer

handle = str(raw_input("Enter the handle of user: "))
dir_path = str(raw_input("Enter the submissions' local dir_path: "))

if handle is not None and dir_path is not None:
    print 'Importing submissions of ' + handle + ' at ' + dir_path
    codeforces_importer.importer.import_codes(handle, dir_path)
else:
    print 'Invalid args'
    sys.exit(1)
