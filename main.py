import matplotlib.pyplot as plt
import pandas as pd

mh = pd.read_csv('./data/raw/messy_housing_data.csv')

from src.report import data_quality_report

report = data_quality_report(mh)
print(report)

mh.plot(kind="scatter", x="area_sqft", y="price")
#plt.tight_layout()
plt.show()

