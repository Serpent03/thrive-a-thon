import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
from util_funcs import *
from talipp.indicators import EMA, SMA
import numpy as np

plt.style.use("bmh")
axes = plt.gca()
df = pd.read_csv("./oh.csv")

CONST_AVG_WINDOW = 4
CONST_POLY_DEGREE = 4
CONST_LINE_WIDTH = 1
CONST_ROW = 687

mnYearColumns = list(range(4, 40)) # 36 months
df_ptr = df.head(1000)[df.columns[mnYearColumns]]
mnYearColumns = list(range(1, 37)) # 36 months

rawData = getDataFromRow(df_ptr, CONST_ROW)
smaData = list(SMA(CONST_AVG_WINDOW, rawData))
CONST_SIZE_DIFFERENTIAL = 36 - len(smaData)
# smaData = [0,] * CONST_SIZE_DIFFERENTIAL + smaData
smaData = rawData[0 : CONST_SIZE_DIFFERENTIAL] + smaData

polyRegressionModel = np.poly1d(np.polyfit(mnYearColumns, smaData, CONST_POLY_DEGREE))
extrapolation = np.arange(1, 49)

plt.plot(mnYearColumns, rawData, linewidth=CONST_LINE_WIDTH, label="RAW_DATA")
plt.plot(mnYearColumns, smaData, linewidth=CONST_LINE_WIDTH, label="SMA_DATA")
plt.plot(extrapolation, polyRegressionModel(extrapolation), color='purple', linewidth=CONST_LINE_WIDTH, label="PREDICTION")

for i in range(24, 49): # from month 24 to month 48
    calc_y = polyRegressionModel(i)
    plt.scatter(i, calc_y, color='purple', linewidths=CONST_LINE_WIDTH)
    plt.text(i, calc_y+(calc_y / 10), s=f"{i}")

# plt.xlim([-5, 50])
# plt.ylim([-40, 300])
plt.xlabel("Months")
plt.ylabel("Unit demand")
plt.legend() 
plt.show()