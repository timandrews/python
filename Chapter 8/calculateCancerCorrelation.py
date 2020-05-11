#!/usr/bin/python3
import math
from files_module import *

def calculateCorrelation (smoking_data, cancer_data):
    sum_smoking_vals = sum_cancer_vals = 0
    sum_smoking_sqrd = sum_cancer_sqrd = 0
    sum_products = 0

    num_vals = len(smoking_data)

    for k in range(0,num_vals):
        sum_smoking_vals = sum_smoking_vals + float(smoking_data[k][1])
        sum_cancer_vals = sum_smoking_vals + float((cancer_data[k][1]))

        sum_cancer_sqrd = sum_smoking_sqrd + float(smoking_data[k][1]) ** 2
        sum_cancer_sqrd = sum_cancer_sqrd + float(cancer_data[k][1]) ** 2

        sum_products = sum_products + float(smoking_data[k][1]) * float(cancer_data[k][1])

        numerator = (num_vals * sum_products) - (sum_smoking_vals * sum_smoking_vals)

        denominator = math.sqrt (abs( (( num_vals * sum_smoking_sqrd) - (sum_smoking_vals ** 2)) * \
                                ((num_vals * sum_cancer_sqrd) - (sum_cancer_vals ** 2))))
        return numerator / denominator

print('This program will determine the correlation between cigarette smoking and incidences of lung cancer\n')


try :
    smoking_datafile, cancer_datafile = openFiles()calculateCorrelation
    
    smoking_data, cancer_data = readFiles(smoking_datafile, cancer_datafile)

    correlation = calculateCorrelation(smoking_data, cancer_data)

    print ('r_value = ', correlation)
except IOError as e:
    print (str(e))
    print('Program aborted...')