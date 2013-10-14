# X-trie implementation

import numpy as np


yescolor, nocolor = 0.86, 0.39

class Xtrie(object):
  def __init__(self,order):
    self.order = order
    self.size = 2**order
    self.DAT =[False for x in range(self.size)] # direct access table
    self.heap =[False for x in range(2*self.size -1)] # direct access table

  def mark(self,index):
    self.DAT[index] = True
    self.heap[self.size -1 + index] = True
    pointer = self.size -1 + index
    for i in range(self.order):
        pointer = (pointer - 1)/2
        self.heap[pointer] = True


  def self_report(self):
    for index, el in enumerate(self.DAT):
      if el:
	print str(index)

  def visualize(self):
    output = []
    pointer = 0
    for j in range(self.order+1):
        scope = 2**(self.order - j)
        new = [nocolor for i in range(self.size)]
        for i in range(2**j):
            if self.heap[pointer + i]:
                for brush in range(scope):
                    new[i*scope + brush] = yescolor
        pointer = pointer + 2**j
        output.append(new)
    return np.array(output)


