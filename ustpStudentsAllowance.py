import matplotlib.pyplot as plt
import numpy as np

# Data of student's allowance based on lecture 3

data = [200,200,200,300,200,300,200,400,250,250,200,200,300,200,200,180,240,100]

fig,ax = plt.subplots()
ax.hist(data, bins=80,color="yellow", edgecolor='black')

# Change the frequency numbers 
ax.set_yticks(range(1,19))
# set the limit for y-axis
ax.set_ylim(0,18)

# now for the x axis
ax.set_xticks(range(0,501,50))
ax.set_xlim(0,500)

ax.set_title("USTP Students Allowance")
ax.set_xlabel("Allowance")
ax.set_ylabel("Frequency")
plt.show()
