import random
from tkinter import *
from tkinter import ttk

from bubbleSort import bubble_sort
from insertionSort import insertion_sort
from mergeSort import merge_sort
from quickSort import quick_sort
from selectionSort import selection_sort

root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(900, 600)
root.config(bg='black')

selected_algo = StringVar()
data = []


def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalisedData = [i / max(data) for i in data]

    for i, height in enumerate(normalisedData):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0 + 2, y0, anchor='sw', text=str(data[i]))
    root.update_idletasks()


def generate():
    global data
    minValue = int(MinEntry.get())
    maxValue = int(MaxEntry.get())
    Size = int(sizeEntry.get())
    data = []
    for _ in range(Size):
        data.append(random.randrange(minValue, maxValue + 1))
    drawData(data, ['pink' for x in range(len(data))])


def startAlgorithm():
    global data
    if algMenu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data) - 1, drawData, speedScale.get())
        drawData(data, ['light blue' for c in range(len(data))])
    elif algMenu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, speedScale.get())
    elif algMenu.get() == 'Selection Sort':
        selection_sort(data, drawData, speedScale.get())
    elif algMenu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, speedScale.get())
    elif algMenu.get() == 'Merge Sort':
        merge_sort(data, drawData, speedScale.get())


UI_frame = Frame(root, width=600, height=200, bg='white')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='black')
canvas.grid(row=1, column=0, padx=10, pady=5)

Label(UI_frame, text='Algorithm: ', bg='black', fg='white').grid(row=0, column=0, padx=10, pady=5, sticky='w')
algMenu = ttk.Combobox(UI_frame, textvariable=selected_algo,
                       values=['Merge Sort', 'Bubble Sort', 'Quick Sort', 'Selection Sort', 'Insertion Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.2, to=5.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, bg='black',
                   fg='white', label="Select Speed [S]")
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text='Start', command=startAlgorithm, bg='black', fg='white').grid(row=0, column=3, padx=5, pady=5)

sizeEntry = Scale(UI_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, label="Data Size", bg='black', fg='white')
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

MinEntry = Scale(UI_frame, from_=1, to=10, resolution=1, orient=HORIZONTAL, label="Minimum Value", bg='black',
                 fg='white')
MinEntry.grid(row=1, column=1, padx=5, pady=5)

MaxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Maximum Value", bg='black',
                 fg='white')
MaxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text='Generate', command=generate, bg='black', fg='white').grid(row=1, column=3, padx=5, pady=5)

root.mainloop()
