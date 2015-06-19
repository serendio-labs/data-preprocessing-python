
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

