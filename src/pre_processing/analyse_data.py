import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path_dir = 'src\data\outer_round1_forward.csv'
ofr1 = pd.read_csv(path_dir)
ofr1 = ofr1.dropna(how="all")

path_dir = 'src\data\outer_round1_backwards.csv'
obr1 = pd.read_csv(path_dir)
obr1 = obr1.dropna(how="all")

path_dir = 'src\data\inner_round1_forward.csv'
ifr1 = pd.read_csv(path_dir)
ifr1 = ifr1.dropna(how="all")

path_dir = 'src\data\inner_round1_backwards.csv'
ibr1 = pd.read_csv(path_dir)
ibr1 = ibr1.dropna(how="all")
print(ofr1)
s1 = ofr1['steering']
o1 = ofr1['fixpoint_odometer_steps']

s2 = obr1['steering']
o2 = obr1['fixpoint_odometer_steps']

s3 = ifr1['steering']
o3 = ifr1['fixpoint_odometer_steps']

s4 = ibr1['steering']
o4 = ibr1['fixpoint_odometer_steps']


plt.figure(figsize=(20,6))
plt.plot(o1, s1, "r")
plt.plot(o2, s2, "b")
plt.plot(o3, s3, "g")
plt.plot(o4, s4, "y")
plt.xlabel = ('Odometer Schritte')
plt.ylabel = ('Hall-Spannung in mV')
plt.title = ('Fahrt 1')

plt.show()