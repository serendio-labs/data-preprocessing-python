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

