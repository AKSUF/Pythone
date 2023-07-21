import matplotlib.pyplot as plt
import numpy as np
print(plt.style.available)
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
x_indexes = np.arange(len(dev_x))
width = 0.25
dev_y = [45331, 75332, 95333, 75334, 65335, 75336, 85337, 75338, 35339, 25340, 75341]
py_dev_y = [456541, 456542, 456543, 456544, 456545, 456546, 456547, 456548, 456549, 456550, 456551]
js_dev_y = [156541, 256542, 356543, 956544, 156545, 356546, 856547, 356548, 756549, 956550, 356551]

# Plot the bar chart for "All Devs"
plt.bar(x_indexes - width, dev_y, color='k', linestyle='--', label="All Devs", width=width)

# Plot markers on top of the bars for "All Devs"
plt.plot(x_indexes - width + width / 2, dev_y, marker='o', markersize=5, color='red')

# Plot the bar chart for "Python"
plt.bar(x_indexes, py_dev_y, color='b', label="Python", width=width)

# Plot markers on top of the bars for "Python"
plt.plot(x_indexes + width / 2, py_dev_y, marker='o', markersize=5, color='blue')

# Plot the bar chart for "Javascript"
plt.bar(x_indexes + width, js_dev_y, color='r', label="Javascript", width=width)

# Plot markers on top of the bars for "Javascript"
plt.plot(x_indexes + width + width / 2, js_dev_y, marker='o', markersize=5, color='green')

plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")
plt.title('Media Salary (USD) by Age')
plt.legend()
plt.xticks(ticks=x_indexes,labels=x_indexes)
plt.grid(True)
plt.tight_layout()
plt.savefig('diagram.png')
plt.show()
