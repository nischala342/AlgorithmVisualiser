import time


def merge_sort(data, drawData, timeTick):
    merge_sort_algo(data, 0, len(data) - 1, drawData, timeTick)


def merge_sort_algo(data, left, right, drawData, timeTick):
    if left < right:
        middle = (left + right) // 2
        merge_sort_algo(data, left, middle, drawData, timeTick)
        merge_sort_algo(data, middle + 1, right, drawData, timeTick)
        merge(data, left, middle, right, drawData, timeTick)


def merge(data, left, middle, right, drawData, timeTick):
    drawData(data, getColorArray(len(data), left, middle, right))
    time.sleep(timeTick)
    left_half = data[left:middle + 1]
    right_half = data[middle + 1: right + 1]
    left_index = right_index = 0
    for dataIdx in range(left, right + 1):
        if left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] <= right_half[right_index]:
                data[dataIdx] = left_half[left_index]
                left_index += 1
            else:
                data[dataIdx] = right_half[right_index]
                right_index += 1
        elif left_index < len(left_half):
            data[dataIdx] = left_half[left_index]
            left_index += 1
        else:
            data[dataIdx] = right_half[right_index]
            right_index += 1
    drawData(data, ["pink" if x < left or x > right else "light blue" for x in range(len(data))])
    time.sleep(timeTick)


def getColorArray(leght, left, middle, right):
    colorArray = []
    for i in range(leght):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append("medium purple")
            else:
                colorArray.append("turquoise1")
        else:
            colorArray.append("pink")
    return colorArray
