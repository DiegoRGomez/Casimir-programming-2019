import numpy as np
import matplotlib.pyplot as plt

#print("Hello world!")

def Circ(r):
	"""
	This function calculates the circumference of the circle, where r is the radius of the circle. hkfjahkjlfadavVDF 
	this is just in case you are writting the same thing and we wouldn't be able to discriminate the two version. 
	"""
	C = 2*np.pi*r
	return C


def Area(r):
	A = np.pi*r**2
	return A

def PlotCircle(r):
        with plt.style.context('bmh'):
            theta = np.linspace(0, 2*np.pi, num=1E3)
            x = r*np.cos(theta)
            y = r*np.sin(theta)
            fig, axes = plt.subplots()
            plt.ylim(-r-.2*r, r+.2*r)
            plt.xlim(-r-.2*r, r+.2*r)
            axes.plot(x, y)
            axes.spines['left'].set_position('center')
            axes.spines['bottom'].set_position('center')
            axes.spines['right'].set_color('none')
            axes.spines['top'].set_color('none')
            plt.gca().set_aspect('equal', adjustable='box')
            #Save to .png:
            plt.savefig("CirleRadius" + str(r) + ".png")
        

def AreaTriangle(b,h):
    return b*h/2
