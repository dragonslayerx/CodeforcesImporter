
from config import Codeforces
from httpRequest import HttpRequest
from SubmissionImporter import SubmissionImport
from lxml import html
from sourceCodeExtractor import  SourceCodeExtractor

importer = SubmissionImport('m17');

submissions_list = importer.getSubmissions()

# for key in submissions_list:
#     print "{",
#     print key.contestId,
#     print key.problem.index,
#     print key.problem.name,
#     print key.verdict,
#     print key.id,
#     print "}"

code = SourceCodeExtractor.extractSourceCode(459, 7457076);

path = 'C:\Users\dragonslayer\Desktop\\1.txt'

print path

target = open(path, 'w')
target.truncate();
target.write(str(code));