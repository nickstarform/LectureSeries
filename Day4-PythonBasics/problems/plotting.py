"""Tutorial on loading in data."""

import csv
import matplotlib.pyplot as plt
import numpy as np


files = ['learnjava.csv', 'learnpython.csv']

a = []
for x in files:
    with open(x, 'r') as csvfile:
        a.append([row for row in csv.reader(csvfile, delimiter=', ')])

learnjava = np.array([float(x[1]) for x in a[0][3:]], dtype=float)
learnpython = np.array([float(x[1]) for x in a[1][3:]], dtype=float)

plt.figure(figsize=[10, 7])
plt.scatter(x=range(len(learnpython)), y=learnpython, color='blue', s=30,
            label='Python')
plt.scatter(x=range(len(learnjava)), y=learnjava, color='red', s=30,
            label='Java')
plt.xlabel('Time', fontsize=25)
plt.ylabel('Frequency', fontsize=25)
plt.title('Google Trends', fontsize=25)
plt.tick_params(axis='both', which='major', labelsize=25)
plt.tick_params(axis='both', which='minor', labelsize=25)
plt.legend()
plt.tight_layout()
plt.show()

# end of file
