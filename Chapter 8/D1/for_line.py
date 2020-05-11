filepath = 'kjv.txt'
with open(filepath) as fp:
   for cnt, line in enumerate(fp):
       print("Line {}: {}".format(cnt, line))