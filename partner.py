import matplotlib.pyplot as plt
import numpy as np

dev_x=[25,26,27,28,29,30,31,32,33,34,35]
dev_y=[45331,75332,95333,75334,65335,75336,85337,75338,35339,25340,75341]
plt.plot(dev_x,dev_y,'k--',label="All Devs")

py_dev_x=[25,26,27,28,29,30,31,32,33,34,35]
py_dev_y=[456541,456542,456543,456544,456545,456546,456547,456548,456549,456550,456551]
plt.plot(dev_x,py_dev_y,'k--',label="Python")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")
plt.title('Media Salary (USD) by Age')
plt.legend(["All Dev's","Python"])
plt.show()