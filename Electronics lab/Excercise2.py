import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import pandas as pd
import seaborn as sns

#Plotting all the graphs on one-> the ultimate plotting function *-*^
def Ultimate_PLOT(x1,y1,x2,y2,x3,y3):

    df1=pd.DataFrame({'logf': x1, 'A':y1})
    
    df2=pd.DataFrame({'logf': x2, 'A':y2})
    
    df3=pd.DataFrame({'logf': x3, 'A':y3})
    
    sns.set_style("whitegrid")

    plt.plot( 'logf', 'A', data=df1, linestyle='-', marker='o', linewidth=4 ,markersize=14,  label="jednostupanjsko", color='red')
    plt.plot( 'logf', 'A', data=df2, linestyle='-', marker='o', linewidth=4 ,markersize=14,label='dvostupanjsko', color='blue')
    plt.plot( 'logf', 'A', data=df3, linestyle='-', marker='o', linewidth=4 ,markersize=14,label='povratna veza', color='green')

    plt.ylabel('$A$',rotation='horizontal', fontsize=25,position=(1,1))
    plt.xlabel('$log(f)$',fontsize=25)
    plt.tick_params(axis = 'both', which = 'major', labelsize = 25)
    plt.legend(loc='center' , prop={'size': 16})
    plt.show()
    
    return

def Plotting(x,y):

    df=pd.DataFrame({'logf': x, 'A':y})
    sns.set_style("whitegrid")

    plt.plot( 'logf', 'A', data=df, linestyle='-', marker='o', linewidth=4 ,markersize=14,color='green',)
    plt.ylabel('$A$',rotation='horizontal', fontsize=25,position=(1,1))
    plt.xlabel('$log(f)$',fontsize=25)
    plt.tick_params(axis = 'both', which = 'major', labelsize = 25)
    plt.show()
    return

#Second-stage amplifier

#input data
u_out = np.array([125,146,155,165,175,182.2,185,186,189.2,221,220,218,217,211,209,195,186,162.7,130.7])
u_in = np.array([6.27,6.27,6.25,6.23,6.25,6.32,6.3,6.28,6.37,7.4,7.35,7.31,7.38,7.25,7.27,7.14,7.03,6.76,6.37])
f = np.array([36,42,50,70,106,165,421,703,1192,2834,3894,5122,8084,17107,20385,31051,37101,50766,65610])

A1=u_out/u_in   #calculating amplification
logf1=sc.log(f) 

#Plotting(logf1,A1)

#Two stage amplifier

#input data
u_out = np.array([365,724,833,873,912,940,947,963,977,957,958,954,901,775,615,461,376])
u_in = np.array([6.4,6.4,6.4,6.4,6.4,6.4,6.4,6.4,6.4,6.45,6.35,6.3,6.31,6.1,5.83,5.54,5.35])
f = np.array([20,52,81,104,145,206,551,1072,1485,3752,4975,6220,21000,35456,51202,67566,78435])

A2=u_out/u_in   #calculating amplification
logf2=sc.log(f) 

#Plotting(logf2,A2)

# Amplifier with negative feedback

#input data
u_out = np.array([553,670,726,818,843,880,910,940,978,999,1006,1006,1038,992,988,985,973,955,847,798,728,522])
u_in = np.array([7.6,7.6,7.58,7.58,7.56,7.56,7.58,7.59,7.65,7.72,7.66,7.67,7.92,7.53,7.46,7.46,7.46,7.46,7.32,7.22,7.22,6.65])
f = np.array([26,34,39,50,55,65,75,93,135,183,410,811,1754,3954,7954,10465,14705,19251,32834,37752,44828,65721])

A3=u_out/u_in   #calculating amplification
logf3=sc.log(f) 

Plotting(logf3,A3)

#Ultimate_PLOT(logf1,A1,logf2,A2,logf3,A3)