'''
Copyright 2015 Serendio Inc.
Author - Satish Palaniappan
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
'''


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

