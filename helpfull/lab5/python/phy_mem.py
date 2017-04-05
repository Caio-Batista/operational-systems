import random
class PhysicalMemory:
	
  ALGORITHM_AGING_NBITS = 8

  def __init__(self,algorithm):
    assert algorithm in {"fifo", "nru", "aging", "second-chance"}
    self.algorithm = algorithm
    if self.algorithm == "fifo":
		self.frames = []
    if self.algorithm == "aging":
		self.mem = {}
    if self.algorithm == "nru":
		self.mem = {}	
    if self.algorithm == "second-chance":
		self.frames = []
		self.acessados = []
		
  def contains(self, frame_id):
	if self.algorithm == "nru":
	  return frame_id in self.mem	  
	if self.algorithm == "aging":
	  return frame_id in self.mem

  def put(self, frameId):
    if self.algorithm == "fifo":
	  self.frames.insert(0,frameId)
    if self.algorithm == "nru":
	  self.mem[frameId] = ["data", 1, 1]  
    if self.algorithm == "aging": 
	  self.mem[frameId] = Element("data1")
    if self.algorithm == "second-chance":
		self.frames.append(frameId)
		self.acessados.append(0)
		
  def evict(self):
    if self.algorithm == "aging":  
      f_id = self.mem.keys()[0]
      for i in self.mem.keys():
        if self.mem[i].numericValue() < self.mem[f_id].numericValue():
          f_id = i
      del self.mem[f_id]
      return f_id
      
    if self.algorithm == "second-chance":
		index = 0
		while (True):
			if self.acessados[index] == 0:
				self.acessados.pop(index)
				return self.frames.pop(index)
			else :
				self.acessados.pop(index)
				frameId = self.frames.pop(index)
				self.put(frameId)
				
    if self.algorithm == "fifo" and len(self.frames) > 0:
	  page = self.frames.pop()
	  return page

    if self.algorithm == "nru":
	  class1 = self.get_all(0,0)
	  if len(class1) > 0:
		f_id = random.choice(class1)
		del self.mem[f_id]
		return f_id

	  class2 = self.get_all(0,1)
	  if len(class2) > 0:
		f_id = random.choice(class2)
		del self.mem[f_id]
		return f_id

	  class3 = self.get_all(1,0)
	  if len(class3) > 0:
		f_id = random.choice(class3)
		del self.mem[f_id]
		return f_id

	  class4 = self.get_all(1,1)
	  if len(class4) > 0:
		f_id = random.choice(class4)
		del self.mem[f_id]
		return f_id  		
    else:
		return "ERROR: NO PAGES TO REMOVE"    

  def clock(self):
    if self.algorithm == "aging":
      for i in self.mem.keys():
        self.mem[i].clock()
    if self.algorithm == "nru":
	  for x in self.mem.keys():
	    self.mem[x][1] = 0		    
    else: pass

  def access(self, frameId, isWrite):
    if self.algorithm == "aging":
      if isWrite:
        self.mem[frameId].setd("data2")
        return
      else:
        return self.mem[frameId].read()

    if self.algorithm == "nru":
      if self.contains(frameId):
		self.mem[frameId][1] = 1
			
		if isWrite:
		  self.mem[frameId][0] = "data2"
		  self.mem[frameId][2] = 1 
		  return None
		else:
		  self.mem[frameId][2] = 0 
		  return self.mem[frameId][0]
      return None
    if self.algorithm == "second-chance":
		index = self.frames.index(frameId)	
		self.acessados[index] = 1	

    else: pass  		

  def get_all(self, ref, mod):
    return [i for i in self.mem if self.mem[i][1:] == [ref,mod]]
    
class Element:

  def __init__(self, data):
    self.data = data
    self.counters = [0 for i in range(8)]
    self.referenced = 0

  def numericValue(self): 
    lista_str = [str(i) for i in self.counters]
    return int(''.join(lista_str), 2)

  def read(self):
    self.referenced = 1
    return self.data

  def setd(self, data):
    self.data = data

  def clock(self):
    self.counters.pop()
    self.counters.insert(0, self.referenced)
    self.referenced = 0

