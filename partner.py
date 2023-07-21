import matplotlib.pyplot as plt
import numpy as np
import csv
from collections import Counter

import pandas as pd

plt.style.use('seaborn-v0_8')
data = pd.read_csv('G:\File store\data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']
language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

languages = list(language_counter.keys())
popularity = list(language_counter.values())

plt.bar(languages, popularity)

plt.xlabel("Most popular programming languages")
# plt.ylabel("Popularity")
plt.title('Most Popular Programming Languages')
plt.xticks(rotation=90)
# plt.tight_layout()
# plt.savefig('diagram.png')
plt.show()

