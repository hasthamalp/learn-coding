# Demonstrating use of matplotlib.patches.Circle() function
# to plot a colored Circle

import matplotlib.pyplot as plt

figure, axes = plt.subplots()
Drawing_colored_circle = plt.Circle(( 0.6 , 0.6 ), 0.2 )

axes.set_aspect( 1 )
axes.add_artist( Drawing_colored_circle )
plt.title( 'Colored Circle' )
plt.show()
