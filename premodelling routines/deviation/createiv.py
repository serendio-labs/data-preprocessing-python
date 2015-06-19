
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

