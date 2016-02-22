import codeforces_importer.importer
import sys


argc = len(sys.argv)
argv = sys.argv
if argc != 3:
    print 'Usage ' + argv[0] + " handle local_directory"
    handle = str(raw_input("Enter user's Codeforces handle: "))
    dir_path = str(raw_input("Enter local_directory_path for import: "))

else:
    argv = argv[1:]
    handle = argv[0]
    dir_path = argv[1]

if handle is not None and dir_path is not None:
    print 'Importing submissions of ' + handle + ' at ' + dir_path
    codeforces_importer.importer.import_codes(handle, dir_path)
    sys.exit(0)
else:
    print 'Invalid args'
    sys.exit(1)
