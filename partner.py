import matplotlib.pyplot as plt
import numpy as np
import csv
from collections import Counter

plt.style.use('seaborn-v0_8')
with open('G:\File store\data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    language_counter = Counter()
    for row in csv_reader:
        languages = row['LanguagesWorkedWith'].split(':')
        language_counter.update(languages)

languages = list(language_counter.keys())
popularity = list(language_counter.values())

plt.bar(languages, popularity)

plt.xlabel("Most popular programming languages")
plt.ylabel("Popularity")
plt.title('Most Popular Programming Languages')
plt.xticks(rotation=90)
# plt.tight_layout()
# plt.savefig('diagram.png')
plt.show()

