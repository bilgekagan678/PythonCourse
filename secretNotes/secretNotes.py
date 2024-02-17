import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Secret Notes")
window.config(padx=30, pady=30)

# UI
image = Image.open("top_secret.png")
pixels_x, pixels_y = tuple([int(0.1 * x) for x in image.size])
img = ImageTk.PhotoImage(image.resize((pixels_x, pixels_y)))
label_img = tk.Label(window, image=img)
label_img.image = img
label_img.pack()

title_label = tk.Label(window, text="Enter Your Title", font=("Arial", 10, "bold"))
title_label.pack()
title_entry = tk.Entry(window, width=65)
title_entry.pack()

message_label = tk.Label(window, text="Enter Your Message", font=("Arial", 10, "bold"))
message_label.pack()
message_text = tk.Text(window, width=50, height=20)
message_text.pack()

key_label = tk.Label(window, text="Enter Your Key", font=("Arial", 10, "bold"))
key_label.pack()
key_entry = tk.Entry(window, width=65)
key_entry.pack()

save_encrypt_btn = tk.Button(text="Save & Encrypt", font=("Arial", 8, "bold"))
save_encrypt_btn.pack()

decrypt_btn = tk.Button(text="Decrypt", font=("Arial", 8, "bold"))
decrypt_btn.pack()

window.mainloop()
