import csv
from matplotlib import pyplot as plt
from datetime import datetime


filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs, lows, dates = [], [], []

    for row in reader:      #row到reader的内容，是怎么进行循环的？一行一行的读取然后换行的？为什么不是一列一列的读取？
       try:
          current_date = datetime.strptime(row[0], "%Y-%m-%d")
          low = int(row[3])
          high = int(row[1])
       except ValueError:
          print(current_date, 'missing data')
       else:
          lows.append(low)
          dates.append(current_date)
          highs.append(high)  #书里面的解释：阅读器对象从其停留的位置继续往下阅读csv文件，每次都自动返回当前位置所处的下一行。
                            # 和阅读器读取文档的方法有关？
    print(highs)
    print(dates)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title("Daily high and low temperatures 2014 death_valley_2014", fontsize=24)

plt.xlabel('', fontsize=16)
fig.autofmt_xdate()#倾斜日期标签

plt.ylabel('Temperature (F)', fontsize=16)

plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
