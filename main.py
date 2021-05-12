import random
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(900, 600)
root.config(bg='black')

selected_algo = StringVar()


def drawData(data):
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

        canvas.create_rectangle(x0, y0, x1, y1, fill='pink')
        canvas.create_text(x0 + 2, y0, anchor='sw', text=str(data[i]))


def generate():
    print("ALgo selected: " + selected_algo.get())
    try:
        minValue = int(MinEntry.get())
    except:
        minValue = 5
    try:
        maxValue = int(MaxEntry.get())
    except:
        maxValue = 1000
    try:
        Size = int(sizeEntry.get())
    except:
        Size = 15
    if minValue < 0:
        minValue = 5
    if maxValue < 0:
        maxValue = 1000
    if Size < 0:
        Size = 10
    data = []
    for _ in range(Size):
        data.append(random.randrange(minValue, maxValue + 1))

    drawData(data)


UI_frame = Frame(root, width=600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

Label(UI_frame, text='Algorithm: ', bg='grey').grid(row=0, column=0, padx=10, pady=5, sticky='w')
algMenu = ttk.Combobox(UI_frame, textvariable=selected_algo, values=['Merge Sort', 'Bubble Sort'])
algMenu.grid(row=0, column=0, padx=5, pady=5)
algMenu.current(0)
Button(UI_frame, text='Generate', command=generate, bg='red').grid(row=0, column=2, padx=5, pady=5)

Label(UI_frame, text='Size: ', bg='grey').grid(row=1, column=0, padx=10, pady=5, sticky='w')
sizeEntry = Entry(UI_frame)
sizeEntry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

Label(UI_frame, text='Min Length: ', bg='grey').grid(row=1, column=2, padx=10, pady=5, sticky='w')
MinEntry = Entry(UI_frame)
MinEntry.grid(row=1, column=3, padx=5, pady=5, sticky='w')

Label(UI_frame, text='Max Length: ', bg='grey').grid(row=1, column=4, padx=10, pady=5, sticky='w')
MaxEntry = Entry(UI_frame)
MaxEntry.grid(row=1, column=5, padx=5, pady=5, sticky='w')

root.mainloop()
