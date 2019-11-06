import numpy as np
import matplotlib.pyplot as plt

#print("Hello world!")

def Circ(r):
	"""
	Calculates circumference of circle with radius r
	"""
	C = 2*np.pi*r
	return C


def Area(r):
	A = np.pi*r**2
	return A

def PlotCircle(r):
	theta = np.linspace(0, 2*np.pi, num=1E3)
	x = r*np.cos(theta)
	y = r*np.sin(theta)
	fig, axes = plt.subplots()
	axes.plot(x, y)
    

#r=3
#PlotCircle(r)
#print(Area(r))
