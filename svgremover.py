import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET

# Function to remove background


def remove_background(svg_input_path, svg_output_path):
    tree = ET.parse(svg_input_path)
    root = tree.getroot()
    if len(root) > 0:
        root.remove(root[0])
    tree.write(svg_output_path)


def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("SVG Files", "*.svg")])
    if file_path:
        output_path = filedialog.asksaveasfilename(
            defaultextension=".svg", filetypes=[("SVG Files", "*.svg")])
        if output_path:
            remove_background(file_path, output_path)
            label_result.config(
                text="Background removed and saved successfully!")


app = tk.Tk()
app.title('SVG Background Remover')

label_instruction = tk.Label(
    app, text="Select an SVG file to remove the background:", padx=10, pady=10)
label_instruction.pack()

button_select = tk.Button(app, text="Select File",
                          command=select_file, padx=10, pady=10)
button_select.pack()

label_result = tk.Label(app, text="", padx=10, pady=10)
label_result.pack()

app.mainloop()
