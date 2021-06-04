#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 17:29:50 2020

@author: ericbotelho
"""

import pandas as pd
import matplotlib.pyplot as plt

excel_file = (r'/Users/ericbotelho/Downloads/SurveyResponsesCoded.xlsx')
ABS = pd.read_excel(excel_file)

Male = ABS[(ABS['What gender you most identify with?'] == True)]['How long would you say your average shower is in minutes?'].sum()
Female = ABS[(ABS['What gender you most identify with?'] == False)]['How long would you say your average shower is in minutes?'].sum()


labels = ["Male", "Female"]
sizes = [Male, Female]
explode = (0.01, 0)
colors = ['#ff9999','#66b3ff']
 

fig1, ax1 = plt.subplots()
piechart = ax1.pie(sizes, explode = explode, labels = labels, colors = colors, autopct='%1.1f%%')

ax1.set_title("Male vs Female, Time Spent Showering")        
plt.savefig("PieChart.png")