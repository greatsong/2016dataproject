import csv
data = csv.reader(open('201605subway.csv','r'), delimiter=",")

max_person1 = [0] * 24
max_station1 = [''] * 24

max_person2 = [0] * 24
max_station2 = [''] * 24
for row in data :
    for i in range(24):
        if int(max_person1[i]) < int(row[2+(i*2)]) :
            max_person1[i] = row[2+(i*2)]
            max_station1[i] = row[1] + '/' + str(i+4) #+'('+ row[0]+')'
        if int(max_person2[i]) < int(row[3 + (i * 2)]):
            max_person2[i] = row[3 + (i * 2)]
            max_station2[i] = row[1] + '/' + str(i + 4)  # +'('+ row[0]+')'

for i in range(24):
    print(i+4,'시(승차): ', max_station1[i],'/',max_person1[i])
    print(i + 4,'시(하차): ', max_station2[i], '/', max_person2[i])

import matplotlib.pyplot as plt
import numpy as np
plt.rc('font',family='Malgun Gothic')
cnt = np.arange(24)
plt.subplot(121)
plt.title('2016년 5월 서울시 지하철 시간대별 최다 승차역')
plt.plot(cnt, max_person1,'r')
plt.xticks(cnt, max_station1,rotation='vertical')
plt.ylim(ymax=500000)
plt.subplot(122)
plt.title('2016년 5월 서울시 지하철 시간대별 최다 하차역')
plt.plot(cnt, max_person2,'b')
plt.xticks(cnt, max_station2,rotation='vertical')
plt.ylim(ymax=500000)
plt.show()