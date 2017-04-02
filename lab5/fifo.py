
class PhysicalMemory:
  ALGORITHM_AGING_NBITS = 8
  """How many bits to use for the Aging algorithm"""

  def __init__(self, algorithm):
    assert algorithm in {"fifo", "nru", "aging", "second-chance"}
    self.algorithm = algorithm
    if self.algorithm == "fifo":
		self.frames = []

  def put(self, frameId):
    """Allocates this frameId for some page"""
    if self.algorithm == "fifo":
		self.frames.insert(0,frameId)

  def evict(self):
    """Deallocates a frame from the physical memory and returns its frameId"""
    if self.algorithm == "fifo" and len(self.frames) > 0:
		page = self.frames.pop()
		return page
    else:
		return "ERROR: NO PAGES TO REMOVE"


  def clock(self):
    """The amount of time we set for the clock has passed, so this is called"""
    pass

  def access(self, frameId, isWrite):
    """A frameId was accessed for read/write (if write, isWrite=True)"""
    pass
    
