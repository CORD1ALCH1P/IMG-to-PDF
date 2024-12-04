import os
from tkinter import Tk, Label, Button, filedialog, StringVar, OptionMenu
from PIL import Image

def create_pdf(image_files, output_pdf, page_size):
    if page_size == "A4":
        page_width, page_height = 595, 842
    elif page_size == "A3":
        page_width, page_height = 842, 1191
    else:
        page_width, page_height = 595, 842

    images = []
    for file in sorted(image_files):
        img = Image.open(file)
        img.thumbnail((page_width, page_height), Image.Resampling.LANCZOS)
        images.append(img)

    images[0].save(output_pdf, save_all=True, append_images=images[1:])
    print(f"PDF создан: {output_pdf}")

def select_images():
    filetypes = [("Image files", "*.png *.jpg *.jpeg *.img")]
    filenames = filedialog.askopenfilenames(title="Select images", filetypes=filetypes)
    if filenames:
        image_files_var.set(f"Выбрано файлов: {len(filenames)}")
        global image_files
        image_files = list(filenames)

def save_pdf():
    output_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if output_pdf and image_files:
        create_pdf(image_files, output_pdf, page_size_var.get())

root = Tk()
root.title("Image to PDF Converter")

Label(root, text="Select images:").grid(row=0, column=0, padx=10, pady=10)
image_files_var = StringVar()
Button(root, text="Open", command=select_images).grid(row=0, column=1, padx=10)
Label(root, textvariable=image_files_var).grid(row=1, column=0, columnspan=2)

Label(root, text="Choose a format:").grid(row=2, column=0, padx=10, pady=10)
page_size_var = StringVar(root)
page_size_var.set("A4")
OptionMenu(root, page_size_var, "A4", "A3").grid(row=2, column=1, padx=10)

Button(root, text="Create PDF", command=save_pdf).grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()