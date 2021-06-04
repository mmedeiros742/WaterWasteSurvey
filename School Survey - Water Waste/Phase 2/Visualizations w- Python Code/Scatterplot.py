#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 17:12:15 2020

@author: ericbotelho
"""

import pandas as pd
import matplotlib.pyplot as plt

excel_file = (r'/Users/ericbotelho/Downloads/SurveyResponsesCoded.xlsx')
ABS = pd.read_excel(excel_file)

scatterplot = plt.scatter(x = ABS["On average how many showers would you say you take a week?"], y = ABS["How long would you say your average shower is in minutes?"])

plt.xlabel("Shower per Week")
plt.ylabel("Time Spent Showering (minutes)")
plt.title("Time Spent Showering vs Showers per Week")

plot_file_name = "Scatterplot.jpg"
scatterplot.figure.savefig(plot_file_name, format= "jpeg", dpi = 100)
