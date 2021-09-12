import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

#Thomasan sampling make sure 
#header us this to header =none to make the titile of data to no from string
dataset=pd.read_csv("c:/Users/A Kumar/Desktop/ml2/Ads_CTR_Optimisation.csv")
"""import random
N=10000
d=10
ads_selected=[]
total_reward=0
for i in range(0,N):
    ad=random.randrange(d)
    ads_selected.append(ad)
    reward=dataset.values[i,ad]
    total_reward=total_reward+reward

plt.hist(ads_selected)
plt.show()"""
import random
###Thamson sampling algo Algorithm  from scratch
N=1000
d=10
ads_selected=[]
total_reward=0
No_of_selection_1=[0]*d
No_of_selection_0=[0]*d
for i in range(0,N):
    ad=0
    max_random=0
    for n in range(0,d):
        random_beta=random.betavariate(No_of_selection_1[n]+1,No_of_selection_0[n]+1)   
        if(random_beta> max_random):
            max_random=random_beta
            ad=n
    ads_selected.append(ad)
    reward=dataset.values[n,ad]
    
    if(reward==1):
        No_of_selection_1[i]=No_of_selection_1+1
    else:
        No_of_selection_0[i]=No_of_selection_0[i]+1
    total_reward=total_reward+reward


plt.hist(ads_selected)
plt.title("Histogram of ads Selection")
plt.xlabel("Ads")
plt.ylabel("No of Times Each Ads was Selcted")
plt.show()




        




