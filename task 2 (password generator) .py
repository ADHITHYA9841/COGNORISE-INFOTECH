import random
import string
import tkinter as tk
from tkinter import messagebox

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x250")

        self.label = tk.Label(root, text="Enter the desired length of the password:", font=("Helvetica", 12))
        self.label.pack(pady=10)

        self.length_entry = tk.Entry(root, font=("Helvetica", 12), width=5)
        self.length_entry.pack(pady=10)

        self.options_frame = tk.Frame(root)
        self.options_frame.pack(pady=10)

        self.include_uppercase = tk.BooleanVar()
        self.include_numbers = tk.BooleanVar()
        self.include_special = tk.BooleanVar()

        self.uppercase_check = tk.Checkbutton(self.options_frame, text="Include Uppercase Letters", variable=self.include_uppercase, font=("Helvetica", 10))
        self.uppercase_check.pack(anchor='w')

        self.numbers_check = tk.Checkbutton(self.options_frame, text="Include Numbers", variable=self.include_numbers, font=("Helvetica", 10))
        self.numbers_check.pack(anchor='w')

        self.special_check = tk.Checkbutton(self.options_frame, text="Include Special Characters", variable=self.include_special, font=("Helvetica", 10))
        self.special_check.pack(anchor='w')

        self.gen_button = tk.Button(root, text="Generate Password", command=self.generate_password, font=("Helvetica", 12))
        self.gen_button.pack(pady=10)

        self.password_display = tk.Entry(root, font=("Helvetica", 12), width=30)
        self.password_display.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 1:
                raise ValueError("Length must be at least 1.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for the length.")
            return

        characters = string.ascii_lowercase
        if self.include_uppercase.get():
            characters += string.ascii_uppercase
        if self.include_numbers.get():
            characters += string.digits
        if self.include_special.get():
            characters += string.punctuation

        if len(characters) == 0:
            messagebox.showerror("No Characters Selected", "Please select at least one character set.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        
        self.password_display.delete(0, tk.END)
        self.password_display.insert(0, password)

def main():
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
