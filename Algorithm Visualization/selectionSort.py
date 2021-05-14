import time

def selection_sort(data,drawData, timeTick):
    for i in range(len(data)):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[min_index] > data[j]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
        drawData(data,['light blue' if x == i or x == min_index else 'pink' for x in range(len(data)) ])
        time.sleep(timeTick)
    drawData(data,['light blue' for x in range(len(data))])
