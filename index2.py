import tkinter as tk
from tkinter import messagebox

# Step 1: Dictionary for Morse code
english_to_morse = {
    # Letters
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    # Numbers
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',

    # Special Characters
    ',': '--..--', '.': '.-.-.-', "'": '.----.', ';': '-.-.-.', ':': '---...',
    '?': '..--..', '-': '-....-', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', '"': '.-..-.', '=': '-...-', '@': '.--.-.', '!': '-.-.--',
    '+': '.-.-.', '_': '..--.-', '$': '...-..-', ' ': '  '  # Space between words
}

# Translate function
def translate(text):
    text = text.upper()
    morse_string = ""
    for char in text:
        try:
            if char == " ":
                morse_string += "  "  # add a space between words
            else:
                morse_string += english_to_morse[char] + " "
        except KeyError:
            messagebox.showerror("Error", f"Sorry, I can't translate this character: {char}")
            morse_string += char + " "  # add the character to the string

    return morse_string

# GUI setup
def translate_text():
    input_text = text_input.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Input Error", "Please enter some text to translate.")
        return

    output = translate(input_text)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, output)

# Placeholder functionality
def add_placeholder(event):
    if text_input.get("1.0", tk.END).strip() == "":
        text_input.insert("1.0", "Enter your text here")
        text_input.tag_add("placeholder", "1.0", "end")
        text_input.tag_configure("placeholder", foreground="grey", font=('Times New Roman', 16))

def remove_placeholder(event):
    if text_input.get("1.0", tk.END).strip() == "Enter your text here":
        text_input.delete("1.0", tk.END)

# Setup the main window
root = tk.Tk()
root.title("Morse Code Translator")

# Input Text
label1 = tk.Label(root, text="Enter Text:", font=('Times New Roman', 20), fg='#1e212b')
label1.grid(row=0, column=0, padx=15, pady=10)
text_input = tk.Text(root, height=10, width=50, bg='#fff3b0', font=('Times New Roman', 16))
text_input.grid(row=1, column=0, padx=10, pady=10)
text_input.insert("1.0", "Enter your text here")
text_input.tag_add("placeholder", "1.0", "end")
text_input.tag_configure("placeholder", foreground="grey", font=('Times New Roman', 16))
text_input.bind("<FocusIn>", remove_placeholder)
text_input.bind("<FocusOut>", add_placeholder)

# Translate Button
translate_button = tk.Button(root, text="Translate", command=translate_text, font=('Times New Roman', 16), bg='#42bfdd', width=20, height=2)
translate_button.grid(row=2, column=0, padx=50, pady=50)

# Output Text Heading
output_heading = tk.Label(root, text="Translated Morse Code:", font=('Times New Roman', 20), fg='blue')
output_heading.grid(row=3, column=0, padx=10, pady=10)

# Output Text Label
output_label = tk.Label(root, text="Output Text:", font=('Times New Roman', 16), fg='#194190')
output_label.grid(row=4, column=0, padx=10, pady=10)

# Output Text
text_output = tk.Text(root, height=10, width=50, bg='#86bbd8', font=('Times New Roman', 16), fg='black')
text_output.grid(row=5, column=0, padx=10, pady=10)

# Start the main loop
root.mainloop()