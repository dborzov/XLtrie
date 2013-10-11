INPUT_YEAR = 1977
m = 128

class Xtrie(object):
  def __init__(self,m):
    self.DAT =[False for x in range(m)] # direct access table]
    
    
  def mark_year(self,year):
    self.DAT[year-1900] = True
    
  def self_report(self):
    for index, el in enumerate(self.DAT):
      if el:
	print str(1900+index)



mytrie = Xtrie(m)
years = [int(year_str) for year_str in open('years.txt','rb').readlines()]

for year in years:
  mytrie.mark_year(year)
  
mytrie.self_report()