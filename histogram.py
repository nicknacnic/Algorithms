# Authors Nic Williams && Rachel Platt && Roy De Jesus
# CSCI 3104 PS4
# Python Script for 4(a)
#
# Help received in data processing from these sources on StackOverflow:
# Daniel Hodgkins, elyase
#

import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('out.txt')
data.hist(bins=200)
plt.xlim([0,200])
plt.title("Distribution of Hash Locations")
plt.xlabel("Bucket Value")
plt.ylabel("Number of Names")
plt.show()
fig.savefig("hist.png")
