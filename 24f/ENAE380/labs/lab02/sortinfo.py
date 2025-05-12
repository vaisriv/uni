import pandas as pd

sorts = pd.read_csv("SortingTests.csv")
averages = sorts.mean()

print(averages)
