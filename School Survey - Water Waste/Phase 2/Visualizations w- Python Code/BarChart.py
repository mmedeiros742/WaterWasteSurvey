#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:00:55 2020

@author: ericbotelho
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

excel_file = (r'/Users/ericbotelho/Downloads/SurveyResponsesCoded.xlsx')
ABS = pd.read_excel(excel_file)

FreshmenRes = ABS[(ABS['Are you a Resident (1) or Commuter (0)?'] == True) & (ABS['What year of school are you in?'] == 1)]['How long would you say your average shower is in minutes?'].mean()
SophmoreRes = ABS[(ABS['Are you a Resident (1) or Commuter (0)?'] == True) & (ABS['What year of school are you in?'] == 2)]['How long would you say your average shower is in minutes?'].mean()
JuniorRes = ABS[(ABS['Are you a Resident (1) or Commuter (0)?'] == True) & (ABS['What year of school are you in?'] == 3)]['How long would you say your average shower is in minutes?'].mean()
SeniorRes = ABS[(ABS['Are you a Resident (1) or Commuter (0)?'] == True) & (ABS['What year of school are you in?'] == 4)]['How long would you say your average shower is in minutes?'].mean()
GradRes = ABS[(ABS['Are you a Resident (1) or Commuter (0)?'] == True) & (ABS['What year of school are you in?'] == 5)]['How long would you say your average shower is in minutes?'].mean()


height = [FreshmenRes, SophmoreRes, JuniorRes, SeniorRes, GradRes]
bars = ["Freshmen", "Sophomores", "Juniors", "Seniors", "Grad Students"]

y_pos = np.arange(len(bars))
plt.xticks(y_pos, bars)

barplot = plt.bar(y_pos, height, ec = "black")

plt.xlabel("Year")
plt.ylabel("Average Time Spent Showering (minutes)")
plt.title("Average Resident Time Spent Showering")

plot_file_name = "Average Resident Time Spent Showering.jpg"
plt.savefig(plot_file_name, format= "jpeg", dpi = 100)