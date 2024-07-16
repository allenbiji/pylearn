import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd

data=pd.read_csv("1.01.+Simple+linear+regression.csv")

y=data["GPA"]
x1=data["SAT"]

