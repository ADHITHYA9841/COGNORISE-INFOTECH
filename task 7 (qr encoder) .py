import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
import cv2
from PIL import Image, ImageTk
import numpy as np

class QRCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Encoder/Decoder")
        self.root.geometry("600x400")

        self.input_label = tk.Label(root, text="Enter text or URL to generate QR Code:", font=("Helvetica", 12))
        self.input_label.pack(pady=10)

        self.input_entry = tk.Entry(root, font=("Helvetica", 12), width=50)
        self.input_entry.pack(pady=10)

        self.generate_button = tk.Button(root, text="Generate QR Code", command=self.generate_qr_code, font=("Helvetica", 12))
        self.generate_button.pack(pady=10)

        self.qr_code_display = tk.Label(root)
        self.qr_code_display.pack(pady=10)

        self.decode_button = tk.Button(root, text="Decode QR Code from Image", command=self.decode_qr_code, font=("Helvetica", 12))
        self.decode_button.pack(pady=10)

        self.decoded_text_display = tk.Label(root, text="", font=("Helvetica", 12))
        self.decoded_text_display.pack(pady=10)

    def generate_qr_code(self):
        input_data = self.input_entry.get()
        if not input_data:
            messagebox.showerror("Input Error", "Please enter text or URL to generate QR Code.")
            return

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(input_data)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        img = img.resize((200, 200), Image.LANCZOS)  # Use Image.LANCZOS instead of Image.ANTIALIAS

        self.qr_code_img = ImageTk.PhotoImage(img)
        self.qr_code_display.config(image=self.qr_code_img)

    def decode_qr_code(self):
        file_path = filedialog.askopenfilename()
        if not file_path:
            return

        img = cv2.imread(file_path)
        detector = cv2.QRCodeDetector()
        data, bbox, _ = detector.detectAndDecode(img)
        if not data:
            messagebox.showerror("Decoding Error", "Could not decode the QR Code.")
        else:
            self.decoded_text_display.config(text=f"Decoded Data: {data}")

def main():
    root = tk.Tk()
    app = QRCodeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
