import csv
with open("MMMGraph.csv", newline='')as f:
    reader = csv.reader(f)
    filedata = list(reader)
filedata.pop(0)
height = []
for i in range (len(filedata)):
    num = filedata[i][1]
    height.append(float(num))

n = len(height)
height.sort()
print(n)
if n %2==0:
    median1 = float(height[n//2])
    median2 = float(height[n//2-1])
    median = (median1+median2)/2
else:
    median = height[n//2]
print("median of the data is ", median)

