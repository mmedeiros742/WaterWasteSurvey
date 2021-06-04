#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 12:43:41 2020

@author: ericbotelho
"""

import pandas as pd
import seaborn as sns 

sns.set(rc={'figure.figsize':(11.7,8.27)})

excel_file = (r'/Users/ericbotelho/Downloads/SurveyResponsesCoded.xlsx')
ABS = pd.read_excel(excel_file)

boxplot = sns.boxplot(x=ABS["How long would you say your average shower is in minutes?"])


plot_file_name = "Boxplot.jpg"
boxplot.figure.savefig(plot_file_name, format= "jpeg", dpi = 100)