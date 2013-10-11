import re


source = open('movies.txt','rb').readlines()
out = open('result.txt','wb')
yearsonly = open('years.txt','wb')

cleared = []
for each in source:
  match = re.search('(^[\W\w\s,]+) \((\d\d\d\d)\)',each)
  if match:
    hasX = re.search('X',match.group(1))
    if hasX:
      out.write(match.group(1)+'\n')
      yearsonly.write(match.group(2)+'\n')
       
