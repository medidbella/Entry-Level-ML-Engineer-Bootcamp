import numpy
import pandas
import matplotlib.pyplot as plt
import seaborn as sbrn

db = pandas.read_csv("../Housing.csv")
db = db.dropna()
db = db.drop_duplicates()

# for field in db.columns:
#     if field == "price":
#         continue
#     plt.title("price in relation to " + field)
#     plt.scatter(db["price"], db[field])
#     plt.show()

sbrn.heatmap([db["price"] [db["stories"]]])
plt.show()
