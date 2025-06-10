import os
import shutil
import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

CACHE_FOLDERS = {
    "DXCache": os.path.expandvars(r"%LocalAppData%\NVIDIA\DXCache"),
    "PerDriverVersion": os.path.expandvars(r"%LocalAppData%\NVIDIA\GLCache"),
    "ComputeCache": os.path.expandvars(r"%LocalAppData%\NVIDIA\ComputeCache"),
    "D3DSCache": os.path.expandvars(r"%LocalAppData%\D3DSCache"),
}

def delete_cache_folders():
    errors = []
    for name, folder in CACHE_FOLDERS.items():
        if os.path.exists(folder):
            try:
                for filename in os.listdir(folder):
                    path = os.path.join(folder, filename)
                    if os.path.isfile(path) or os.path.islink(path):
                        os.unlink(path)
                    elif os.path.isdir(path):
                        shutil.rmtree(path)
            except Exception as e:
                errors.append(f"{name}: {e}")
    if errors:
        messagebox.showerror("Errore", "\n".join(errors))
    else:
        messagebox.showinfo("Pulizia completata", "Le cache NVIDIA/DirectX sono state eliminate.")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("NVIDIA Cache Cleaner")
        self.geometry("460x480")
        self.resizable(False, False)

        ctk.CTkLabel(self, text="🧹 NVIDIA Cache Cleaner", font=("Segoe UI Semibold", 22)).pack(pady=(20, 5))
        ctk.CTkLabel(self, text="Pulitore Cache DirectX e Shader per Windows 11", font=("Segoe UI", 14)).pack()

        warning_text = (
            "⚠️ Questa operazione eliminerà le cache precompilate.\n"
            "I giochi potrebbero richiedere più tempo al primo avvio successivo."
        )
        ctk.CTkLabel(
            self,
            text=warning_text,
            text_color="#ffcc00",
            font=("Segoe UI", 12),
            justify="center",
            wraplength=420
        ).pack(pady=20)

        for label, folder in CACHE_FOLDERS.items():
            frame = ctk.CTkFrame(self, fg_color="#2b2b2b", corner_radius=8)
            frame.pack(pady=5, padx=20, fill="x")
            ctk.CTkLabel(frame, text=f"📂 {label}", font=("Segoe UI", 14), anchor="w").pack(side="left", padx=10, pady=8)
            ctk.CTkLabel(frame, text=folder.split("\\")[-1], font=("Segoe UI", 12), text_color="#888").pack(side="right", padx=10)

        ctk.CTkButton(
            self,
            text="🧹 Pulisci Cache NVIDIA",
            command=delete_cache_folders,
            fg_color="#32cd32",
            hover_color="#2eb82e",
            font=("Segoe UI Semibold", 16),
            text_color="black",
            height=40
        ).pack(pady=30, ipadx=20)

if __name__ == "__main__":
    app = App()
    app.mainloop()
