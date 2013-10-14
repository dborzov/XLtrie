# X-trie class implementation
#



INPUT_YEAR = 1977
order = 7

class Xtrie(object):
  def __init__(self,order):
    self.size = 2**order
    self.DAT =[False for x in range(self.size)] # direct access table
    self.heap =[False for x in range(2*self.size)] # direct access table

  def mark_year(self,year):
    index = year-1900
    self.DAT[index] = True
    self.heap[self.size + index] = True
    pointer = self.size + index
    for i in range(order):
        pointer = pointer /2
        self.heap[pointer] = True


  def self_report(self):
    for index, el in enumerate(self.DAT):
      if el:
	print str(1900+index)



mytrie = Xtrie(order)
years = [int(year_str) for year_str in open('years.txt','rb').readlines()]

for year in years:
  mytrie.mark_year(year)

mytrie.self_report()