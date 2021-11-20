import numpy as np
import matplotlib.pyplot as plt

class ChaosGame:
	# constructor for class ChaosGame
	def __init__(self, n, r):
		self.n = n
		self.r = r
		self._generate_ngon() # calling methode _generate_ngon()
		"""
		test checking if n >= 3 and 0 < r < 1.0

		if this is not the case:
		if self.n < 3:
		----------------------------------------

		ValueError: n must be >= 3

		----------------------------------------


		if self.r < 0 or self.r > 1:
		----------------------------------------

		ValueError: r must be greater than 0 and less than 1

		----------------------------------------

		"""
		if self.n < 3:
			raise ValueError("n must be >= 3")

		if self.r < 0 or self.r > 1:
			raise ValueError("r must be greater than 0 and less than 1")

	# Generating corners for ngon
	def _generate_ngon(self):
		theta = np.linspace(0, 2*np.pi, self.n+1)
		self.C_list = []
		for i in range(self.n+1):
			# adding corners to C_list
			c_i = np.array([np.sin(theta[i]),np.cos(theta[i])])
			self.C_list.append(c_i)

	# plotting ngon
	def plot_ngon(self):
		plt.scatter(*zip(*self.C_list))
		plt.show()

	# finding startingpoint
	def _starting_point(self):
		x_0 = np.array([0, 0])
		weight = np.random.random(self.n) # weight is a list of n random weights
		for i in range(self.n):
			w = weight[i]/sum(weight) # making the sum of all the weights equal
			x_0 = x_0 + w*self.C_list[i]
		return x_0

	# iterating steps, creating a X list with points and discarding the 5 first points
	def iterate(self, steps, discard=5):
		self.X = np.zeros((steps+discard, 2))
		self.X[0] = self._starting_point()
		self.rc = np.zeros(len(self.X))
		j = np.random.randint(len(self.C_list))
		self.rc[0] = j
		# iterating through X list creating each Xi point and storing j values to rc list
		for i in range(len(self.X)-1):
			j = np.random.randint(len(self.C_list))
			self.X[i+1] = self.r*self.X[i] + (1 - self.r)*self.C_list[j]
			self.rc[i+1] = j
		self.X = self.X[discard:]
		self.rc = self.rc[discard:]

	# plotting figure
	def plot(self, color=False, cmap="jet"):
		"""
		if color == True
		calling property gradiant_color

		else
		default black color
		"""
		if color == True:
			colors = self.gradiant_color
		else:
			colors = "black"
		plt.scatter(*zip(*self.X), c=colors, cmap=cmap, s=0.2)
		plt.axis("equal")

	# method showing plot
	def show(self, color=False, cmap="jet"):
		self.plot(color, cmap)
		plt.show()

	# proparty methode creating _C list with color gradiant values
	@property
	def gradiant_color(self):
		self._C = [0 for i in range(len(self.rc))]
		self._C[0] = self.rc[0]
		for i in range(len(self.rc)-1):
			self._C[i+1] = (self._C[i] + self.rc[i+1])/2
		return self._C

	# methode saving figure as filename.png
	def savepng(self, outfile, color=False, cmap="jet"):
		self.plot(color, cmap)
		# checking if outfile is a png file
		if outfile[-4:] != ".png":
			for i in outfile:
				"""
				if outfile is named with another filetype
				-----------------------------------------

				ValueError: outfile can only be .png file, {outfile} is not accepted

				-----------------------------------------
				"""
				if i == ".":
					raise ValueError(f"outfile can only be .png file, {outfile} is not accepted")

			outfile = outfile + ".png"

		plt.savefig(outfile, dpi=300, transparent=False)
		plt.clf()

			
# main function calling class
def main():
	
	CG = ChaosGame(5, 0.5)
	CG.plot_ngon()

	X_list = []
	for i in range(1001):
		X_list.append(CG._starting_point())
	plt.scatter(*zip(*X_list))
	plt.show()


	CG = ChaosGame(3, 0.5)
	CG.iterate(10000)
	CG.show(color=True)
	#CG.savepng("test1.png", color=True)


	"""
	CG1 = ChaosGame(3, 0.5)
	CG1.iterate(10000)
	CG1.savepng(outfile="chaos1.png")

	CG = ChaosGame(4, 1/3)
	CG.iterate(10000)
	CG.savepng(outfile="chaos2.png")

	CG = ChaosGame(5, 1/3)
	CG.iterate(10000)
	CG.savepng(outfile="chaos3.png")

	CG = ChaosGame(5, 3/8)
	CG.iterate(10000)
	CG.savepng(outfile="chaos4.png")

	CG = ChaosGame(6, 1/3)
	CG.iterate(10000)
	CG.savepng(outfile="chaos5.png")
	"""
	
	
if __name__ == "__main__":
	main()


