

__author__ = 'kshitij'

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



def stndize(str,list):

    s=list
    w= pd.read_csv(str,usecols=s)
    frame = DataFrame(w)

    t=frame.mean()
    print t
    z=frame.std()
    print z
    print (w-t)/z

    return;



def gs(str,list):
    s = list
    t= pd.read_csv(str,usecols= s)

    w=DataFrame(t)



    try:
         plt.scatter(w[s[0]],w[s[1]],color='red')

         plt.show()
    except:
        pass
    try:
        w.hist()
        plt.show()

        w.plot(kind='box',by=list)
        plt.show()
    except:
        pass

    t=w.applymap(np.isreal)
    print t

    b= ''.join(s)
    for i in t[b]:
        if i==False:

            a=(w[b].value_counts())


            a.plot(kind='bar')

            plt.show()
            break



def mydeviate(str,list,Deviation=0,MeanAbsDeviation=1,MeanSqDev=0):

    s=list

    w= pd.read_csv(str,usecols=s)

    s=DataFrame(w)
    t= s.mean()

    if Deviation==1:


        b=[w-t]

        print b

    if MeanAbsDeviation==1:

        a=[abs(s)-t]
        print(a)

    if MeanSqDev==1:

        c=[(w-t)**2]
        print c


    return




def skewness(str,list):
    s= list



    w = pd.read_csv(str, usecols=s)

    frame = DataFrame(w)

    h=len(w)

    t = frame.mean()



    d = frame.std()

    e = ((w - t) /d) ** 3

    g=e.sum()

    i=(h*g)/((h-1)*(h-2))


    print 'skewness=',i

def kurtosis(str,list):

    s=list
    w = pd.read_csv(str, usecols=s)

    frame = DataFrame(w)

    h=len(w)


    print h
    t = frame.mean()

    d = frame.std()

    e = ((w - t) /d) ** 4

    g=e.sum()


    p1=h*(h+1)
    p2=float((h-1)*(h-2)*(h-3))
    p3=float(3*((h-1)**2))
    p4=(h-2)*(h-3)

    i=(((p1/p2)*g)-(p3/p4))

    print 'kurtosis=',i



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







def proptrans(str,list):

        w= pd.read_csv(str,usecols=list)


        f= DataFrame(w)
        c=f.astype(float)


        x=c.as_matrix()



        t=np.arcsin(x**0.5)

        print t


def poitrans(str,list):
    w= pd.read_csv(str,usecols=list)


    f= DataFrame(w)
    c=f.astype(float)


    x=c.as_matrix()

    a=((x**0.5)+((x+1)**0.5))/2

    print a

def boxcoxtrans(str,list):
        s=list
        w = pd.read_csv(str, usecols=s)

        f = DataFrame(w)
        c = f.astype(float)

        x = c.as_matrix()


        e = []

        for j in np.linspace(-2, 2, num=21):

                if j != 0:

                    b =(x**j)

                    d=[]
                    c=[]
                    for i in range(0,len(b)):
                        c = b[i]
                        d.append(c[0])
                    

                    t = stats.shapiro(d)
                    
                    
                    e.append(t[1])




        for i in range(0,len(e)):

            if e[i]==max(e):

                break
        t=(-2+0.2*i)

        if t>=0:
            t=(-2+0.2*(i+1))

        print 'optimal lembda=',t

        h=((x**t)-1)/t
        l=[]
        m=[]
        for i in range(0,len(h)):
            l = h[i]
            m.append(l[0])


        print pd.DataFrame(m)
        k=stats.shapiro(m)

        print 'shapiro test of trans column',k






