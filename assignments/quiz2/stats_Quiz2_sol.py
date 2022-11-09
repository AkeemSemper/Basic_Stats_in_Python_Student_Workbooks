import thinkstats2
import pandas as pd
import numpy as np
import math
import scipy

#Check correlations
def multiCorr(df1, columnName1, columnName2, spearman=False):
    finalCorr = -999
    if spearman == True:
        finalCorr = thinkstats2.SpearmanCorr(df1[columnName1], df1[columnName2])
    if spearman == False:
        finalCorr = thinkstats2.Corr(df1[columnName1], df1[columnName2])
    return finalCorr
  
#Analytical distribution test. 
def passAnalytical(df1, columnName, threshold=.05):
    k, p = scipy.stats.normaltest(df1[columnName])
    fitted = False
    if fitted > threshold:
        fitted = True
    model = scipy.stats.norm(loc=df1[columnName].mean(), scale=df1[columnName].std())
    return fitted, model

#Rankskew
def rankSkew(df1, columnName1, columnName2, columnName3):
    skew1 = thinkstats2.PearsonMedianSkewness(df1[columnName1])
    skew2 = thinkstats2.PearsonMedianSkewness(df1[columnName2])
    skew3 = thinkstats2.PearsonMedianSkewness(df1[columnName3])
    #print(skew1, skew2, skew3)
    skewList = [(skew1, columnName1), (skew2, columnName2), (skew3, columnName3)]
    skewList.sort(key=lambda tup: tup[0])
    firstTmp = skewList[0]
    first = firstTmp[1]
    skew1 = firstTmp[0]
    secTmp = skewList[1]
    second = secTmp[1]
    skew1 = secTmp[0]
    thiTmp = skewList[2]
    third = thiTmp[1]
    skew1 = thiTmp[0]
    return first, skew1, second, skew2, third, skew3

def lognormOrNorm(df1, columnName):
    k1, pNorm = scipy.stats.normaltest(df1[columnName])
    k2, pLog = scipy.stats.normaltest(np.log(df1[columnName]))
    isLog = False
    if pNorm >= pLog:
        isLog = True
    #print(pNorm, pLog)
    return isLog