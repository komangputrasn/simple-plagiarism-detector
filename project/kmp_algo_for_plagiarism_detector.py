# langkah 1: masukan file yang akan dibandingkan. ada pattern, file yang akan diamati dan ada file text, file yang akan dibandingkan
# langkah 2: pecah/split semua kalimat di file pattern dengan tanda titik sebagai pemisah
# langkah 3: simpan semua kalimat yang dipecah dalam suatu array
# langkah 4: untuk semua kalimat yang ada di array, periksa apakah dapat ditemukan dalam file text menggunakan algoritma KMP
# langkah 5: hitung presentase kalimat yang plagiat dengan rumus = % plagiat = (# kalimat plagiat / # kalimat dalam pattern) * 100

# sentences_in_file1 = docx2txt.process("text1.docx").split('.')
# file2text = docx2txt.process("text2.docx")

# plagiarized_sentences = []

# for sentence in sentences_in_file1:
#     if sentence in file2text:
#         plagiarized_sentences.append(sentence)

# if len(plagiarized_sentences):
#     plagiarized_sentences.pop()

# print(f'There are {len(plagiarized_sentences)} sentences plagiarized.')

# print(plagiarized_s entences)
    

from kmp_algorithm import *

from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter import messagebox
import tkinter.scrolledtext as st

import docx2txt

source_dir = ""
compare_dir = ""
plagiarized_sentences = []

MAIN_WINDOW_SIZE = "400x300"

    
def check_plagiarism():
    # split the sentences into array with the full stop as the delimiter
    sentences_in_source = docx2txt.process(source_dir).split('.')
    compare_text = docx2txt.process(compare_dir)

    # remove the last empty sentence in the array pyth
    try:
        sentences_in_source.pop()
    except Exception:
        messagebox.showerror("Error", "One document is empty")
    
    for sentence in sentences_in_source:
        print(sentence)
        if KMP_search(compare_text, sentence) != -1:
        # if sentence in compare_text:
            plagiarized_sentences.append(sentence)


def get_source_dir():
    # want to modify the global variable, use the 'global' keyword
    global source_dir 
    source_dir = askopenfilename(filetypes=[('Microsoft Word', '*.docx')])
    print(source_dir)

def get_compare_dir():
    global compare_dir 
    compare_dir = askopenfilename(filetypes=[('Microsoft Word', '*.docx')])
    print(compare_dir)

def check_result(root):
    global source_dir, compare_dir
    if len(source_dir) and len(compare_dir):
        check_plagiarism()
        open_result_window(root)
    else:
        messagebox.showerror("Error", "You need to select the source file and the file you want to compare!")

def return_to_main_window(window):
    window.destroy()
    main_window()

def open_result_window(root):
    root.destroy()
    result_window = Tk()
    result_window.title('Simple Plagiarism Detector')
    result_window.geometry(MAIN_WINDOW_SIZE)

    source_file_path = Label(result_window, text=f"Source file: {source_dir.split('/')[-1]}", justify=LEFT)
    source_file_path.pack(side=TOP)

    compare_file_path = Label(result_window, text=f"File to compare: {compare_dir.split('/')[-1]}", justify=LEFT)
    compare_file_path.pack(side=TOP)

    plagiarized_amount_label = Label(result_window, text=f"Total sentences plagiarized: {len(plagiarized_sentences)}", justify=LEFT)
    plagiarized_amount_label.pack(side=TOP)

    plagiarized_text_label = Label(result_window, text=f"These are the plagiarized sentences found in both file", justify=LEFT)
    plagiarized_text_label.pack(side=TOP)

    plagiarized_text = st.ScrolledText(result_window,
                            width = 40, 
                            height = 8, 
                            font = ("Arial",
                                    12))
    
    for s in plagiarized_sentences:
        plagiarized_text.insert(INSERT, s + '\n\n')

    plagiarized_text.pack(side=TOP, pady=10)
    plagiarized_text.configure(state='disabled')
    
    return_button =  Button(result_window, text='Return to Main Menu', command=lambda:return_to_main_window(result_window))
    return_button.pack(side=BOTTOM, pady=5)

    result_window.mainloop()

def main_window():
    # root window
    root = Tk()
    root.title("Simple Plagiarism Detector")
    root.geometry(MAIN_WINDOW_SIZE)

    description = Label(root, text="Detecting plagiarism in two files\nwith the help of Knuth-Morris-Pratt algorithm.\nDeveloped by Fairo, Ihsan, Komang, and Rafi.", justify=CENTER)
    description.place(x=200, y=50, anchor="center")

    # buttons and getting the file's directory
    select_file_source_btn = Button(root, text='Select Source File', command=lambda:get_source_dir())
    select_file_source_btn.pack(side=BOTTOM, pady=20)

    select_file_compare_btn = Button(root, text='Select File To Compare', command=lambda:get_compare_dir())
    select_file_compare_btn.pack(side=BOTTOM)

    check_result_btn = Button(root, text='Check Result', command=lambda:check_result(root))
    check_result_btn.pack(side=BOTTOM, pady=20)

    root.mainloop()

main_window()
