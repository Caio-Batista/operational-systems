
class PhysicalMemory:
  ALGORITHM_AGING_NBITS = 8
  """How many bits to use for the Aging algorithm"""

  def __init__(self, algorithm):
    assert algorithm in {"fifo", "nru", "aging", "second-chance"}
    self.algorithm = algorithm

    if self.algorith == "second-chance":
		self.frames = []
		self.acessados = []

  def put(self, frameId):
    """Allocates this frameId for some page"""
    if self.algorithm == "second-chance":
		self.frames.append(frameId)
		self.acessados.append(0)

  def evict(self):
    """Deallocates a frame from the physical memory and returns its frameId"""
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


  def clock(self):
    """The amount of time we set for the clock has passed, so this is called"""
    pass

  def access(self, frameId, isWrite):
    """A frameId was accessed for read/write (if write, isWrite=True)"""
    if self.algorithm == "second-chance":
		index = self.frames.index(frameId)	
		self.acessados[index] = 1	

