import matplotlib.pyplot as plt

dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [45331, 75332, 95333, 75334, 65335, 75336, 85337, 75338, 35339, 25340, 75341]

# Plot the bar chart
plt.bar(dev_x, dev_y, color='k', linestyle='--', label="All Devs")

# Add markers on top of the bars
# plt.plot(dev_x, dev_y, marker='o', markersize=5, color='red')

plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")
plt.title('Media Salary (USD) by Age')
plt.legend(["All Dev's", "Markers on Bars"])
plt.grid(True)
plt.tight_layout()
plt.savefig('diagram.png')
plt.show()
