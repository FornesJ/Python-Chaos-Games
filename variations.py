import numpy as np
import matplotlib.pyplot as plt 
from chaos_game import ChaosGame

# class Variations
class Variations:
    # constructor for x, y, name and calling a methode in variations
    def __init__(self, x, y, name):
        self.x = x
        self.y = y 
        self.name = name
        self._func = getattr(Variations, name)

    # linear variation
    @staticmethod
    def linear(x, y):
        return x, y

    # handkerchief variation
    @staticmethod
    def handkerchief(x, y):
        # defining r and theta
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(x, y)
        return r*np.sin(theta + r), r*np.cos(theta - r) 

    # swirl variation
    @staticmethod
    def swirl(x, y):
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(x,y)
        return x*np.sin(r**2) - y*np.cos(r**2), x*np.cos(r**2) + y*np.sin(r**2)

    # disc variation
    @staticmethod
    def disc(x, y):
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(x,y)
        return theta/np.pi*np.sin(np.pi*r), theta/np.pi*np.cos(np.pi*r)

    # diamond variation
    @staticmethod
    def diamond(x, y):
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(x,y)
        return np.sin(theta)*np.cos(r), np.cos(theta)*np.sin(r)

    # heart variation
    @staticmethod
    def heart(x, y):
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(x,y)
        return r*(np.sin(theta*r)), r*(-np.cos(theta*r))

    # methode transform calling variations
    def transform(self):
    	return self._func(self.x, self.y)

    # calling chaos game class and returning x-values, y-values and name
    @classmethod
    def from_chaos_game(cls, cg, name):
        cg.iterate(102)
        return cls(cg.X[:,0], cg.X[:,1], name)

# mein function
def main():
    N = 101
    grid_values = np.linspace(-1, 1, N)
    x, y = np.meshgrid(grid_values, grid_values)
    x_values = x.flatten()
    y_values = y.flatten()
        

    transformations = ["linear", "handkerchief", "swirl", "disc", "diamond", "heart"]
    variations = [Variations(x_values, y_values, version) for version in transformations]

    fig, axs = plt.subplots(2, 3, figsize=(9, 9))
    for i, (ax, variation) in enumerate(zip(axs.flatten(), variations)):
       
        
        u, v = variation.transform()
        
        ax.plot(u, -v, markersize=1, marker=".", linestyle="", color="black")
        ax.scatter(u, -v, s=0.2, marker=".", color="black")
        ax.set_title(variation.name)
        ax.axis("off")
    plt.show()
    
if __name__ == "__main__":
	main()







