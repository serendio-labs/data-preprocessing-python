# data-preprocessing
Data pre-processing utility for Machine Learning

Standardization

Function Name :stndize
Details       :stndize('file path',list of columns)
               Transforms originalvalue into its respective "Z" value
               return Returns standardized column              

Example

INPUT  : stndize('/home/kshitij/rstudio-0.98.1103/bin/iris.csv',['Sepal.Length'])
OUTPUT : standardize column
 
    Sepal.Length
0       -0.897674
1       -1.139200
2       -1.380727
3       -1.501490
4       -1.018437
5       -0.535384






Graphical Summary

Function Name:   gs
Details      :   gs('file path',list of columns)
Gives four types of graphical summary Histogram,Box plot,scatter plot,bar plot only for categorical variables.
details Histogram displays the values in Frequency Domain. Outliers and Skewness of the distribution can be assed usingbox-    Plot.scatter plot is used to get the graph between two columns.so to get scatter plot we should give only two columns. Bar-plots only for categorical variables.

return plots

Examples
INPUT : gs('/home/kshitij/rstudio-0.98.1103/bin/iris.csv',['Sepal.Length'])

OUTPUT:plots of the given column







Deviations

Function Name:mydeviate
Details      :mydeviate('file path',list of columns,0,1,0)
This functions addresses Deviation, MAD & MSD.
Three numeric parameters Parameter 1: It is a column of a Data Frame,Parameter 2: If the second parameter = 1, it then displays DEVIATIONS for each observation,Parameter 3: If the third parameter = 1, it then displays column required to compute MAD,Parameter 4: If the fourth parameter = 1, it then displays column required to compute MSD
return Displays the computed columns

Example

INPUT :mydeviate('/home/kshitij/rstudio-0.98.1103/bin/iris.csv',['Sepal.Length'],0,1,0)
OUTPUT:deviations of given columns

     Sepal.Length
0        0.552544
1        0.889878
2        1.307211
3        1.545878
4        0.711211
5        0.196544











dummy variables

Function Name: createiv
details      : createiv('file path',list of columns,0,1)
Creates two types of indicator variables.Indicator Variables is a method that is widely used in modeling particularly to handle data that are NOMINAL in nature.  It converts NOMINAL data into a meaningful numerical variables knows as ‘Indicator Variables’ (IV).  The other names for Indicator Variables are also known as Dummy Variables (DV).At times, Indicator Variables (IV) were rarely applied even on NOMINAL data, to convert them into meaningful numerical variables.Indicator Variables (IVs) is widely applied in Regression Techniques, Machine Learning Techniques & Multivariate Techniques such as Cluster Analysis, etc.
INPUT contains the type of dummy variables you want to get like matrix and zero based.
return Indicator Variables Columns
Example
INPUT :createiv('/home/kshitij/rstudio-0.98.1103/bin/iris.csv',['Sepal.Length'],0,1)
OUTPUT:dummy variable columns of the given type and given columns
    0  1
0   1  0
1   1  0
2   0  1
3   0  1
4   1  0









skewness

Functio Name:skewness
Details     :skewness('file path',list of columns)
Measure of Descriptive Statistics
details Skewness addresses the characteristics of symmetry.
return Gives the skewness value

Example

INPUT :skewness('/home/kshitij/rstudio-0.98.1103/bin/iris.csv',['Sepal.Length'])
OUTPUT:skewness of given column

Sepal.Length  skewness=  0.314911








kurtosis

Functio Name :kurtosis
Details      :kurtosis('file path',list of columns)
description Measure of Descriptive Statistics
details Kurtosis addresses the characteristics of ‘Peakedness’ & ‘Taildness’.
return Gives the kurtosis value

Example

INPUT :kurtosis('/home/kshitij/rstudio-0.98.1103/bin/iris.csv',['Sepal.Length'])
OUTPUT:kurtosis of given columns

Sepal.Length kurtosis=  -0.552064








box-cox transformation

Functio Name  :boxcoxtrans
Details       :boxcoxtrans('file path',list of columns)
description  Box-Cox Power Transformations from Non-Normal to Normality
details Box-Cox transformation is usually applied in order to achieve modeling assumptions.  As stated earlier techniques such as Simple Linear Regression, Multiple Linear Regression, Logistic Regression and other Classification Techniques like Discriminant Analysis, DT, NN, etc., also requires data to be normally distributed.(E.g.) In ENERGY model building, the usage of ENERGY in any house, district or state will be right-skewed.  Using Box-Cox when the same is transformed into ‘NORMAL’ the assumption is met, at the same time after transformation that particular units will lose its original UNIT OF MEASUREMENT.


Example

INPUT :boxcoxtrans('/home/kshitij/rstudio-0.98.1103/bin/iris.csv',['Sepal.Length'])
OUTPUT:box-cox transformation of given columns
optimal lembda=0.2
            0
0    7.801137
1    7.801137
2    7.378459
3    7.801137
4    9.046807
5    7.682587

shapiro test=(0.9712131023406982, 0.5335444211959839)







poisson transformation

Functio Name : poitrans
Details      : poitrans('file path',list of columns)
Freeman Tukey Variance Stabilization transformation for POISSON DISTRIBUTION DATA
details This technique widely used to Stabilize Variance during model building.if the COUNT data follows Poisson Distribution, this transformation is then applied.
return Returns transformed column vector

Example

INPUT :poitrans('/home/kshitij/rstudio-0.98.1103/bin/iris.csv',['Sepal.Length'])
OUTPUT:poisson data transformation of given columns as numpy array

 [[10.51187112]
 [ 10.51187112]
 [  9.66950524]
 [ 10.51187112]
 [ 13.24762786]
 [ 10.27129045]]








proportional transformation

Function Name:proptrans
Details      :proptrans('file path',list of columns)
Freeman Tukey Arcsin Transformation For Proportions
This technique is widely used to Stabilize Variance during model building.The proportion should be arrived from a COUNT data only.It should not be applied under scenarios like where the Proportion is arrived from Continuous Data. Should not be applied for Profit Margins.
return Returns transformed column vector as numpy array 


Example

INPUT :proptrans('/home/kshitij/rstudio-0.98.1103/bin/iris.csv',['Sepal.Length'])
OUTPUT:proportion data transformation of given columns as numpy array

[[ 0.        ]
 [ 0.        ]
 [ 1.57079633]
 [ 1.57079633]
 [ 0.        ]
 [ 1.57079633]]














