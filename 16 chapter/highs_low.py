import csv
from matplotlib import pyplot as plt

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs = []
    for row in reader:      #row到reader的内容，是怎么进行循环的？一行一行的读取然后换行的？为什么不是一列一列的读取？
        high = int(row[1])
        highs.append(high)  #书里面的解释：阅读器对象从其停留的位置继续往下阅读csv文件，每次都自动返回当前位置所处的下一行。
                            # 和阅读器读取文档的方法有关？
    print(highs)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
