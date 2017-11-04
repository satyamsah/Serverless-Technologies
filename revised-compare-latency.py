import matplotlib.pyplot as plt
import numpy as np

x =np.asarray([0,100,200,400,800,1600,3000])

plt.gca().set_color_cycle(['red', 'green', 'blue', 'purple'])


#plt.plot(x, [0,03.9,07.4,14.1,27.901,59.501,106.175],linestyle='--',linewidth=2)
plt.plot(x, [0,03.9,07.4,14.1,27.901,59.501,106.175],linewidth=2)
plt.plot(x, [0,9.277,14.725,23.691,53.846,111.846,193.044],linewidth=2)
plt.plot(x,  [0,6.06,14.35,25.83,53.35,np.nan,np.nan],linewidth=2)
plt.plot(x, [0,5.224,1.263,2.261,4.814,9.232,21.060],linewidth=2)

plt.legend(['AWS FUCNTION', 'IBM', 'GOOGLE', 'AZURE'], loc='upper left')

plt.xlabel('Number of HTTP invocation')
plt.ylabel('Elapsed time in Seconds')
plt.show()
