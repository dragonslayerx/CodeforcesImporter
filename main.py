import sys
import CodeforcesImporter.codeforces_importer.importer

handle = None
dir_path = None

argv = sys.argv[1:]
if len(sys.argv) == 2:
    handle = argv[0]
    dir_path = argv[1]
else:
    handle = str(raw_input("Enter the handle of user: "))
    dir_path = str(raw_input("Enter the submissions' local dir_path: "))

if handle is not None and dir_path is not None:
    print 'Inporting submissions of ' + handle + 'at' + dir_path
    CodeforcesImporter.codeforces_importer.importer.import_codes(handle, dir_path)
else:
    print 'Invalid Args'
    sys.exit(1)
