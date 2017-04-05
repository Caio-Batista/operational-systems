class PhysicalMemory:
  ALGORITHM_AGING_NBITS = 8

  def __init__(self):
    self.mem = {}

  def contains(self, frame_id):
    return frame_id in self.mem

  def put(self, frameId):
    self.mem[frameId] = Element("data1")

  def evict(self):
    f_id = self.mem.keys()[0]
    for i in self.mem.keys():
      if self.mem[i].numericValue() < self.mem[f_id].numericValue():
        f_id = i
    del self.mem[f_id]
    return f_id

  def clock(self):
    for i in self.mem.keys():
      self.mem[i].clock()

  def access(self, frameId, isWrite):
    if isWrite:
      self.mem[frameId].setd("data2")
      return
    else:
      return self.mem[frameId].read()


class Element:

  def __init__(self, data):
    self.data = data
    self.counters = [0 for i in range(8)]
    self.referenced = 0

  def numericValue(self): # eficiencia foi pro espaco
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

