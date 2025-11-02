from tkinter import Tk, ttk, filedialog, StringVar
from watermarker import add_watermark

root = Tk()
root.title("Add Watermark")

img_path: StringVar = StringVar()


def get_image_file(event=None):
    img_path.set(filedialog.askopenfilename(parent=root,filetypes=[("Image Files", ["*.png", "*.jpg", "*.jpeg", "*.webp"])]))


def get_watermark_folder(event=None):
    save_path: str = filedialog.asksaveasfilename(parent=root, initialfile=img_path.get())
    
    add_watermark(img_path.get(), save_path)


mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky="NWES")

img_label = ttk.Label(mainframe, text="Upload an image to get watermarked.").grid(
    column=0, row=0, sticky="we", columnspan=2
)
img_button = ttk.Button(mainframe, text="Upload Image", command=get_image_file).grid(
    column=0, row=1, sticky="we"
)
watermark_button = ttk.Button(
    mainframe, text="Watermark", command=get_watermark_folder
).grid(column=1, row=1, sticky="we")
file_label = ttk.Label(mainframe, text="Selected Image: ").grid(
    column=0, row=2, sticky="w"
)
path_label = ttk.Label(mainframe, textvariable=img_path).grid(
    column=1, row=2, sticky="w"
)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
