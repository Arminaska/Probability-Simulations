import numpy as np 
import random 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from time import sleep


#let's draw an interactive histogram


#plt.ion()
#
#fig,ax = plt.subplots()
##raw_x,raw_y = [],[]
#x,y = [],[]
#
#ax.hist(x)
#
#
#
#plt.ylim(0,100)
#plt.xlim(-2,2)
#
#plt.draw()
#n_bins = 4
#for i in range(1000):
#	x.append(random.gauss(-1,1))
#	
#	
#	plt.cla()
#	ax.hist(x,bins = n_bins,color = 'blue')
#	
#	fig.canvas.draw_idle()
#	plt.pause(0.00001)
#
#plt.waitforbuttonpress()

	
class RouletteWheel:
	def re_wheel(self):
		self.wheel = []
		for option in self.options:
			rng = random.randint(*self.int_limits)
			for i in range(rng):
				self.wheel.append(option)


	def __init__(self,options,int_limits):
		self.options = options
		self.int_limits = int_limits
		self.re_wheel()

	


	def random_roulette_wheel(self):
		#the extra limits argument is only for compatibility purposes.
		return random.choice(self.wheel)


	def linear_roulette_wheel(self):
		self.wheel = []
		for index in range(*self.int_limits):
			for j in range(index):
				self.wheel.append(index)
		return random.choice(self.wheel)

class Experiment:
	def __init__(self,epochs = 1000,generator_pack = (random.uniform,(0,1)),limits = (0,1)):
		self.generator,self.generator_arguments = generator_pack  #Please note how the generator is inserted in a tuple, and the arguments are 
		self.epochs = epochs									  # inserted in another tuple. 
		
		#self.limits = limits # Obsolete after introducing generator pack, and tuple unpacking
		

		self.npx = np.array([])



	def do_experiment(self):
		for _ in range(self.epochs):
			self.npx = np.append(self.npx,self.generator(*self.generator_arguments))


	def experiment_over(self):
		self.npx = np.array([])




class ProbabilityHistogram:
	

	def create_scene(self):
		self.fig,self.ax = plt.subplots()
		self.npx = np.array([])

		#self.ax.hist(self.npx)


	def __init__(self,experiment,color = 'blue',bins = 10):

		self.bins = bins
		self.color = color
		self.experiment = experiment #adding the experiment as an input greatly reduced the complexity of the algorithm

		#self.create_scene()


		


		#plt.ylim(*y_lims)
		#plt.xlim(*x_lims) # if you do these, and you do autoscale, you get two plots!



	def show_experiment(self,experiment):
		''' do the experiment statically, pass the random suffix 
			to run the experiment'''
		
		self.create_scene()  #if not used, the second plot will be empty
		
		experiment.do_experiment()	
	
		self.ax.hist(experiment.npx,color = self.color)
		#plt.autoscale(enable = True)
		plt.show()

		experiment.experiment_over()





	#def static_experiment(self,epochs = 1000,generator = random.uniform):
	#	''' do the experiment statically, pass the random suffix 
	#		to run the experiment'''
	#	
	#	self.create_scene()  #if not used, the second plot will be empty
#
#
	#	for _ in range(epochs):
	#		self.npx = np.append(self.npx,generator(*limits))
	#	
	#	#self.npx /= epochs
	#	#print(self.npx)
	#	self.ax.hist(self.npx,color = self.color)
	#	plt.autoscale(enable = True)
	#	plt.show()


		#After the experiment, clean the data
		#self.npx = np.array([])


	def animation_update(self,i):
		plt.cla()
		self.experiment.npx = np.append(self.experiment.npx,self.experiment.generator(*self.experiment.generator_arguments)) #call the input experiment methods!
		self.ax.hist(self.experiment.npx,self.bins,color = self.color)


	def animate_experiment(self,interval = 100):
		self.create_scene()
		anim = FuncAnimation(self.fig,self.animation_update,interval)
		plt.show()

wheel = RouletteWheel(range(40),int_limits = (0,10))
exp = Experiment(epochs = 100000,generator_pack = (random.gauss,(0,1))) # You need to enter the generator as tuple (generator,(tuple of generator arguments))
hist = ProbabilityHistogram(exp)





hist.animate_experiment(interval = 1)
#hist.show_experiment(exp)