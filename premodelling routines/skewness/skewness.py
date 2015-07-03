'''
Copyright 2015 Serendio Inc.
Author - kshitij soni
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

