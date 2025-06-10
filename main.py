import os
import shutil
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Cartelle di cache da pulire
CACHE_FOLDERS = [
    os.path.expandvars(r"%LocalAppData%\NVIDIA\DXCache"),
    os.path.expandvars(r"%LocalAppData%\NVIDIA\GLCache"),
    os.path.expandvars(r"%LocalAppData%\NVIDIA\ComputeCache"),
    os.path.expandvars(r"%LocalAppData%\D3DSCache"),
    os.path.expandvars(r"%ProgramData%\NVIDIA Corporation\NV_Cache"),
]

def delete_cache_folders():
    errors = []
    for folder in CACHE_FOLDERS:
        if os.path.exists(folder):
            try:
                for filename in os.listdir(folder):
                    file_path = os.path.join(folder, filename)
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
            except Exception as e:
                errors.append(f"Errore con {folder}: {e}")
    if errors:
        messagebox.showerror("Errore", "\n".join(errors))
    else:
        messagebox.showinfo("Successo", "Cache DirectX e NVIDIA pulita con successo!")

# Interfaccia grafica
app = tk.Tk()
app.title("Pulizia Cache Shader NVIDIA")
app.geometry("400x200")
app.configure(bg="#1e1e1e")

style = ttk.Style(app)
style.theme_use("clam")
style.configure("TButton", foreground="white", background="#3a3a3a", font=("Segoe UI", 12))
style.map("TButton", background=[("active", "#505050")])

label = tk.Label(app, text="Pulizia Cache Shader / DirectX 12", bg="#1e1e1e", fg="white", font=("Segoe UI", 14))
label.pack(pady=20)

clean_button = ttk.Button(app, text="Avvia Pulizia Cache", command=delete_cache_folders)
clean_button.pack(pady=10)

app.mainloop()
