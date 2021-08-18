import matplotlib.pyplot as plt
year = [1950,1970,1990,2010]
pop = [2.519,3.692,5.263,6.972]
year = [1800,1840,1890,1920] + year
pop = [1.1,1.5,1.9,2.1]+ pop
plt.plot(year,pop)
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("World population projections")
plt.yticks([0,2,4,6,8,10],["0","2B","4B","6B","8B","10B"])
plt.show()