import PySimpleGUI as sg
import Sort as s
import numpy as np
import time


def generate_array(dim, range_n):
    return np.random.randint(range_n, size=dim)


def sort(alg):
    array = generate_array(dim, range_n)
    start = time.time()
    alg(array)
    end = time.time()
    return end - start


def add_to_table(value):
    window['-TABLE-'].update(values=table_values)
    window.refresh()


s = s.Sort()

layout = [[sg.Text('Number of elements'), sg.InputText()],
          [sg.Text('Range'), sg.InputText()],
          [sg.Checkbox('Insertion Sort', size=(40, 1))],
          [sg.Checkbox('Merge Sort')],
          [sg.Checkbox('Quick Sort')],
          [sg.Checkbox('Rand quick Sort')],
          [sg.Checkbox('Iterative quick Sort')],
          [sg.Checkbox('Heap Sort')],
          [sg.Checkbox('Counting Sort')],
          [sg.Checkbox('Radix Sort')],
          [sg.Checkbox('Bucket Sort')],
          [sg.Button('Order')]]
# add a table for display results
layout += [[sg.Table(values=[[]], headings=['Algorithm', 'Time'],
                     max_col_width=25,
                     auto_size_columns=True,
                     display_row_numbers=False,
                     justification='right',
                     num_rows=10,
                     expand_x=True,
                     expand_y=True,
                     key='-TABLE-',
                     size=(500, 500),
                     col_widths=[20, 20],
                     row_height=35)]]


window = sg.Window('Window Title', layout, resizable=True, finalize=True)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Order':
        dim = int(values[0])
        range_n = int(values[1])
        table_values = []

        # remove elements from table
        window['-TABLE-'].update(values=[])
        # refresh window
        window.refresh()

        if values[2]:
            table_values.append(['Insertion Sort', sort(s.insertion_sort)])
            add_to_table(table_values)
        if values[3]:
            table_values.append(['Merge Sort', sort(s.merge_sort)])
            add_to_table(table_values)
        if values[4]:
            table_values.append(['Quick Sort', sort(s.quick_sort)])
            add_to_table(table_values)
        if values[5]:
            table_values.append(['Rand quick Sort', sort(s.rand_quick_sort)])
            add_to_table(table_values)
        if values[6]:
            table_values.append(
                ['Iterative quick Sort', sort(s.iterative_quick_sort)])
            add_to_table(table_values)
        if values[7]:
            table_values.append(['Heap Sort', sort(s.heap_sort)])
            add_to_table(table_values)
        if values[8]:
            table_values.append(['Counting Sort', sort(s.counting_sort)])
            add_to_table(table_values)
        if values[9]:
            table_values.append(['Radix Sort', sort(s.radix_sort)])
            add_to_table(table_values)
        if values[10]:
            table_values.append(['Bucket Sort', sort(s.bucket_sort)])
            add_to_table(table_values)


window.close()
