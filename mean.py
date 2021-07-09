import csv
with open('MMMGraph.csv',newline='')as f:
    reader=csv.reader(f)
    filedata = list(reader)
filedata.pop(0)
height = []
for i in range(len(filedata)):
    num = filedata[i][1]
    height.append(float(num))

n = len(height)
total = 0
for x in height:
    total = total+x
mean = total/n
print("the mean of the height is", mean)