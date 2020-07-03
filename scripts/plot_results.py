#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jesse
"""

import matplotlib.pyplot as plt
import pandas as pd

foldername = "/home/jesse/Documents/Github/garage/examples/tf/data/local/experiment/"
filename = "osimArm_20/progress.csv"

data = pd.read_csv(foldername+filename).to_dict(orient="list")

for key in data:
    if key == "Epoch":
        continue
    plt.plot(data["Epoch"], data[key])
    plt.title(key + " from " + filename)
    plt.xlabel("Epoch")
    plt.ylabel(key)
    plt.show()
