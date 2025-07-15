from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from tkinter import PhotoImage

import tkinter.filedialog, tkinter as tk, time
from tkinter import messagebox as mb, filedialog, colorchooser
import customtkinter as ctk

import subprocess
import ctypes

import elevate
import keyboard as kb
import re
import os
import pickledb
import pyautogui
import webbrowser
import elevate

cur_path = ""
is_dvoetoch = False
PATHMAIN = os.getcwd()

'''def playcode():
    global pathMAin
    code = editArea.get('1.0', END)
    os.chdir(pathMain)
    output.change(code)
    os.system("python output.py")'''

db = pickledb.load("set.db", True)

def createBase(event=None):
    selection = font_combobox.get()
    if selection == "C++":
        answer = tkinter.messagebox.askokcancel(u'Создание новой структуры программы', u'Вы точно хотите создать новую структуру программы? Весь несохраненный контент будет удален!')
        if answer:
            baseprog = "#include <iostream> \nusing namespace std; \n\nint main() {\n   cout << \"Hello, World\"; \n}"
            editArea.insert('1.0', baseprog)
            changes()

    elif selection == "C#":
        answer = tkinter.messagebox.askokcancel(u'Создание новой структуры программы', u'Вы точно хотите создать новую структуру программы? Весь несохраненный контент будет удален!')
        if answer:
            baseprog = "using System;\n\npublic class Project\n{\n    public static void Main(string[] args)\n    {\n        Console.WriteLine (\"Hello, world!\");\n    }\n}"
            editArea.insert('1.0', baseprog)
            changes()

    elif selection == "HTML":
        answer = tkinter.messagebox.askokcancel(u'Создание новой структуры программы', u'Вы точно хотите создать новую структуру программы? Весь несохраненный контент будет удален!')
        if answer:
            baseprog = "<!DOCTYPE html> \n<html>\n  <head>\n        <!--Not visible settings-->\n   </head>\n   <body>\n       <!--Visible settings-->\n    </body>\n</html> "
            editArea.insert('1.0', baseprog)
            changes()

    elif selection == "Java":
        answer = tkinter.messagebox.askokcancel(u'Создание новой структуры программы', u'Вы точно хотите создать новую структуру программы? Весь несохраненный контент будет удален!')
        if answer:
            baseprog = "public class Program{\n\n    public static void main (String args[]){\n\n        System.out.println(\"Hello, world!\");\n\n    }\n\n}"
            editArea.insert('1.0', baseprog)
            changes()

    else:
        mb.showerror("Внимание", "Для данного языка программирования не требуется точка входа(начальная структура программы)")

def addLines(event=None):
    global lines, linesLabel
    text = editArea.get("1.0", 'end-1c')  # Получаем текст из виджета Text
    lines = text.split('\n')  # Разделяем текст на строки по символу новой строки
    num_lines_with_newline = len(lines)  # Получаем количество строк с символом новой строки
    lines = num_lines_with_newline
    linesLabel.config(text=lines)
    '''update_line_numbers()'''
    
def changePL(event=None):
    global repl
    selection = font_combobox.get()
    if selection == "Python":
        repl = [
            ['(^|\\s)(True|False|int|float|str|and |or |with |for |in |while |None|if |break|continue|async |class |self.|elif |else:|lambda|try|except|global )',keywords],
            ['(^|\\s)(from |import |as )', importPy],
            ['(^|\\s)(print|return |input|type|range|round|len|pass)', pyfunc],
            ['(^|\\s)(def)', func],
            ['".*?"', string],
            ['\".*?\"', string],
            ["'.*?'", string],
            ["\'.*?\'", string],
            ['#.*', comments],
            ['@.*', cppskob],
            ['{.*?}', cppskob],
        ]
        changes()

    elif selection == "C++":
        repl = [
            ['(^|\\s)(#include|using|namespace|int |float |double |string |bool |char |short |long )', keywords],
            ['(^|\\s)(cout|cin|std|return)', pyfunc],
            ['(^|\\s)(void|function)', func],
            ['".*?"', string],
            ['\".*?\"', string],
            ["'.*?'", string],
            ["\'.*?\'", string],
            ['//.*', comments],
            ['<.*?>', cppskob],
        ]
        changes()

    elif selection == "C#":
        repl = [
            ['(^|\\s)(using|namespace|int |float |double |string |bool |char |short |long |static |class |args|Convert.|public |static |private )', keywords],
            ['(^|\\s)(Console.|std|return|ToInt32|ToInt16|ToInt8|ToString)', pyfunc],
            ['(^|\\s)(void|function)', func],
            ['".*?"', string],
            ['\".*?\"', string],
            ["'.*?'", string],
            ["\'.*?\'", string],
            ['//.*', comments],
        ]
        changes()
    
    elif selection == "HTML":
        repl = [
            ['<.*?>', keywords],
            ['".*?"', string],
            ['\".*?\"', string],
            ["'.*?'", string],
            ["\'.*?\'", string],
            ['<!--.*?-->', comments],
        ]
        changes()
    
    elif selection == "CSS":
        repl = [
            [re.compile(r'{.*?}', re.DOTALL), cppskob],
            ['(^|\\s)(display|display|color|color|background-color|background-color|font-size|font-size|font-family|font-family|z-index|z-index|position|position|justify-content|justify-content|align-items|align-items)', pyfunc],
        ]
        changes()

    elif selection == "Java":
        repl = [
            ['(^|\\s)(abstract|assert|boolean|Int|Float|String|int|float|double|break|byte|case|catch|char|class|const |continue|default|do|double|else|enum|extends|final|finnaly|for|goto|if|instanceof|interface|long|native|new|private|protected|public|return|short|static|strictfp|super|switch|synchronized|this|throw|throws|transient|try|void|volatile|while)',keywords],
            ['(^|\\s)(package |import |implements )', importPy],
            ['(^|\\s)(.print|.println|.printf|.out|System|)', pyfunc],
            ['".*?"', string],
            ['\".*?\"', string],
            ["'.*?'", string],
            ["\'.*?\'", string],
            ['#.*', comments],
            ['@.*', cppskob],
            ['{.*?}', cppskob],
        ]
        changes()

    changes()


def CloseDir():
    global statusbar_list
    answer = tkinter.messagebox.askokcancel(u'Закрытие папки', u'Вы точно хотите закрыть папку? Весь несохраненный контент будет удален!')
    if answer:
        tree.delete(*tree.get_children())
        editArea.delete('1.0', 'end')
        editArea.pack()
        cur_path = ""
        app.title('FavoRit 2024')
        statusLabel.config(text=statusbar_list[6])

def OpenFile():
    global cur_path
    try:
        ftypes = [
        (u'Все файлы', '*'), (u'Текстовые файлы', '*.txt'), (u'Python код', '*.py'), (u'C++ код', '*.cpp'), (u'C# код', '*.cs'),]
        fn = tkinter.filedialog.Open(app, filetypes=ftypes).show()
        if fn == '':
            return
        editArea.delete('1.0', 'end')
        editArea.insert('1.0', open(fn, encoding=db.get('encode')).read())
        cur_path = fn
        if cur_path[-3:] == ".py":
            font_combobox.set("Python")
            changePL()
        elif cur_path[-3:] == "cpp":
            font_combobox.set("C++")
            changePL()
        elif cur_path[-3:] == ".cs":
            font_combobox.set("C#") 
            changePL()
        elif cur_path[-4:] == "html":
            font_combobox.set("HTML") 
            changePL()
        elif cur_path[-3:] == "css":
            font_combobox.set("CSS") 
            changePL()
        elif cur_path[-4:] == "java":
            font_combobox.set("Java")
            changePL()

        app.title(f'FavoRit 2024 - {cur_path}')
        changes()
        statusLabel.config(text=statusbar_list[1])
    except UnicodeDecodeError as e:
        mb.showerror("Encoding Error", f"An encoding error occurred while encoding the file. Check that the selected encoding supports the file \n\n\nError reading file: {str(e)}")
        statusLabel.config(text=statusbar_list[7])

def populate_tree(tree, node):
    tree.delete(*tree.get_children(node))
    path = tree.set(node, "fullpath")
    parent = tree.parent(node)

    if parent == "":
        parent_path = ""
    else:
        parent_path = tree.set(parent, "fullpath")

    if os.path.isdir(path):
        for p in sorted(os.listdir(path)):
            ptype = None
            ppath = os.path.join(path, p)
            if os.path.isdir(ppath):
                ptype = "dir"
                oid = tree.insert(node, "end", text=p, values=[ppath, ptype], image=DirBarImg_light)
                tree.insert(oid, 0, text="dummy")
                tree.item(oid, open=True)
                populate_tree(tree, oid)  # Рекурсивно добавляем содержимое папки
            elif os.path.isfile(ppath):
                ptype = "file"
                if ppath.endswith(".py"):
                    file_icon = PythonBarImg_light  # Укажите путь к иконке для файлов .py
                elif ppath.endswith(".cpp"):
                    file_icon = CppBarImg_light
                elif ppath.endswith(".cs"):
                    file_icon = CsBarImg_light
                elif ppath.endswith(".html"):
                    file_icon = HtmlBarImg_light
                elif ppath.endswith(".css"):
                    file_icon = CssBarImg_light
                elif ppath.endswith(".java"):
                    file_icon = JavaBarImg_light
                else:
                    file_icon = FileBarImg_light  # Для остальных файлов не устанавливаем иконку
                tree.insert(node, "end", text=p, values=[ppath, ptype], image=file_icon)
    
    tree.update()

#file_image = PhotoImage(file="file.gif")
    
def select_dir():
    selected_dir = filedialog.askdirectory()
    if selected_dir:
        tree.delete(*tree.get_children(""))
        tree.set("", "fullpath", selected_dir)
        populate_tree(tree, "")
        statusLabel.config(text=statusbar_list[5])

def on_open(event):
    item_id = tree.focus()
    if item_id:
        item = tree.item(item_id)
        if item["values"][1] == "dir":
            populate_tree(tree, item_id)

def read_file(event=None):
    global cur_path, pl_var, play_btn
    item_id = tree.focus()
    if item_id:
        item = tree.item(item_id)
        if item["values"][1] == "file":
            file_path = item["values"][0]
            file_path = file_path.replace('/', '\\')
            cur_path = file_path.replace('/', '\\')
            try:
                with open(file_path, "r", encoding=db.get('encode')) as file:
                    cur_path = file_path
                    if cur_path[-3:] == ".py":
                        font_combobox.set("Python")
                        changePL()
                    elif cur_path[-3:] == "cpp":
                        font_combobox.set("C++")
                        play_btn = Button
                        changePL()
                    elif cur_path[-3:] == ".cs":
                        font_combobox.set("C#") 
                        changePL()
                    elif cur_path[-4:] == "html":
                        font_combobox.set("HTML") 
                        changePL()
                    elif cur_path[-3:] == "css":
                        font_combobox.set("CSS") 
                        changePL()
                    elif cur_path[-4:] == "java":
                        font_combobox.set("Java")
                        changePL()

                    app.title(f'FavoRit 2024 - {file_path}')
                    content = file.read()
                    editArea.delete('1.0', 'end')
                    editArea.insert('1.0',content)
                    changes()
                    statusLabel.config(text=statusbar_list[1])
            except Exception as e:
                statusLabel.config(text=statusbar_list[7])
                mb.showerror("Encoding Error", f"An encoding error occurred while encoding the file. Check that the selected encoding supports the file \n\n\nError reading file: {str(e)}")

def SaveFile():
    global cur_path
    try:
        SaveFile = open(cur_path, "w", encoding=db.get('encode'))
        text = editArea.get('1.0', END)
        SaveFile.write(text)
        SaveFile.close()
        statusLabel.config(text=statusbar_list[2])
    except NameError:
        if cur_path == "":
            statusLabel.config(text=statusbar_list[7])
            tkinter.messagebox.showinfo("Операция отменена", "Вы не открыли файл для сохранения!")
        else:
            statusLabel.config(text=statusbar_list[7])
            tkinter.messagebox.showinfo("Произошла ошибка", "Произошла неизвестная ошибка! Попробуйте ещё раз")
    except FileNotFoundError:
        if cur_path == "":
            statusLabel.config(text=statusbar_list[7])
            tkinter.messagebox.showinfo("Операция отменена", "Вы не открыли файл для сохранения!")
        else:
            statusLabel.config(text=statusbar_list[7])
            tkinter.messagebox.showinfo("Произошла ошибка", "Произошла неизвестная ошибка! Попробуйте ещё раз")

def NewFile():
    answer = tkinter.messagebox.askokcancel(u'Создание нового файла', u'Вы точно хотите создать новый файл? Весь несохраненный контент будет удален!')
    if answer:
        editArea.delete('1.0', 'end')
        editArea.pack()
        app.title('FavoRit 2024')
        statusLabel.config(text=statusbar_list[0])

def SaveAllFile():
    file_path = filedialog.asksaveasfilename(defaultextension='.*', filetypes=((u'Все файлы', '*'), (u'Python код', '*.py'), (u'C++ код', '*.cpp'), (u'C# код', '*.cs'),))
    f = open(file_path, 'w', encoding=db.get('encode'))
    text = editArea.get('1.0', END)
    f.write(text)
    f.close()
    statusLabel.config(text=statusbar_list[3])

def close_file():
    global cur_path
    answer = tkinter.messagebox.askokcancel(u'Закрытие файла', u'Вы точно хотите закрыть файл? Весь несохраненный контент будет удален!')
    if answer:
        editArea.delete('1.0', 'end')
        editArea.pack()
        cur_path = ""
        app.title('FavoRit 2024')
        statusLabel.config(text=statusbar_list[4])

def rgb(rgb):
    return "#%02x%02x%02x" % rgb

def info():
    tkinter.messagebox.showinfo('FavoRit 2024', 'FavoRit 2024 \nПростая удобная IDE для разработки ПО на многих языках программирования \n\nfilcher2011, 2024')

def circSkobSet(event=None):
    kb.write(')')

def zakrugSkobSet(event=None):
    kb.write('}')

def squareSkobSet(event=None):
    kb.write(']')

def KovDvoinSet(event=None):
    kb.write('"')

def KovOdinSet(event=None):
    kb.write("'")

def execute(event=None):
    selection = font_combobox.get()
    if selection == "Python":
        try:
            with open(cur_path, 'w', encoding=db.get('encode')) as f:
                f.write(editArea.get('1.0', END))
            
            os.chdir(os.path.dirname(cur_path))
            os.system('start cmd /K python ' + os.path.basename(cur_path))
        except FileNotFoundError:
            mb.showerror("Error", "You haven't opened the file! Open the program with your code to start debugging")

    elif selection == "C#":
        try:
            with open(cur_path, 'w', encoding=db.get('encode')) as f:
                f.write(editArea.get('1.0', END))

            os.chdir(os.path.dirname(cur_path))
            os.system('start cmd /K "dotnet run"')
        except FileNotFoundError:
            mb.showerror("Error", "You haven't opened the file! Open the program with your code to start debugging")

    elif selection == "C++":
        try:
            with open(cur_path, 'w', encoding=db.get('encode')) as f:
                f.write(editArea.get('1.0', END))

            os.chdir(os.path.dirname(cur_path))
            os.system('start cmd /K "cl /EHsc'+ os.path.basename(cur_path) + '"')
        except FileNotFoundError:
            mb.showerror("Error", "You haven't opened the file! Open the program with your code to start debugging")

    elif selection == "HTML":
        try:
            with open(cur_path, 'w', encoding=db.get('encode')) as f:
                f.write(editArea.get('1.0', END))

            os.chdir(os.path.dirname(cur_path))
            webbrowser.open(cur_path)
        except FileNotFoundError:
            mb.showerror("Error", "You haven't opened the file! Open the program with your code to start debugging")

    elif selection == "Java":
        try:
            with open(cur_path, 'w', encoding=db.get('encode')) as f:
                f.write(editArea.get('1.0', END))

            os.chdir(os.path.dirname(cur_path))
            os.system(f'start cmd /K "javac {os.path.basename(cur_path)}"')
            os.system(f'start cmd /K "java {os.path.basename(cur_path).replace(".java", "")}"')
        except FileNotFoundError:
            mb.showerror("Error", "You haven't opened the file! Open the program with your code to start debugging")

    else:
        mb.showerror("Ошибка", "Данный тип файла нельзя запускать!")
    

def changes(event=None):
    global ptext

    if editArea.get('1.0', END) == ptext:
        return

    for tag in editArea.tag_names():
        editArea.tag_remove(tag, '1.0', 'end')
    
    i = 0
    for parrent, color in repl:
        for start, end in search_re(parrent, editArea.get('1.0', END)):
            editArea.tag_add(f'{i}', start, end)
            editArea.tag_config(f'{i}', foreground=color)
            i += 1
    
    ptext = editArea.get('1.0', END)
    addLines()
    '''update_line_numbers()'''

def search_re(pat, text):
    matches = []
    text = text.splitlines()

    for i, line in enumerate(text):
        for match in re.finditer(pat, line):
            matches.append((f"{i + 1}.{match.start()}", f"{i + 1}.{match.end()}"))

    return matches

def undo():
    editArea.edit_undo()

def redo():
    editArea.edit_redo()

def neonblacktheme():
    db.set('lightMode', 'false')
    app.quit()

def neonwhitetheme():
    db.set('lightMode', 'true')
    app.quit()

def gitcommit():
    global cur_path
    os.chdir(os.path.dirname(cur_path))
    os.system('start cmd /K "git commit"')

def gitpull():
    global cur_path
    os.chdir(os.path.dirname(cur_path))
    os.system('start cmd /K "git pull"')

def gitpush():
    global cur_path
    os.chdir(os.path.dirname(cur_path))
    os.system('start cmd /K "git push"')

def gitinit():
    global cur_path
    os.chdir(os.path.dirname(cur_path))
    os.system('start cmd /K "git init"')

def gitadd():
    global cur_path
    os.chdir(os.path.dirname(cur_path))
    os.system('start cmd /K "git add ."')

def screen():
    try:
        photo_path = filedialog.asksaveasfilename(defaultextension='.*', filetypes=((u'Все файлы', '*'), (u'PNG-Картинка', '*.png'), (u'JPEG-Картинка', '*.jpg'), (u'BMP-Картинка', '*.bmp')))
        pyautogui.screenshot(photo_path)
        tkinter.messagebox.showinfo('Откладка', 'Скриншот был успешно сохранен в папке ' + photo_path)
    except FileExistsError:
        photo_path = filedialog.asksaveasfilename(defaultextension='.*', filetypes=((u'Все файлы', '*'), (u'PNG-Картинка', '*.png'), (u'JPEG-Картинка', '*.jpg'), (u'BMP-Картинка', '*.bmp')))
        pyautogui.screenshot(photo_path)
        tkinter.messagebox.showinfo('Откладка', 'Скриншот был успешно сохранен в папке ' + photo_path)


def deleteFileWindow():
    global cur_path  # Убедитесь, что cur_path доступен в этой функции
    try:
        response = mb.askyesno("Подтверждение", "Вы действительно хотите удалить файл?")
        if response:
            # Удаляем файл из файловой системы
            os.remove(cur_path)

            # Удаляем элемент из Treeview по его идентификатору (cur_path)
            item_id = tree.focus()  # Получаем текущий фокусированный элемент
            if item_id:  # Проверяем, что элемент выбран
                tree.delete(item_id)  # Удаляем элемент из Treeview
            else:
                mb.showerror("Ошибка", "Пожалуйста, выберите файл для удаления.")
    except FileNotFoundError:
        mb.showerror("Ошибка", "Файл не найден. Пожалуйста, откройте файл чтобы его удалить.")
    except Exception as e:
        mb.showerror("Ошибка", f"Не удалось удалить файл: {str(e)}")

ctypes.windll.shcore.SetProcessDpiAwareness(True)

lines = 1
statusbar_list = ["The file was created successfully", "The file has been opened successfully", "The file was saved successfully", "The file was successfully saved as", "The file was successfully closed", "The folder has been opened successfully", "The folder was successfully closed", "Error"]

ctk.set_appearance_mode("Dark")
if db.get("lightMode") == 'true':
    try:
        ctk.set_default_color_theme("fr24_theme.json")
    except FileNotFoundError:
        tkinter.messagebox.showerror("Файла не существует", "Программа не нашла файл fr24_theme.json, которая отвечает за тему вашей программы. Пожалуйста, проверьте что файл не был удален или переименован")
else:
    try:
        ctk.set_default_color_theme("fr24_theme_dark.json")
    except FileNotFoundError:
        tkinter.messagebox.showerror("Файла не существует", "Программа не нашла файл fr24_theme_dark.json, которая отвечает за тему вашей программы. Пожалуйста, проверьте что файл не был удален или переименован")

app = ctk.CTk()
app.geometry('1366x768')
app.title("FavoRit 2024")

path = os.getcwd()
app.iconbitmap('icon.ico')
# Create menubar by setting the color 
menubar = Menu(app, background='lightblue', foreground='black', activebackground='#004c99', activeforeground='white')
  
# Declare file and edit for showing in menubar 
file = Menu(menubar, tearoff=False) 
edit = Menu(menubar, tearoff=False) 
view = Menu(menubar, tearoff=False)
git = Menu(menubar, tearoff=False)
encodings_menu = Menu(menubar, tearoff=False)
learn_program = Menu(menubar, tearoff=False)
  
# Add commands in in file menu 
file.add_command(label="New file", command=NewFile, accelerator="   CTRL-N")
file.add_command(label="Open file", command=OpenFile, accelerator="   CTRL-O")
file.add_command(label="Close file", command=close_file, accelerator="   CTRL-W")  
file.add_separator()
file.add_command(label="Open Folder", command=select_dir, accelerator="   CTRL-SHIFT-O")
file.add_command(label="Close Folder", command=CloseDir, accelerator="   CTRL-SHIFT-W")  
file.add_separator()
file.add_command(label="Save file", command=SaveFile, accelerator="   CTRL-S") 
file.add_command(label="Save file as", command=SaveAllFile, accelerator="   CTRL-SHIFT-S") 
file.add_separator()
file.add_command(label="Exit", command=app.quit, accelerator="   ALT-F4") 
  
# Add commands in edit menu 
edit.add_command(label="Undo", command = undo, accelerator="   CTRL-Z") 
edit.add_command(label="Redo", command = redo, accelerator="   CTRL-Y")
edit.add_separator()
edit.add_command(label="Cut", command=lambda: pyautogui.hotkey('ctrl', 'x'), accelerator="   CTRL-X") 
edit.add_command(label="Copy", command=lambda: pyautogui.hotkey('ctrl', 'c'), accelerator="   CTRL-C") 
edit.add_command(label="Paste", command=lambda: pyautogui.hotkey('ctrl', 'v'), accelerator="   CTRL-V") 

themeMenu = Menu(view, tearoff=0)
themeMenu.add_command(label="Dark Neon", command=neonwhitetheme)
themeMenu.add_command(label="Dark", command=neonblacktheme)

view.add_command(label="Create screenshot", command=screen, accelerator="   CTRL-P")
view.add_separator()
view.add_cascade(label="Theme",menu=themeMenu)
view.add_separator()

DopTheme = Menu(view, tearoff=0)
for filename in os.listdir(PATHMAIN + f'\\Theme\\'):
    DopTheme.add_command(label=filename, command=lambda fn=filename: db.set('themeFolder', fn) and app.quit())

view.add_cascade(label="Add. theme",menu=DopTheme)

def changeUpPanel(mode):
    if mode == 'light':
        rgb, hex = colorchooser.askcolor()
        if hex not in [' ', '', None]:
            try:
                color = open(PATHMAIN + '\\desing-set\\bg-color-light.txt', 'w')
                color.write(hex)
                color.close()
            except FileNotFoundError:
                mb.showerror("Файл не найден!","Внимание! Программа не нашла файл bg-color-light.txt  в папке desing-set! Он отвечает за цвет верхней панели. Пожалуйста, убедитесь что вы не переименовали и не удалили файл.")
        else:
            try:
                color = open(PATHMAIN + '\\desing-set\\bg-color-light.txt', 'w')
                color.write('#800080')
                color.close()
            except FileNotFoundError:
                mb.showerror("Файл не найден!","Внимание! Программа не нашла файл bg-color-light.txt  в папке desing-set! Он отвечает за цвет верхней панели. Пожалуйста, убедитесь что вы не переименовали и не удалили файл.")
    elif mode == 'dark':
        rgb, hex = colorchooser.askcolor()
        if hex not in [' ', '', None]:
            try:
                color = open(PATHMAIN + '\\desing-set\\bg-color-dark.txt', 'w')
                color.write(hex)
                color.close()
            except FileNotFoundError:
                mb.showerror("Файл не найден!","Внимание! Программа не нашла файл bg-color-light.txt  в папке desing-set! Он отвечает за цвет верхней панели. Пожалуйста, убедитесь что вы не переименовали и не удалили файл.")
        else:
            try:
                color = open(PATHMAIN + '\\desing-set\\bg-color-dark.txt', 'w')
                color.write('#4a4a4a')
                color.close()
            except FileNotFoundError:
                mb.showerror("Файл не найден!","Внимание! Программа не нашла файл bg-color-light.txt  в папке desing-set! Он отвечает за цвет верхней панели. Пожалуйста, убедитесь что вы не переименовали и не удалили файл.")

changeColorInterface = Menu(view, tearoff=0)
changeColorInterface.add_command(label="Изменить цвет верхней панели для светлой темы", command=lambda: changeUpPanel('light'))
changeColorInterface.add_command(label="Изменить цвет верхней панели для темной темы", command=lambda: changeUpPanel('dark'))

view.add_cascade(label="Интерфейс", menu=changeColorInterface)

git.add_command(label='Init', command=gitinit)
git.add_separator()
git.add_command(label='Commit', command=gitcommit)
git.add_command(label='Pull', command=gitpull)
git.add_command(label='Push', command=gitpush)
git.add_separator()
git.add_command(label='Add changes', command=gitadd)

encodings_menu.add_command(label="UTF-8", command=lambda: db.set('encode', 'UTF-8'))
encodings_menu.add_command(label="UTF-16", command=lambda: db.set('encode', 'utf-16'))
encodings_menu.add_command(label="UTF-16BE", command=lambda: db.set('encode', 'utf-16be'))
encodings_menu.add_command(label="CP1252", command=lambda: db.set('encode', 'cp1252'))
encodings_menu.add_command(label="CP437", command=lambda: db.set('encode', 'cp437'))

def hw():
    selection = font_combobox.get()
    if selection == 'Python':
        try:
            with open(f'{PATHMAIN}\\Programs\\Python\\hello_world.py') as file:
                content = file.read()
                editArea.delete('1.0', 'end')
                editArea.insert('1.0', content)
                changes()
        except Exception as e:
            mb.showerror("Ошибка при чтении файла",f"Ошибка при чтении файла: {e}")

    elif selection == 'C++':
        try:
            with open(f'{PATHMAIN}\\Programs\\C++\\hello_world.cpp') as file:
                content = file.read()
                editArea.delete('1.0', 'end')
                editArea.insert('1.0', content)
                changes()
        except Exception as e:
            mb.showerror("Ошибка при чтении файла", f"Ошибка при чтении файла: {e}")

    elif selection == 'C#':
        try:
            with open(f'{PATHMAIN}\\Programs\\C#\\hello_world.cs') as file:
                content = file.read()
                editArea.delete('1.0', 'end')
                editArea.insert('1.0', content)
                changes()
        except Exception as e:
            mb.showerror("Ошибка при чтении файла", f"Ошибка при чтении файла: {e}")
def calc():
    selection = font_combobox.get()
    if selection == 'Python':
        try:
            with open(f'{PATHMAIN}\\Programs\\Python\\calculator.py') as file:
                content = file.read()
                editArea.delete('1.0', 'end')
                editArea.insert('1.0', content)
                changes()
        except Exception as e:
            mb.showerror("Ошибка при чтении файла", f"Ошибка при чтении файла: {e}")

    elif selection == 'C++':
        try:
            with open(f'{PATHMAIN}\\Programs\\C++\\calculator.cpp') as file:
                content = file.read()
                editArea.delete('1.0', 'end')
                editArea.insert('1.0', content)
                changes()
        except Exception as e:
            mb.showerror("Ошибка при чтении файла", f"Ошибка при чтении файла: {e}")

    elif selection == 'C#':
        try:
            with open(f'{PATHMAIN}\\Programs\\C#\\calculator.cs') as file:
                content = file.read()
                editArea.delete('1.0', 'end')
                editArea.insert('1.0', content)
                changes()
        except Exception as e:
            mb.showerror("Ошибка при чтении файла", f"Ошибка при чтении файла: {e}")
def what_ur_name():
    selection = font_combobox.get()
    if selection == 'Python':
        try:
            with open(f'{PATHMAIN}\\Programs\\Python\\what_is_your_name.py') as file:
                content = file.read()
                editArea.delete('1.0', 'end')
                editArea.insert('1.0', content)
                changes()
        except Exception as e:
            mb.showerror("Ошибка при чтении файла", f"Ошибка при чтении файла: {e}")

    elif selection == 'C++':
        try:
            with open(f'{PATHMAIN}\\Programs\\C++\\what_is_your_name.cpp') as file:
                content = file.read()
                editArea.delete('1.0', 'end')
                editArea.insert('1.0', content)
                changes()
        except Exception as e:
            mb.showerror("Ошибка при чтении файла", f"Ошибка при чтении файла: {e}")

    elif selection == 'C#':
        try:
            with open(f'{PATHMAIN}\\Programs\\C#\\what_is_your_name.cs') as file:
                content = file.read()
                editArea.delete('1.0', 'end')
                editArea.insert('1.0', content)
                changes()
        except Exception as e:
            mb.showerror("Ошибка при чтении файла", f"Ошибка при чтении файла: {e}")

learn_program.add_command(label="Hello, world!", command=hw)
learn_program.add_command(label="Calculator", command=calc)
learn_program.add_command(label="What is your name?", command=what_ur_name)

# Display the file and edit declared in previous step 
menubar.add_cascade(label="File", menu=file) 
menubar.add_cascade(label="Edit", menu=edit) 
menubar.add_cascade(label="View", menu=view)
menubar.add_cascade(label="Git", menu=git)
menubar.add_cascade(label="Encodings", menu=encodings_menu)
menubar.add_cascade(label="Info", command=info)
menubar.add_cascade(label="Learn Program", menu=learn_program)

# Displaying of menubar in the app 
app.config(menu=menubar)
if db.get("lightMode") == 'true':
    #Подправь тут в ошибках название файлов!!!
    try:
        newImgIshod_light = PATHMAIN + f'\\Theme\\' + db.get('themeFolder') +'\\new_file_fr24.gif'
        newImg_light = PhotoImage(file=newImgIshod_light)
    except tkinter.TclError:
            tkinter.messagebox.showerror("Ошибка работы №1", "Произошла ошибка работы. Она связанна с тем, что отсутствует файл \"new_file_fr24.gif\". Чтобы устранить проблему, пожалуйста, убедитесь что вы не переименовали или не удалили файл \"newfile.gif\". Если его нет, то верните его, или поставте другую иконку(Главное чтобы она имела имя newfile.gif!).")

    try:
        openImgIshod_light = PATHMAIN + f'\\Theme\\' + db.get('themeFolder') + '\\open_file_fr24.gif'
        openImg_light = PhotoImage(file=openImgIshod_light)
    except tkinter.TclError:
            tkinter.messagebox.showerror("Ошибка работы №1.1", "Произошла ошибка работы. Она связанна с тем, что отсутствует файл \"open_file_fr24.gif\". Чтобы устранить проблему, пожалуйста, убедитесь что вы не переименовали или не удалили файл \"open.gif\". Если его нет, то верните его, или поставте другую иконку(Главное чтобы она имела имя open.gif!).")

    try:
        saveImgIshod_light = PATHMAIN + f'\\Theme\\' + db.get('themeFolder') + '\\save_fr24.gif'
        saveImg_light = PhotoImage(file=saveImgIshod_light)
    except tkinter.TclError:
            tkinter.messagebox.showerror("Ошибка работы №1.2", "Произошла ошибка работы. Она связанна с тем, что отсутствует файл \"save_fr24.gif\". Чтобы устранить проблему, пожалуйста, убедитесь что вы не переименовали или не удалили файл \"save.gif\". Если его нет, то верните его, или поставте другую иконку(Главное чтобы она имела имя save.gif!).")

    try:
        playImgIshod_light = PATHMAIN + f'\\Theme\\' + db.get('themeFolder') + '\\play_fr24.gif'
        playImg_light = PhotoImage(file=playImgIshod_light)
    except tkinter.TclError:
            tkinter.messagebox.showerror("Ошибка работы №1.3", "Произошла ошибка работы. Она связанна с тем, что отсутствует файл \"play_fr24.gif\". Чтобы устранить проблему, пожалуйста, убедитесь что вы не переименовали или не удалили файл \"play_fr24.gif\". Если его нет, то верните его, или поставте другую иконку(Главное чтобы она имела имя play_fr24.gif!).")

    try:
        openDirImgIshod_light = PATHMAIN + f'\\Theme\\' + db.get('themeFolder') + '\\openDir_fr24.gif'
        OpenDirImg_light = PhotoImage(file=openDirImgIshod_light)
    except tkinter.TclError:
            tkinter.messagebox.showerror("Ошибка работы №1.4", "Произошла ошибка работы. Она связанна с тем, что отсутствует файл \"openDir_fr24.gif\". Чтобы устранить проблему, пожалуйста, убедитесь что вы не переименовали или не удалили файл \"openDir_fr24.gif\". Если его нет, то верните его, или поставте другую иконку(Главное чтобы она имела имя openDir_fr24.gif!).")

    try:
        closeFileImgIshod_light = PATHMAIN + f'\\Theme\\' + db.get('themeFolder') + '\\close_file.gif'
        CloseFileImg_light = PhotoImage(file=closeFileImgIshod_light)
    except tkinter.TclError:
            tkinter.messagebox.showerror("Ошибка работы №1.5", "Произошла ошибка работы. Она связанна с тем, что отсутствует файл \"close_file.gif\". Чтобы устранить проблему, пожалуйста, убедитесь что вы не переименовали или не удалили файл \"close_file.gif\". Если его нет, то верните его, или поставте другую иконку(Главное чтобы она имела имя close_file.gif!).")

    try:
        closeDirImgIshod_light = PATHMAIN + f'\\Theme\\' + db.get('themeFolder') + '\\close_folder.gif'
        closeDirImg_light = PhotoImage(file=closeDirImgIshod_light)
    except tkinter.TclError:
            tkinter.messagebox.showerror("Ошибка работы №1.6", "Произошла ошибка работы. Она связанна с тем, что отсутствует файл \"close_folder.gif\". Чтобы устранить проблему, пожалуйста, убедитесь что вы не переименовали или не удалили файл \"close_folder.gif\". Если его нет, то верните его, или поставте другую иконку(Главное чтобы она имела имя close_folder.gif!).")
    
    try:
        DirBarImgIshod_light = PATHMAIN + f'\\Theme\\' + db.get('themeFolder') + '\\dir_bar_fr24.gif'
        DirBarImg_light = PhotoImage(file=DirBarImgIshod_light)
    except tkinter.TclError:
        tkinter.messagebox.showerror("Ошибка работы №1.7", "Произошла ошибка работы. Она связанна с тем, что отсутствует файл \"folder_bar.gif\". Чтобы устранить проблему, пожалуйста, убедитесь что вы не переименовали или не удалили файл \"folder_bar.gif\". Если его нет, то верните его, или поставте другую иконку(Главное чтобы она имела имя folder_bar.gif!).")
    
    try:
        PythonImgIshod_light = PATHMAIN + f'\\Theme\\' + db.get('themeFolder') + '\\python_file_fr24.png'
        PythonBarImg_light = PhotoImage(file=PythonImgIshod_light)
    except tkinter.TclError:
        tkinter.messagebox.showerror("Ошибка работы №1.8", "Произошла ошибка работы. Она связанна с тем, что отсутствует файл \"python_file.gif\". Чтобы устранить проблему, пожалуйста, убедитесь что вы не переименовали или не удалили файл \"python_file.gif\". Если его нет, то верните его, или поставте другую иконку(Главное чтобы она имела имя python_file.gif!).")

    try:
        FileImgIshod_light = PATHMAIN + f'\\Theme\\' + db.get('themeFolder') + '\\null_file.gif'
        FileBarImg_light = PhotoImage(file=FileImgIshod_light)
    except tkinter.TclError:
        tkinter.messagebox.showerror("Ошибка работы №1.9", "Произошла ошибка работы. Она связанна с тем, что отсутствует файл \"null_file.gif\". Чтобы устранить проблему, пожалуйста, убедитесь что вы не переименовали или не удалили файл \"null_file.gif\". Если его нет, то верните его, или поставте другую иконку(Главное чтобы она имела имя null_file.gif!).")
    
    try:
        CppImgIshod_light = PATHMAIN + f'\\Theme\\' + db.get('themeFolder') + '\\cpp_file_fr24.png'
        CppBarImg_light = PhotoImage(file=CppImgIshod_light)
    except tkinter.TclError:
        tkinter.messagebox.showerror("Ошибка работы №1.10", "Произошла ошибка работы. Она связанна с тем, что отсутствует файл \"cpp_file_fr24.png\". Чтобы устранить проблему, пожалуйста, убедитесь что вы не переименовали или не удалили файл \"cpp_file_fr24.png\". Если его нет, то верните его, или поставте другую иконку(Главное чтобы она имела имя cpp_file_fr24.png!).")
    
    try:
        CsBarImg_light_ishod = PATHMAIN + f'\\Theme\\' + db.get('themeFolder') + '\\cs_file_fr24.png'
        CsBarImg_light = PhotoImage(file=CsBarImg_light_ishod)
    except tkinter.TclError:
        tkinter.messagebox.showerror("Ошибка работы №1.11", "Произошла ошибка работы. Она связанна с тем, что отсутствует файл \"cs_file_fr24.png\". Чтобы устранить проблему, пожалуйста, убедитесь что вы не переименовали или не удалили файл \"cs_file_fr24.png\". Если его нет, то верните его, или поставте другую иконку(Главное чтобы она имела имя cs_file_fr24.png!).")

    try:
        CssBarImg_light_ishod = PATHMAIN + f'\\Theme\\' + db.get('themeFolder') + '\\css_file_fr24.png'
        CssBarImg_light = PhotoImage(file=CssBarImg_light_ishod)
    except tkinter.TclError:
        tkinter.messagebox.showerror("Ошибка работы №1.12", "Произошла ошибка работы. Она связанна с тем, что отсутствует файл \"css_file_fr24.png\". Чтобы устранить проблему, пожалуйста, убедитесь что вы не переименовали или не удалили файл \"css_file_fr24.png\". Если его нет, то верните его, или поставте другую иконку(Главное чтобы она имела имя css_file_fr24.png!).")

    try:
        HtmlBarImg_light_ishod = PATHMAIN + f'\\Theme\\' + db.get('themeFolder') + '\\html_file_fr24.png'
        HtmlBarImg_light = PhotoImage(file=HtmlBarImg_light_ishod)
    except tkinter.TclError:
        tkinter.messagebox.showerror("Ошибка работы №1.13", "Произошла ошибка работы. Она связанна с тем, что отсутствует файл \"html_file_fr24.png\". Чтобы устранить проблему, пожалуйста, убедитесь что вы не переименовали или не удалили файл \"html_file_fr24.png\". Если его нет, то верните его, или поставте другую иконку(Главное чтобы она имела имя html_file_fr24.png!).")

    try:
        JavaBarImg_light_ishod = PATHMAIN + f'\\Theme\\' + db.get('themeFolder') + '\\java_file_fr24.png'
        JavaBarImg_light = PhotoImage(file=JavaBarImg_light_ishod)
    except tkinter.TclError:
        tkinter.messagebox.showerror("Ошибка работы №1.14", "Произошла ошибка работы. Она связанна с тем, что отсутствует файл \"java_file_fr24.png\". Чтобы устранить проблему, пожалуйста, убедитесь что вы не переименовали или не удалили файл \"java_file_fr24.png\". Если его нет, то верните его, или поставте другую иконку(Главное чтобы она имела имя java_file_fr24.png!).")

    try:
        colorPanel = open(PATHMAIN + '\\desing-set\\bg-color-light.txt').read()
        panelFrame = Frame(app, height=40, bg=colorPanel)
        newfile_btn = Button(panelFrame, text="", image=newImg_light, command=NewFile).pack(side="left")
        openfile_btn = Button(panelFrame, text="", image=openImg_light, command=OpenFile).pack(side="left")
        savefile_btn = Button(panelFrame, text="", image=saveImg_light, command=SaveFile).pack(side="left")
        closefile_btn = Button(panelFrame, text="", image=CloseFileImg_light, command=close_file).pack(side="left")
        nullLabel = Label(panelFrame, text="      ", fg=colorPanel, bg=colorPanel).pack(side="left")
        play_btn = Button(panelFrame, text="", image=playImg_light, command=execute).pack(side="left")
        nullLabel = Label(panelFrame, text="      ", fg=colorPanel, bg=colorPanel).pack(side="left")
        openDir_btn = Button(panelFrame, text="", image=OpenDirImg_light, command=select_dir).pack(side="left")
        closeDir_btn = Button(panelFrame, text="", image=closeDirImg_light, command=CloseDir).pack(side="left")
        nullLabel = Label(panelFrame, text="      ", fg=colorPanel, bg=colorPanel).pack(side="left")
        plCombo = ["Python", "C++", "C#", "HTML", "CSS", "Java"]
        pl_var = StringVar(value=plCombo[0])
        font_combobox = ctk.CTkOptionMenu(panelFrame, values=plCombo, command=changePL)
        font_combobox.pack(side="left")
        fr24_text = Label(panelFrame, text="FavoRit 2024", font="Cygre 14", fg="white", bg=colorPanel).pack(side="right")
    except FileNotFoundError:
        mb.showerror("Файл не найден!", "Внимание! Программа не нашла файл bg-color-light.txt  в папке desing-set! Он отвечает за цвет верхней панели. Пожалуйста, убедитесь что вы не переименовали и не удалили файл.")
else:

    try:
        newImgIshod_dark = PATHMAIN + f'\\Theme\\' + db.get('themeFolder') + '\\newfile_dark_fr24.gif'
        newImg_dark = PhotoImage(file=newImgIshod_dark)
    except tkinter.TclError:
            tkinter.messagebox.showerror("Ошибка работы №1", "Произошла ошибка работы. Она связанна с тем, что отсутствует файл \"newfile_dark_fr24.gif\". Чтобы устранить проблему, пожалуйста, убедитесь что вы не переименовали или не удалили файл \"newfile_dark_fr24.gif\". Если его нет, то верните его, или поставте другую иконку(Главное чтобы она имела имя newfile_dark_fr24.gif!).")

    try:
        openImgIshod_dark = PATHMAIN + f'\\Theme\\' + db.get('themeFolder') + '\\openfile_dark_fr24.gif'
        openImg_dark = PhotoImage(file=openImgIshod_dark)
    except tkinter.TclError:
            tkinter.messagebox.showerror("Ошибка работы №1.1", "Произошла ошибка работы. Она связанна с тем, что отсутствует файл \"openfile_dark_fr24.gif\". Чтобы устранить проблему, пожалуйста, убедитесь что вы не переименовали или не удалили файл \"openfile_dark_fr24\". Если его нет, то верните его, или поставте другую иконку(Главное чтобы она имела имя openfile_dark_fr24!).")

    try:
        saveImgIshod_dark = PATHMAIN + f'\\Theme\\' + db.get('themeFolder') + '\\savefile_dark_fr24.gif'
        saveImg_dark = PhotoImage(file=saveImgIshod_dark)
    except tkinter.TclError:
            tkinter.messagebox.showerror("Ошибка работы №1.2", "Произошла ошибка работы. Она связанна с тем, что отсутствует файл \"savefile_dark_fr24.gif\". Чтобы устранить проблему, пожалуйста, убедитесь что вы не переименовали или не удалили файл \"savefile_dark_fr24.gif\". Если его нет, то верните его, или поставте другую иконку(Главное чтобы она имела имя savefile_dark_fr24.gif!).")

    try:
        playImgIshod_dark = PATHMAIN + f'\\Theme\\' + db.get('themeFolder') + '\\playcode_dark_fr24.gif'
        playImg_dark = PhotoImage(file=playImgIshod_dark)
    except tkinter.TclError:
            tkinter.messagebox.showerror("Ошибка работы №1.3", "Произошла ошибка работы. Она связанна с тем, что отсутствует файл \"playcode_dark_fr24.gif\". Чтобы устранить проблему, пожалуйста, убедитесь что вы не переименовали или не удалили файл \"playcode_dark_fr24.gif\". Если его нет, то верните его, или поставте другую иконку(Главное чтобы она имела имя playcode_dark_fr24.gif!).")

    try:
        openDirImgIshod_dark = PATHMAIN + f'\\Theme\\' + db.get('themeFolder') + '\\openFolder_dark_fr24.gif'
        openDirImg_dark = PhotoImage(file=openDirImgIshod_dark)
    except tkinter.TclError:
            tkinter.messagebox.showerror("Ошибка работы №1.4", "Произошла ошибка работы. Она связанна с тем, что отсутствует файл \"openFolder_dark_fr24.gif\". Чтобы устранить проблему, пожалуйста, убедитесь что вы не переименовали или не удалили файл \"openFolder_dark_fr24.gif\". Если его нет, то верните его, или поставте другую иконку(Главное чтобы она имела имя openFolder_dark_fr24.gif!).")

    try:
        closeFileImgIshod_dark = PATHMAIN + f'\\Theme\\' + db.get('themeFolder') + '\\closefile_dark_fr24.gif'
        CloseFileImg_dark = PhotoImage(file=closeFileImgIshod_dark)
    except tkinter.TclError:
            tkinter.messagebox.showerror("Ошибка работы №1.5", "Произошла ошибка работы. Она связанна с тем, что отсутствует файл \"closefile_dark_fr24.gif\". Чтобы устранить проблему, пожалуйста, убедитесь что вы не переименовали или не удалили файл \"closefile_dark_fr24.gif\". Если его нет, то верните его, или поставте другую иконку(Главное чтобы она имела имя closefile_dark_fr24.gif!).")

    try:
        closeDirImgIshod_dark = PATHMAIN + f'\\Theme\\' + db.get('themeFolder') + '\\closefolder_dark_fr24.gif'
        closeDirImg_dark = PhotoImage(file=closeDirImgIshod_dark)
    except tkinter.TclError:
            tkinter.messagebox.showerror("Ошибка работы №1.6", "Произошла ошибка работы. Она связанна с тем, что отсутствует файл \"closefolder_dark_fr24.gif\". Чтобы устранить проблему, пожалуйста, убедитесь что вы не переименовали или не удалили файл \"closefolder_dark_fr24.gif\". Если его нет, то верните его, или поставте другую иконку(Главное чтобы она имела имя closefolder_dark_fr24.gif!).")
    
    try:
        DirBarImgIshod_light = PATHMAIN + f'\\Theme\\' + db.get('themeFolder') + '\\dir_bar_fr24.gif'
        DirBarImg_light = PhotoImage(file=DirBarImgIshod_light)
    except tkinter.TclError:
        tkinter.messagebox.showerror("Ошибка работы №1.7", "Произошла ошибка работы. Она связанна с тем, что отсутствует файл \"folder_bar.gif\". Чтобы устранить проблему, пожалуйста, убедитесь что вы не переименовали или не удалили файл \"folder_bar.gif\". Если его нет, то верните его, или поставте другую иконку(Главное чтобы она имела имя folder_bar.gif!).")
    
    try:
        PythonImgIshod_light = PATHMAIN + f'\\Theme\\' + db.get('themeFolder') + '\\python_file_fr24.png'
        PythonBarImg_light = PhotoImage(file=PythonImgIshod_light)
    except tkinter.TclError:
        tkinter.messagebox.showerror("Ошибка работы №1.8", "Произошла ошибка работы. Она связанна с тем, что отсутствует файл \"python_file.gif\". Чтобы устранить проблему, пожалуйста, убедитесь что вы не переименовали или не удалили файл \"python_file.gif\". Если его нет, то верните его, или поставте другую иконку(Главное чтобы она имела имя python_file.gif!).")

    try:
        FileImgIshod_light = PATHMAIN + f'\\Theme\\' + db.get('themeFolder') + '\\null_file.gif'
        FileBarImg_light = PhotoImage(file=FileImgIshod_light)
    except tkinter.TclError:
        tkinter.messagebox.showerror("Ошибка работы №1.9", "Произошла ошибка работы. Она связанна с тем, что отсутствует файл \"null_file.gif\". Чтобы устранить проблему, пожалуйста, убедитесь что вы не переименовали или не удалили файл \"null_file.gif\". Если его нет, то верните его, или поставте другую иконку(Главное чтобы она имела имя null_file.gif!).")
    
    try:
        CppImgIshod_light = PATHMAIN + f'\\Theme\\' + db.get('themeFolder') + '\\cpp_file_fr24.png'
        CppBarImg_light = PhotoImage(file=CppImgIshod_light)
    except tkinter.TclError:
        tkinter.messagebox.showerror("Ошибка работы №1.10", "Произошла ошибка работы. Она связанна с тем, что отсутствует файл \"cpp_file_fr24.png\". Чтобы устранить проблему, пожалуйста, убедитесь что вы не переименовали или не удалили файл \"cpp_file_fr24.png\". Если его нет, то верните его, или поставте другую иконку(Главное чтобы она имела имя cpp_file_fr24.png!).")
    
    try:
        CsBarImg_light_ishod = PATHMAIN + f'\\Theme\\' + db.get('themeFolder') + '\\cs_file_fr24.png'
        CsBarImg_light = PhotoImage(file=CsBarImg_light_ishod)
    except tkinter.TclError:
        tkinter.messagebox.showerror("Ошибка работы №1.10", "Произошла ошибка работы. Она связанна с тем, что отсутствует файл \"cs_file_fr24.png\". Чтобы устранить проблему, пожалуйста, убедитесь что вы не переименовали или не удалили файл \"cs_file_fr24.png\". Если его нет, то верните его, или поставте другую иконку(Главное чтобы она имела имя cs_file_fr24.png!).")

    try:
        colorPanel = open(PATHMAIN + '\\desing-set\\bg-color-dark.txt').read()
        panelFrame = Frame(app, height=40, bg=colorPanel)
        newfile_btn = Button(panelFrame, text="", image=newImg_dark, command=NewFile).pack(side="left")
        openfile_btn = Button(panelFrame, text="", image=openImg_dark, command=OpenFile).pack(side="left")
        savefile_btn = Button(panelFrame, text="", image=saveImg_dark, command=SaveFile).pack(side="left")
        closefile_btn = Button(panelFrame, text="", image=CloseFileImg_dark, command=close_file).pack(side="left")
        nullLabel = Label(panelFrame, text="      ", fg=colorPanel, bg=colorPanel).pack(side="left")
        play_btn = Button(panelFrame, text="", image=playImg_dark, command=execute).pack(side="left")
        nullLabel = Label(panelFrame, text="      ", fg=colorPanel, bg=colorPanel).pack(side="left")
        openDir_btn = Button(panelFrame, text="", image=openDirImg_dark, command=select_dir).pack(side="left")
        closeDir_btn = Button(panelFrame, text="", image=closeDirImg_dark, command=CloseDir).pack(side="left")
        nullLabel = Label(panelFrame, text="      ", fg=colorPanel, bg=colorPanel).pack(side="left")
        plCombo = ["Python", "C++", "C#", "HTML", "CSS"]
        pl_var = StringVar(value=plCombo[0])
        font_combobox = ctk.CTkOptionMenu(panelFrame, values=plCombo, command=changePL)
        font_combobox.pack(side="left")
        fr24_text = Label(panelFrame, text="FavoRit 2024", font="Cygre 14", fg="white", bg=colorPanel).pack(side="right")
    except FileNotFoundError:
        mb.showerror("Файл не найден!", "Внимание! Программа не нашла файл bg-color-dark.txt  в папке desing-set! Он отвечает за цвет верхней панели. Пожалуйста, убедитесь что вы не переименовали и не удалили файл.")

panelFrame.pack(side='top', fill='x')
statusFrame = Frame(app, height=30, bg='#000000')
statusFrame.pack(side='bottom', fill='x') 
statusLabel = Label(statusFrame, text="", bg="#000000", fg="#FFFFFF")
statusLabel.pack(side="left")
dopLines = Label(statusFrame, text="lines", bg="#000000", fg="#FFFFFF").pack(side="right")
linesLabel = Label(statusFrame, text=lines, bg="#000000", fg="#FFFFFF")
linesLabel.pack(side="right")


normal = rgb((234, 234, 234))
keywords = rgb((234, 95, 95))
pyfunc = rgb((0, 178, 194))
comments = rgb((95, 234, 165))
string = rgb((234, 162, 95))
func = rgb((109, 0, 199))
bgPer = rgb((42, 42, 42))
importPy = rgb((255, 162, 0))

cppskob = rgb((255, 215, 0))

'''line_numbers = tk.Text(app, width=5, background=bgPer, foreground=normal, insertbackground=normal, relief=FLAT, borderwidth=30, font=font)
line_numbers.pack(side="left", fill="y")'''

'''def update_line_numbers(event=None):
    # Удаляем старую нумерацию строк
    line_numbers.delete("1.0", "end")

    # Получаем количество строк в виджете Text
    num_lines = int(editArea.index("end-1c").split('.')[0])

    # Вставляем новую нумерацию строк
    for line in range(1, num_lines + 1):
        line_numbers.insert("end", str(line) + "\n")
    line_numbers.yview_moveto(1.0)

def multiple_yview(*args):
    editArea.yview(*args)
    line_numbers.yview(*args)

def on_mousewheel(event):
    delta = -10000 if event.delta < 1000 else 1000
    if event.widget == editArea:
        editArea.yview_scroll(delta, "units")
        line_numbers.yview_scroll(delta, "units")
    elif event.widget == line_numbers:
        editArea.yview_scroll(delta, "units")
        line_numbers.yview_scroll(delta, "units")'''

font = 'Consolas 15'

editArea = Text(
    app, background=bgPer, foreground=normal, insertbackground=normal, relief=FLAT, borderwidth=30, font=font, undo=True
)

editArea.pack(side='left', fill='both', expand=1)
scrollbar = ctk.CTkScrollbar(app,command=editArea.yview)
scrollbar.pack(side=LEFT, fill=Y)
editArea["yscrollcommand"]=scrollbar.set
'''scrollbar.config(command=multiple_yview)'''

tree = ttk.Treeview(show="tree")
tree.pack(expand=1, fill=BOTH)
#
tree.heading("#0", text="Directory Structure", anchor=tk.W)
tree.bind("<Double-1>", on_open)

tree["columns"] = ("fullpath", "type")
tree.column("fullpath", width=0)
tree.column("type", anchor="w", width=100)
tree.heading("fullpath", text="Full Path")
tree.heading("type", text="Type")

populate_tree(tree, "")

ptext = ''

repl = [
    ['(^|\\s)(True|False|int|float|str|and |or |with |for |in |while |None|if |break|continue|async |class |self.|elif |else:|lambda|try|except|global )', keywords],
    ['(^|\\s)(from |import |as )', importPy],
    ['(^|\\s)(print|return |input|type|range|round|len|pass)', pyfunc],
    ['(^|\\s)(def)', func],
    ['".*?"', string],
    ['\".*?\"', string],
    ["'.*?'", string],
    ["\'.*?\'", string],
    ['#.*', comments],
    ['@.*', cppskob],
    ['{.*?}', cppskob],
]

app.bind('<Delete>', lambda e: deleteFileWindow())

app.bind('(', circSkobSet)
app.bind('"', KovDvoinSet)
app.bind("'", KovOdinSet)
app.bind("{", zakrugSkobSet)
app.bind("[", squareSkobSet)
app.bind('<F5>', execute)

app.bind('<Control-s>', lambda e: SaveFile())
app.bind('<Control-S>', lambda e: SaveFile())
app.bind('<Control-o>', lambda e: OpenFile())
app.bind('<Control-O>', lambda e: OpenFile())
app.bind('<Control-z>', lambda e: undo())
app.bind('<Control-Z>', lambda e: undo())
app.bind('<Control-y>', lambda e: redo())
app.bind('<Control-Y>', lambda e: redo())

app.bind('<Control-Shift-S>', lambda e: SaveAllFile())
app.bind('<Control-Shift-s>', lambda e: SaveAllFile())
app.bind('<Shift-Control-s>', lambda e: SaveAllFile())
app.bind('<Shift-Control-S>', lambda e: SaveAllFile())
'''app.bind('<Control-Shift-f>', lambda e: SaveAllFile())
app.bind('<Control-Shift-F>', lambda e: SaveAllFile())
app.bind('<Shift-Control-f>', lambda e: SaveAllFile())
app.bind('<Shift-Control-F>', lambda e: SaveAllFile())'''

app.bind('<Control-F1>', lambda e: webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
app.bind('<F3>', createBase)
font_combobox.bind("<<ComboboxSelected>>", changePL)
app.bind('<KeyRelease>', changes)
tree.bind("<Double-1>", read_file)

app.bind("<Enter>", addLines)
'''editArea.bind("<Configure>", update_line_numbers)
editArea.bind("<KeyRelease>", multiple_yview)
editArea.bind("<MouseWheel>", on_mousewheel)'''

changes()
'''update_line_numbers()'''

if __name__ == '__main__':
    elevate.elevate()
    app.mainloop()