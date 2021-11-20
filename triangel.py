import numpy as np
import matplotlib.pyplot as plt

class TRIANGEL:
	def __init__(self):
		# constructors for c0, c1, c2 and an empty list that will contain c integers
		self.C0 = np.array([0,0])
		self.C1 = np.array([1,0])
		self.C2 = np.array([0.5,np.sqrt(3)/2])
		self._typ = []

	# picking startingpoint
	def X_zero(self, w):
		return w[0]*self.C0 + w[1]*self.C1 + w[2]*self.C2

	# giving wight random values with total weight sum equalls 1
	def weight(self):
		weight = np.random.random(3)
		w = []		
		for i in range(len(weight)):
			w.append(weight[i]/sum(weight))
		return w

	# finding X_i+1
	def new_X(self, x_i):
		C_list = [self.C0, self.C1, self.C2]
		j = np.random.randint(3)
		self._typ.append(j)
		return (x_i + C_list[j])/2

	# methode plotting triangel using plt.scatter
	def plot(self, X_list, size=None, color=None):
		plt.scatter(*zip(*X_list), s=size, c=color)
		plt.axis("equal")
		plt.axis("off")
		plt.show()


	# adding color by corner
	def color(self):
		color = np.array(["red", "green", "blue"])
		return color, self._typ

	# adding alternating color
	def alternating_color(self):
		del self._typ[:5]
		C = np.zeros((10000,3))
		r = np.array([[1,0,0],[0,1,0],[0,0,1]])
		for i in range(len(self._typ)-1):
			j = self._typ[i]
			C[i+1] = (C[i] + r[j])/2
		return C


def main():
	T = TRIANGEL()

	# creating triangel with corner points
	corners = []
	for i in range(1000):
		w_list = T.weight()
		corners.append(T.X_zero(w_list))
	T.plot(corners)

	# creating wight and X list
	W_0 = T.weight()
	X = [0 for i in range(10005)]
	X[0] = T.X_zero(W_0)

	# calculating X_i and removing the first 5 iterations
	for i in range(len(X)-1):
		X[i+1] = T.new_X(X[i])
	del X[:5]

	# plotting triangel with 3 colors
	color, typ= T.color()
	T.plot(X, 0.2, color[typ[4:]])

	# plotting triangel with alternating colors
	color = T.alternating_color()
	T.plot(X, 0.2, color)
	

if __name__ == "__main__":
	main()



