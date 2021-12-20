from pathlib import Path

# from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1173x706")
window.configure(bg = "#25294C")


canvas = Canvas(
    window,
    bg = "#25294C",
    height = 706,
    width = 1173,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    236.5,
    241.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#2F3560",
    highlightthickness=0
)
entry_1.place(
    x=72.0,
    y=108.0,
    width=329.0,
    height=265.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    931.5,
    243.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#2F3560",
    highlightthickness=0
)
entry_2.place(
    x=767.0,
    y=108.0,
    width=329.0,
    height=268.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=162.91561889648438,
    y=440.44171142578125,
    width=124.08438110351562,
    height=128.55831909179688
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=522.3933715820312,
    y=436.6972351074219,
    width=123.21322631835938,
    height=128.55831909179688
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=870.4390258789062,
    y=440.44171142578125,
    width=123.21319580078125,
    height=128.55831909179688
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    584.0,
    241.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#2F3661",
    highlightthickness=0
)
entry_3.place(
    x=567.0,
    y=179.0,
    width=34.0,
    height=123.0
)

canvas.create_text(
    429.0,
    25.0,
    anchor="nw",
    text="Plagiarism Analyzer",
    fill="#FFFFFF",
    font=("Cambria", 35 * -1)
)
window.resizable(False, False)
window.mainloop()
