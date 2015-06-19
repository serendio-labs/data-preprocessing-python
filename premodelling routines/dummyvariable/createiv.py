from numpy import mean
import numpy as np
import pandas as pd
import csv
from collections import defaultdict
from pandas import DataFrame, Series
from StringIO import StringIO
import scipy
import matplotlib.pyplot
import matplotlib.pyplot as plt
import math as mt
import scipy.stats as stats






def createiv(str,list,matrix=0,zero=1):

    s=list
    w = pd.read_csv(str)

    frame = DataFrame(w)

    if matrix==1:

        dummy_ranks = pd.get_dummies(w[s], prefix=s)

        dummy_ranks[s]=w[s]


        print dummy_ranks


    if zero==1:
        for i in range(0,len(s)):
            sg = s[i]
            t=np.unique(w[sg])


            f=len(w)





            df_ = pd.DataFrame(columns=t,index=np.arange(f))
            df_ = df_.fillna(0)


            length=len(t)



            count =0
            for j in w[sg]:

                for i in range(length):

                    if j == t[i]:
                        df_.at[count,t[i]]=1

                count = count + 1





            df_=df_.drop(df_.columns[0],axis=1)
            print df_







