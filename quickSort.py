import time
def partition(data, low, high,drawData,timeTrick):
	border = low
	pivot = data[high]
	drawData(data,getColorArray(len(data), low,high,border,border))
	time.sleep(timeTrick)

	for j in range(low, high):
		if data[j] < pivot:
			drawData(data, getColorArray(len(data), low, high, border, j,True))
			time.sleep(timeTrick)
			data[border], data[j] = data[j], data[border]
			border += 1
		drawData(data, getColorArray(len(data), low, high, border, j))
		time.sleep(timeTrick)
	data[border], data[high] = data[high], data[border]

	drawData(data, getColorArray(len(data), low, high, border, high, True))
	time.sleep(timeTrick)
	return border
def quick_sort(data, low, high,drawData, timeTrick):
	if len(data) == 1:
		return data
	if low < high:
		pi = partition(data, low, high,drawData, timeTrick)
		quick_sort(data, low, pi-1,drawData,timeTrick)
		quick_sort(data, pi+1, high,drawData,timeTrick)

def getColorArray(datalen,low,high,i,currentindex,isSwapping = False):
	colorArray = []
	for j in range(datalen):
		if j >= low and j <= high:
			colorArray.append('grey')
		else:
			colorArray.append('white')
		if j == high:
			colorArray[j] = 'blue'
		elif j == i:
			colorArray[j] = 'red'
		elif j == currentindex:
			colorArray[j] = 'yellow'

		if isSwapping:
			if j == i or j == currentindex:
				colorArray[j] = 'green'
	return colorArray





