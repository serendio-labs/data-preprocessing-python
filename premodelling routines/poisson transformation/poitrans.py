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





def poitrans(str,list):
    w= pd.read_csv(str,usecols=list)


    f= DataFrame(w)
    c=f.astype(float)


    x=c.as_matrix()

    a=((x**0.5)+((x+1)**0.5))/2

    print a

