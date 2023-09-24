from tkinter import *
from tkinter.ttk import *
import random
import _thread
import time

delay = 0.001


def draw_lines(cvs):
    number = []
    line_id = []
    for i in range(0, 100):
        num = random.randint(10, 200)
        number.append(num)
        l_id = cvs.create_line(0, 3 * i, num, 3 * i, fill='red')
        line_id.append(l_id)
    return number, line_id


def bubble_sort(cvs, A, line_id):
    n = len(A) - 1
    for i in range(n):
        for j in range(0, n - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]

                cvs.move(line_id[j], 0, 3)
                cvs.move(line_id[j + 1], 0, -3)
                cvs.update()
                line_id[j], line_id[j + 1] = line_id[j + 1], line_id[j]
                time.sleep(delay)
    return A


def selection_sort(cvs, A, line_id):
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            if A[j] < A[i]:
                A[i], A[j] = A[j], A[i]

                cvs.move(line_id[i], 0, 3 * (j - i))
                cvs.move(line_id[j], 0, -3 * (j - i))
                cvs.update()
                line_id[i], line_id[j] = line_id[j], line_id[i]
                time.sleep(delay)
    return A


def shell_sort(cvs, A, line_id):
    n = len(A)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            while i >= gap and A[i - gap] > A[i]:
                A[i - gap], A[i] = A[i], A[i - gap]

                cvs.move(line_id[i - gap], 0, 3 * gap)
                cvs.move(line_id[i], 0, -3 * gap)
                cvs.update()
                line_id[i], line_id[i - gap] = line_id[i - gap], line_id[i]
                time.sleep(delay)
                i -= gap
        gap //= 2
    return A


def start_sort():
    try:
        _thread.start_new_thread(bubble_sort, (canvas1, num1, num_id1,))
        _thread.start_new_thread(selection_sort, (canvas2, num2, num_id2,))
        _thread.start_new_thread(shell_sort, (canvas3, num3, num_id3,))
    except:
        print("Error: 无法启动线程")


def init_canvas():
    canvas1.delete("all")
    canvas2.delete("all")
    canvas3.delete("all")

    global num1
    global num2
    global num3
    global num_id1
    global num_id2
    global num_id3

    num1, num_id1 = draw_lines(canvas1)
    num2, num_id2 = draw_lines(canvas2)
    num3, num_id3 = draw_lines(canvas3)


root = Tk()
pw = PanedWindow(orient=HORIZONTAL)
left_fame = Labelframe(pw, text="冒泡排序", width=200, height=400)
pw.add(left_fame, weight=1)
middle_fame = Labelframe(pw, text="选择排序", width=200)
pw.add(middle_fame, weight=1)
right_fame = Labelframe(pw, text="希尔排序", width=200)
pw.add(right_fame, weight=1)
pw.pack(fill=BOTH, expand=True, padx=10, pady=10)

canvas1 = Canvas(left_fame, width=200, height=350)
canvas1.pack()
canvas2 = Canvas(middle_fame, width=200, height=350)
canvas2.pack()
canvas3 = Canvas(right_fame, width=200, height=350)
canvas3.pack()

num1, num_id1 = draw_lines(canvas1)
num2, num_id2 = draw_lines(canvas2)
num3, num_id3 = draw_lines(canvas3)

btn1 = Button(root, text='开始排序', command=start_sort)
btn2 = Button(root, text='初始化画布数据', command=init_canvas)
btn1.pack()
btn2.pack()

root.mainloop()
