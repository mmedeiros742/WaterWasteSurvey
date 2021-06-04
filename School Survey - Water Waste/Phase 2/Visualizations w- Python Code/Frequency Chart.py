#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 13:56:50 2020

@author: ericbotelho
"""

import pandas as pd
import matplotlib.pyplot as plt


excel_file = (r'/Users/ericbotelho/Downloads/SurveyResponsesCoded.xlsx')
ABS = pd.read_excel(excel_file)

fchart = ABS["On average how many showers would you say you take a week?"].hist(label = "Average Showers in a Week", width = 1, ec = "black")
plt.xlabel("Average showers in a Week")
plt.ylabel("Frequency")
plt.title("Frequency Chart")
plot_file_name = "Frequency Chart.jpg"
fchart.figure.savefig(plot_file_name, format= "jpeg", dpi = 100)