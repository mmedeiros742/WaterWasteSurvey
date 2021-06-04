#CIS361 - HW1 source code
#Modified for Project 1 Phase 2

#necessary packages
import numpy as np
import pandas as pd
from scipy.stats import skew


def calculations(data):
    #mean
    try:
        val_mean = np.mean(data)
        print("\tMean: %.3f" %(val_mean))
    except:
        print("\tCannot calculate mean.")

    #median
    try:
        val_median = np.median(data)
        print("\tMedian: %.3f" %(val_median))
    except:
        print("\tCannot calculate median.")

    #standard deviation
    try:
        val_std = np.std(data)
        print("\tStandard Deviation: %.3f" %(val_std))
    except:
        print("\tCannot calculate standard deviation.")

    #variance
    try:
        val_var = np.var(data)
        print("\tVariance: %.3f" %(val_var))
    except:
        print("\tCannot calculate variance.")

    #range
    try:
        val_min = np.min(data)
        val_max = np.max(data)
        val_range = val_max - val_min
        print("\tRange: %.3f" %(val_range))
        print("\t\tMin: %.3f" %(val_min))
        print("\t\tMax: %.3f" %(val_max))
    except:
        print("\tCannot calculate min, max, or range.")

    #skewness
    try:
        val_skew = skew(data)
        print("\tSkewness: %.3f" %(val_skew))
    except:
        print("\tCannot calculate skewness.")

    #quartiles
    try:
        q1 = np.percentile(data, 25)
        q2 = np.percentile(data, 50)
        q3 = np.percentile(data, 75)
        print("\tQuartiles:")
        print("\t\tQ1: %d" %(q1))
        print("\t\tQ2: %d" %(q2))
        print("\t\tQ3: %d" %(q3))
    except:
        print("\tCannot calculate quartiles.")

    #outliers
    try:
        outliers = []
        #following code adapted from https://medium.com/datadriveninvestor/finding-outliers-in-dataset-using-python-efc3fce6ce32
        for x in data:
            z_score = (x - val_mean) / val_std
            if(np.abs(z_score) > 3):
                outliers.append(x)
        ########################################################################################################################
        if(len(outliers) == 0):
            print("\tOutliers: none")
        else:
            print "\tOutliers:", outliers
    except:
        print("\tCannot calculate outliers.")

def correlation(col, data, target):
    try:
        c = np.corrcoef(data, target)
        print ("\t%s vs Average Shower Time = %f" %(col, c[0,1]))
    except:
        print("\tCannot calculate correlation.")

###MAIN###
#take in data from excel file
infile = pd.read_excel('Survey Responses.xlsx')

target = infile[:98]["How long would you say your average shower is in minutes?"]

for col in infile:
    print(col)
    data = infile[:98][col]
    calculations(data)
    correlation(col, data, target)
    print("\n")
