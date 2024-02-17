import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Secret Notes")
window.config(padx=30, pady=30)


def show_key():
    global pixels_x, pixels_y
    pixels_x, pixels_y = tuple([int(0.1 * x) for x in hide_image.size])
    img2 = ImageTk.PhotoImage(hide_image.resize((pixels_x, pixels_y)))
    hide_button = tk.Button(key_frame, image=img2, command=hide_key)
    hide_button.image = img2
    hide_button.grid(row=0, column=1, padx=5)
    key_entry.config(show="")


def hide_key():
    global pixels_x, pixels_y
    pixels_x, pixels_y = tuple([int(0.1 * x) for x in show_image.size])
    img3 = ImageTk.PhotoImage(show_image.resize((pixels_x, pixels_y)))
    show_button = tk.Button(key_frame, image=img3, command=show_key)
    show_button.image = img3
    show_button.grid(row=0, column=1, padx=5)
    key_entry.config(show="*")


# UI
image = Image.open("top_secret.png")
show_image = Image.open("show.png")
hide_image = Image.open("hide.png")

pixels_x, pixels_y = tuple([int(0.1 * x) for x in image.size])
img = ImageTk.PhotoImage(image.resize((pixels_x, pixels_y)))
label_img = tk.Label(window, image=img)
label_img.image = img
label_img.pack()

title_label = tk.Label(window, text="Enter Your Title:", font=("Arial", 10, "bold"))
title_label.pack()
title_entry = tk.Entry(window, width=65)
title_entry.pack()

message_label = tk.Label(window, text="Enter Your Message:", font=("Arial", 10, "bold"))
message_label.pack()
message_text = tk.Text(window, width=50)
message_text.pack()

key_label = tk.Label(window, text="Enter Your Key:", font=("Arial", 10, "bold"))
key_label.pack()

key_frame = tk.Frame(window)
key_frame.pack()
key_entry = tk.Entry(key_frame, width=50)
key_entry.grid(row=0, column=0)

pixels_x, pixels_y = tuple([int(0.1 * x) for x in show_image.size])
img4 = ImageTk.PhotoImage(show_image.resize((pixels_x, pixels_y)))
show_button = tk.Button(key_frame, image=img4, command=show_key)
show_button.image = img4
show_button.grid(row=0, column=1, padx=5)
key_entry.config(show="*")

save_encrypt_btn = tk.Button(window, text="Save & Encrypt", font=("Arial", 8, "bold"))
save_encrypt_btn.pack()

decrypt_btn = tk.Button(window, text="Decrypt", font=("Arial", 8, "bold"))
decrypt_btn.pack()

window.mainloop()
