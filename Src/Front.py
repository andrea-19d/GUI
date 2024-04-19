from tkinter import *
from tkinter import ttk

from Backend.func import choose_encryption_algorithm, choose_decryption_algorithm
from Src.Style import *


def encrypt():
    plaintext = input_text.get("1.0", "end-1c")
    cipher_type = algorithm_var.get()
    ciphertext = choose_encryption_algorithm(cipher_type, plaintext)

    output_text.delete("1.0", "end")
    if isinstance(ciphertext, bytes):
        output_text.insert("1.0", ciphertext.hex())
    else:
        output_text.insert("1.0", ciphertext)


def decrypt():
    try:
        plaintext = input_text.get("1.0", "end-1c")

        ciphertext_hex = output_text.get("1.0", "end-1c")

        input_text.delete("1.0", "end")

        input_text.insert("1.0", ciphertext_hex)

        ciphertext = bytes.fromhex(ciphertext_hex)

        cipher_type = algorithm_var.get()
        plaintext = choose_decryption_algorithm(cipher_type, ciphertext, plaintext)

        output_text.delete("1.0", "end")
        output_text.insert("1.0", plaintext)

    except ValueError:
        output_text.delete("1.0", "end")
        output_text.insert("1.0", "Error: Invalid hexadecimal string")


root = Tk()
# Apply styles to the root window
root.geometry("450x600")
root.configure(bg=root_style["bg"])
root.resizable(*root_style["resizable"])
root["borderwidth"] = root_style["borderwidth"]
root["highlightthickness"] = root_style["highlightthickness"]
root.attributes("-alpha", root_style["opacity"])  # Set opacity
root.config(cursor="top_left_arrow")

root.overrideredirect(True)


def move_app(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')


def quitter(e):
    root.quit()


border_frame = Frame(root, **border_frame_styles)
border_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

title_bar = Frame(root, **title_style)
title_bar.pack(expand=1, fill=X, padx=5)
title_bar.bind("<B1-Motion>", move_app)

title_label = Label(title_bar, **title_label_style)
title_label.pack(side=LEFT)
title_label.bind("<B1-Motion>", move_app)

title_close = Label(title_bar, **title_close_button_style)
title_close.pack(side=RIGHT)
title_close.bind("<Button-1>", quitter)

# Create input frame
input_frame = Frame(root, **input_frame_style)
input_frame.pack(fill=BOTH, expand=True, pady=10, padx=5)

# Load the image
input_bg_image = PhotoImage(file="Fonts/6.png")  # Replace "background_image.png" with your image file

# Create a label to act as the background for the input frame
bg_label = Label(input_frame, image=input_bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Make the label transparent so that the frame is visible
bg_label.image = input_bg_image

# Input label and text area
Label(input_frame, text="Enter Plain Text:", **label_style).grid(row=0, column=0, sticky=W)
input_text = Text(input_frame, **input_text_style)
input_text.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

style = ttk.Style()

# Define your custom style for the dropdown menu
style.theme_create("custom_dropdown_style", parent="alt", settings={
    "TCombobox": {
        "configure": {"foreground": "black", "background": "#EAA1D6", "selectbackground": "#8A2BE2"},
        "selectbackground": [("readonly", "#8A2BE2")],
        "fieldbackground": "#EAA1D6",
        "font": ('Pixelify Sans', 12),
        "relief": "flat",
        "arrowcolor": "#8A2BE2",
        "arrowpadding": 5,
        "border": 1,
        "highlightbackground": "#8A2BE2",
        "highlightthickness": 3,
    }
})
# Set the custom dropdown style
style.theme_use("custom_dropdown_style")

# Menu for choosing the algorithm
Label(input_frame, text="Select Algorithm:", font=('Pixelify Sans', 12, 'bold'), bg='#EAA1D6', fg='#8A2BE2', padx=10,
      pady=5, border=1, highlightbackground="#8A2BE2", highlightthickness=3).grid(row=2, column=0, sticky=W)

algorithm_var = StringVar()
algorithm_dropdown = ttk.Combobox(input_frame, textvariable=algorithm_var, font=('Pixelify Sans', 12, 'bold'),
                                  values=["Symmetric", "Asymmetric", "DSA"])
algorithm_dropdown.set("Symmetric")
algorithm_dropdown.grid(row=2, column=1, padx=10, sticky=W)

# Encrypt button
encrypt_button = Button(input_frame, text="Encrypt", command=encrypt, **button_style)
encrypt_button.grid(row=3, column=0, columnspan=2, pady=5, padx=10, sticky=W)

# Decrypt button
decrypt_button = Button(input_frame, text="Decrypt", command=decrypt, **button_style)
decrypt_button.grid(row=3, column=1, columnspan=2, pady=5, padx=5, sticky=W)

# Create output frame
output_frame = Frame(root, **output_frame_style)
output_frame.pack(fill=BOTH, expand=True, pady=10, padx=5)

output_bg_image = PhotoImage(file="Fonts/3.png")  # Replace "background_image.png" with your image file

# Create a label to act as the background for the input frame
bg_label = Label(output_frame, image=output_bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Make the label transparent so that the frame is visible
bg_label.image = output_bg_image

# Output label and text area
Label(output_frame, text="Encrypted/Decrypted Message:", **label_style).grid(row=0, column=0, sticky=W)
output_text = Text(output_frame, **text_style)
output_text.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Run the Tkinter event loop
root.mainloop()
