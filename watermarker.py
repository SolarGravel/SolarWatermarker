from PIL import Image

WATERMARK_PATH = "Watermark/tsg-logo-b.png"

def add_watermark(img_path: str, img_save_path: str):
    watermark = Image.open(WATERMARK_PATH)
    img = Image.open(img_path)
    
    watermark = watermark.resize(size=(img.size[0] // 4, img.size[1] // 4), resample=Image.Resampling.BILINEAR)
    
    img.paste(watermark, (0, 0), watermark)
    
    img.save(img_save_path)


if __name__ == "__main__":
    add_watermark(r"c:\Users\three\Pictures\nerd.png", r"c:\Users\three\Pictures\foto.png")