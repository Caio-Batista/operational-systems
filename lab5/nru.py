import random

class PhysicalMemory:
	def __init__(self):	
		self.mem = {}

	def clock(self):
		for x in self.mem.keys():
			self.mem[x][1] = 0

	def contains(self, frame_id):
		return frame_id in self.mem

	def put(self, frame_id): # data, referenced, modified
		self.mem[frame_id] = ["data", 1, 1]

	def access(self, frame_id, mode): # mode true if write, false if read
		if self.contains(frame_id):
			self.mem[frame_id][1] = 1 # set the referenced bit
			
			if mode:
				self.mem[frame_id][0] = "data2"
				self.mem[frame_id][2] = 1 # set the modified bit
				return None
			else:
				self.mem[frame_id][2] = 0 # set the modified bit
				return self.mem[frame_id][0]
		return None

	def evict(self):
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

	def get_all(self, ref, mod):
		return [i for i in self.mem if self.mem[i][1:] == [ref,mod]]