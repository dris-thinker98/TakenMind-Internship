import numpy as np
import matplotlib.pyplot as plt

axes_values = np.arange(-100,100,10)

dx, dy = np.meshgrid(axes_values,axes_values)

print "dx:"
print dx

print "dy"
print dy

function1 = 2*dx+3*dy
function2 = np.cos(dx)+np.cos(dy)

print function1
print function2

#replace function2 by function1 to get graph of function1
#plotting the function on graph
plt.imshow(function2)
plt.title("function cos plot")
plt.colorbar()
plt.savefig('myfig2.png')

