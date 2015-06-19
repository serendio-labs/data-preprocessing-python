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

