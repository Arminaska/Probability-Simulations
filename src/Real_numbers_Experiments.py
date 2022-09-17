import random



def is_within(x,a,b):
	return x < b and x > a 	



class Real:

	def __init__(self,start = 0,stop = 1,lims_mtrx = [[0,1],[0,1]]):
		self.start = start
		self.stop = stop
		self.limits = lims_mtrx


	def do_experiment(self,epochs = 1000,a = 0,b = 0.5):
		inside = 0
		
		for i in range(epochs):
			rng = random.uniform(self.start,self.stop)
			
			if is_within(rng,a,b):
				inside += 1
		
		return inside/epochs



	def do_2Dexperiment(self,epochs = 1000,explims = [[0,0.7],[0,0.7]]):
		inside = 0

		for _ in range(epochs):
			rng = [random.uniform(*self.limits[0]),random.uniform(*self.limits[1])]
			if is_within(rng[0],*explims[0]):
				if is_within(rng[1],*explims[1]):
					inside += 1
		return inside/epochs

			

			#is it inside the limits?


		


x = Real()
print(x.do_2Dexperiment(epochs = 1000))




