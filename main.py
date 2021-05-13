import random
from tkinter import *
from tkinter import ttk
from bubbleSort import bubble_sort

root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(900, 600)
root.config(bg='black')

selected_algo = StringVar()
data = []

def drawData(data,colorArray):
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
    drawData(data,['pink' for x in range(len(data))])
def startAlgorithm():
    global data
    bubble_sort(data,drawData,speedScale.get())


UI_frame = Frame(root, width=600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

Label(UI_frame, text='Algorithm: ', bg='grey').grid(row=0, column=0, padx=10, pady=5, sticky='w')
algMenu = ttk.Combobox(UI_frame, textvariable=selected_algo, values=['Merge Sort', 'Bubble Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.1, to=2.0,length = 200, digits=2, resolution = 0.2, orient=HORIZONTAL,label = "Select Speed [S]")
speedScale.grid(row=0,column=2,padx=5,pady=5)
Button(UI_frame, text='Start', command=startAlgorithm, bg='grey').grid(row=0, column=3, padx=5, pady=5)


sizeEntry = Scale(UI_frame, from_=3, to=25,resolution = 1, orient=HORIZONTAL,label = "Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

MinEntry = Scale(UI_frame, from_=1, to=10,resolution = 1, orient=HORIZONTAL,label = "Minimum Value")
MinEntry.grid(row=1, column=1, padx=5, pady=5)

MaxEntry = Scale(UI_frame, from_=10, to=100,resolution = 1, orient=HORIZONTAL,label = "Maximum Value")
MaxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text='Generate', command=generate, bg='grey').grid(row=1, column=3, padx=5, pady=5)

root.mainloop()
