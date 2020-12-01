import matplotlib.pyplot as plt
import json
from urllib.request import urlopen

data = json.load(urlopen('https://www.cbr-xml-daily.ru/daily_json.js'))['Valute']

x = []
y = []

for i in data:
    x.append(i)
    y.append(data[i]['Value'])

plt.title('Курсы валют')
plt.grid()
plt.bar(x, y)
plt.xticks(rotation=90)
plt.show()
