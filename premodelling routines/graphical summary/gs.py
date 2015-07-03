
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



