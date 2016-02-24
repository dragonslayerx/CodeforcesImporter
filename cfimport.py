import codeforces_importer.importer
import sys
import getopt

argc = len(sys.argv)
argv = sys.argv

handle = None
dir_path = None
fetch_submission_flag = True;

if argc < 3:
    print "Usage python cfimport.py [-i, --ignore] {handle} {directory_path}"
    handle = str(raw_input("Enter user's Codeforces handle: "))
    dir_path = str(raw_input("Enter local_directory_path for import: "))
    fetch_submission_flag = str(raw_input("Do you want to import submission program-source (y/n) : ")) == 'y'
else:
    try:
        opt_list, arg = getopt.getopt(sys.argv[1:], 'i', ['ignore'])
    except getopt.GetoptError as ex:
        print(ex);
        print "Usage python cfimport.py [-i, --ignore] {handle} {directory_path}"
        sys.exit(1);
    else:
        for option, val in opt_list:
            if option == '-i' or option == '--ignore':
                fetch_submission_flag = False
        handle = arg[0]
        dir_path = arg[1]

if handle is not None and dir_path is not None:
    print 'Importing submissions of ' + handle + ' at ' + dir_path
    codeforces_importer.importer.import_codes(handle, dir_path, fetch_submission_flag)
    sys.exit(0)
else:
    print 'Invalid args'
    sys.exit(1)
