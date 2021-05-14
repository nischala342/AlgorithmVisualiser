import time

def insertion_sort(data,drawData, timeTick):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        drawData(data,['light blue' if x == i else 'pink' for x in range(len(data)) ])
        time.sleep(timeTick)
    drawData(data,['light blue' for x in range(len(data))])