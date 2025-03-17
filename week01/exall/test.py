import numpy
import pandas
import matplotlib.pyplot as plt

db = pandas.read_csv("../Housing.csv")
db = db.dropna()
db = db.drop_duplicates()
plt.boxplot(db["price"])
plt.show()