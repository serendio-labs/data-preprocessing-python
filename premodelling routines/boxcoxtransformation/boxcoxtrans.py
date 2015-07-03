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



