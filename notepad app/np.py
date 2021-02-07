import PySimpleGUI as sg
from popup import popup_select

sg.theme("Material2")

path = None
Save = False
Size = 13
Font = "Arial"

menu_layout = [
    ["File", ["New", "Open...", "Save", "Save as", "Exit"]],
    ["Edit", ["Font Size", "Font"]]
]

layout = [
    [sg.Menu(menu_layout, background_color="white", text_color="black")],
    [sg.Multiline("", font=(Font, Size), size=(50, 20), key="Text", background_color="white", text_color="Black")],
]


def new_file():
    global Save, Check
    if Save or values.get("Text") == "\n":
        window["Text"].Update(value="")
    if not Save and values.get("Text") != "\n":
        Check = sg.popup_yes_no("Do you want to save?")
        if Check == "Yes":
            save_file()
        else:
            Save = True
            new_file()


def open_file():
    global path, Save, Check
    if not Save and values.get("Text") != "\n":
        Check = sg.popup_yes_no("Do you want to save?")
        if Check == "Yes":
            save_file()
        else:
            Save = True
            open_file()

    if Save or values.get("Text") == "\n":
        path = sg.popup_get_file("Open", no_window=True, file_types=(("Text File", ".txt"),))
        if path:
            f = open(path, "r")
            text = f.read()
            window["Text"].Update(value=text)
            f.close()
            Save = False
        else:
            path = None
            Save = False


def save_file():
    if path is None:
        save_as_file()
    else:
        global Save
        f = open(path, "w")
        f.write(values.get("Text"))
        f.close()
        Save = True


def save_as_file():
    global Save, path
    name = sg.popup_get_file("File Name: ", save_as=True, no_window=True, file_types=(("Text File", ".txt"),))
    if name:
        f = open(name, "w")
        f.write(values.get("Text"))
        f.close()
        Save = True
        path = name
    else:
        path = None
        Save = False


def font():
    global Font
    try:
        Font = popup_select(["Arial", "Arial Black", "Impact", "Courier", "Times", "Verdana", "Garamond", "Palatino"])
        window["Text"].Update(font=(Font, Size))

    except IndexError:
        pass


def font_size():
    global Size
    Siz = sg.popup_get_text("Size : " + str(Size), background_color="white", text_color="black", no_titlebar=True)
    try:
        Size = int(Siz)
        window["Text"].Update(font=(Font, Size))
    except ValueError:
        sg.popup_get_text("Size : " + str(Size), background_color="white", text_color="black", no_titlebar=True,
                          default_text="Incorrect Size")
    except TypeError:
        pass


window = sg.Window("NotePad", layout)

while True:
    events, values = window.Read()

    if events == sg.WIN_CLOSED:
        break

    if events == "Exit":
        if not Save or values.get("Text") != "\n":
            Check = sg.popup_yes_no("Do you want to save?")
            if Check == "Yes":
                save_file()
            else:
                break
        else:
            break

    if events == "New":
        new_file()

    if events == "Open...":
        open_file()

    if events == "Save":
        save_file()

    if events == "Save as":
        save_as_file()

    if events == "Font Size":
        font_size()

    if events == "Font":
        font()

window.close()
