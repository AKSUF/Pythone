import matplotlib.pyplot as plt

print(plt.style.available)
plt.style.use('_classic_test_patch')
slices = [120, 80, 30, 20, 40]
labels = ['Sixty', 'Forty', 'Sixty', 'Thirty', 'Java']
explode = [0, 0, 0, 0.5, 0]
colors = ['blue', 'red', 'yellow', 'green', 'cyan']

plt.pie(slices, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90, colors=colors, wedgeprops={'edgecolor': 'black'})
plt.title("My awesome")
plt.tight_layout()
plt.show()


