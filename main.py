import sys
import codeforces_importer.importer
import sys
import os
def ensure_dir(directory):
    d = os.path.dirname(directory)
    print d
    if not os.path.exists(directory):
        os.mkdir(directory)

argc = len(sys.argv)
argv = sys.argv
if argc != 3:
    print 'Usage ' + argv[0] + " handle local_directory"
    handle = str(raw_input("Enter user's Codeforces handle: "))
    dir_path = str(raw_input("Enter local_directory_path for import: "))

else :
    argv = argv[1:]
    handle = argv[0]
    dir_path = argv[1]

if handle is not None and dir_path is not None:
    print 'Importing submissions of ' + handle + ' at ' + dir_path
    ensure_dir(dir_path)
    codeforces_importer.importer.import_codes(handle, dir_path)
else:
    print 'Invalid args'
sys.exit(1)
