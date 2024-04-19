BLUE = '#A9D8FF'
PINK = '#EAA1D6'
PURPLE = '#8A2BE2'
LIGHT_BLUE = '#4E1683'


root_style = {
    "bg": PURPLE,
    "resizable": (True, False),  # Allow resizing in the horizontal direction only
    "borderwidth": 3,
    "relief": "flat",
    "highlightthickness": 0,
    "opacity": 1,
}

input_frame_style = {
    "bg": PINK,
    'border': 1,
    "highlightbackground": PURPLE,
    "highlightthickness": 3,
}

output_frame_style = {
    "bg": PINK,
    'border': 1,
    "highlightbackground": PURPLE,
    "highlightthickness": 3,
}

input_text_style = {
    'font': ('Pixelify Sans', 12),
    'bg': PINK,
    'fg': LIGHT_BLUE,
    'width': 40,
    'height': 5,
    'padx': 10,
    'pady': 5,
    "highlightbackground": PURPLE,
    "highlightthickness": 3,
    "relief": "flat",
}

text_style = {
    'font': ('Pixelify Sans', 12),
    'bg': PINK,
    'fg': LIGHT_BLUE,
    'width': 40,
    'height': 5,
    'padx': 10,
    'pady': 5,
    "highlightbackground": PURPLE,
    "highlightthickness": 3,
    "relief": "flat",
}

# Define styles for labels
label_style = {
    'font': ('Pixelify Sans', 12, 'bold'),
    'bg': PINK,
    'fg': PURPLE,
    'padx': 10,
    'pady': 10,
    'border': 1,
    "highlightbackground": PURPLE,
    "highlightthickness": 3,
}

# Create custom rounded button style
button_style = {
    "font": ("Pixelify Sans", 12, 'bold'),
    "padx": 10,
    "pady": 10,
    "background": PINK,
    "foreground": PURPLE,
    'border': 3,
    "relief": "groove",
}

title_style = {
    "bg": PINK,
    "border": 2,
    'pady': 2,
    'padx': 2,
    "highlightbackground": PURPLE,
    "highlightthickness": 3,
}

title_label_style = {
    "text": "Message Encryption and Decryption",
    "font": ('Pixelify Sans', 13, 'bold'),
    "bg": PINK,
    "fg": PURPLE,
}

title_close_button_style = {
    "text": "  X  ",
    "font": ('Pixelify Sans', 16),
    'bg': PINK,
    'fg': PURPLE,
    'border': 1,
    "highlightbackground": PURPLE,
    "highlightthickness": 2,
}

border_frame_styles = {
    "bg": BLUE,
    "highlightbackground": BLUE,
    "highlightthickness": 3,
    "border": 5,
}

