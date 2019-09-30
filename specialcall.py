class SpecialCall:
	def __init__(self, func, args):
		self.func = func
		self.args = args
		
	def getFunc(self):
		return self.func
		
	def getArgs(self):
		return self.args
		
	def setFunc(self, func):
		self.func = func
		
	def setArgs(self, args):
		self.args = args
		
