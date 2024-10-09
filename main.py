import os
from tkinter import Tk, Label, Button, filedialog, StringVar, OptionMenu
from PIL import Image

# Функция для создания PDF из изображений
def create_pdf(image_files, output_pdf, page_size):
    # Установим размер страницы
    if page_size == "A4":
        page_width, page_height = 595, 842  # размеры в пунктах (1 пункт = 1/72 дюйма)
    elif page_size == "A3":
        page_width, page_height = 842, 1191
    else:
        page_width, page_height = 595, 842  # по умолчанию A4

    images = []
    for file in sorted(image_files):
        img = Image.open(file)
        # Преобразуем изображения в подходящий размер
        img.thumbnail((page_width, page_height), Image.Resampling.LANCZOS)  # Используем LANCZOS вместо ANTIALIAS
        images.append(img)

    # Создаем PDF из изображений
    images[0].save(output_pdf, save_all=True, append_images=images[1:])
    print(f"PDF создан: {output_pdf}")

# Функция для выбора изображений
def select_images():
    filetypes = [("Image files", "*.png *.jpg *.jpeg *.img")]
    filenames = filedialog.askopenfilenames(title="Выберите изображения", filetypes=filetypes)
    if filenames:
        image_files_var.set(f"Выбрано файлов: {len(filenames)}")  # Отображаем количество файлов
        global image_files
        image_files = list(filenames)

# Функция для сохранения PDF
def save_pdf():
    output_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if output_pdf and image_files:
        create_pdf(image_files, output_pdf, page_size_var.get())

# Основное окно приложения
root = Tk()
root.title("Image to PDF Converter")

# Выбор изображений
Label(root, text="Выберите изображения:").grid(row=0, column=0, padx=10, pady=10)
image_files_var = StringVar()
Button(root, text="Выбрать файлы", command=select_images).grid(row=0, column=1, padx=10)
Label(root, textvariable=image_files_var).grid(row=1, column=0, columnspan=2)

# Выбор формата страницы
Label(root, text="Выберите формат страницы:").grid(row=2, column=0, padx=10, pady=10)
page_size_var = StringVar(root)
page_size_var.set("A4")  # Значение по умолчанию
OptionMenu(root, page_size_var, "A4", "A3").grid(row=2, column=1, padx=10)

# Кнопка для сохранения PDF
Button(root, text="Создать PDF", command=save_pdf).grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()
