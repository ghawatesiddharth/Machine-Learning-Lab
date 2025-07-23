import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('used_cars_data.csv')

print(data.head(5))
print(data.tail(5))
print(data.info())