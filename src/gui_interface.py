import tkinter as tk
from tkinter import filedialog, messagebox
from extract_transform import extract_and_transform
from load import load_to_mysql
import pandas as pd

class ETLPipelineGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ETL Pipeline")
        self.root.geometry("700x500")

        self.file_path = tk.StringVar()

        # File selection
        tk.Label(root, text="Select CSV File:").pack(pady=5)
        frame = tk.Frame(root)
        frame.pack()
        self.path_entry = tk.Entry(frame, textvariable=self.file_path, width=60)
        self.path_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Browse", command=self.browse_file).pack(side=tk.LEFT)

        # Extract & Transform Button
        self.et_button = tk.Button(root, text="1. Extract & Transform", command=self.extract_transform)
        self.et_button.pack(pady=10)

        # Load Button
        self.load_button = tk.Button(root, text="2. Load to MySQL", command=self.load_to_db, state=tk.DISABLED)
        self.load_button.pack(pady=10)

        # Output Display
        self.output_text = tk.Text(root, height=20, width=80)
        self.output_text.pack(pady=10)

    def browse_file(self):
        file = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file:
            self.file_path.set(file)

    def extract_transform(self):
        try:
            self.clean_data = extract_and_transform(self.file_path.get())
            self.output_text.delete('1.0', tk.END)
            self.output_text.insert(tk.END, "Cleaned sales data:\n")
            self.output_text.insert(tk.END, self.clean_data.to_string(index=False))
            self.load_button.config(state=tk.NORMAL)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def load_to_db(self):
        try:
            load_to_mysql(self.clean_data)
            messagebox.showinfo("Success", "Data successfully loaded into MySQL.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == '__main__':
    root = tk.Tk()
    app = ETLPipelineGUI(root)
    root.mainloop()