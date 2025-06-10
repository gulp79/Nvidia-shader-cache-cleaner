# Shader Cache Cleaner

Una semplice applicazione desktop per Windows 11 che consente di cancellare rapidamente le cache degli shader e di DirectX 12 delle GPU NVIDIA. Utile in caso di problemi grafici dopo aggiornamenti di giochi come Fortnite.

<img width="353" alt="image" src="https://github.com/user-attachments/assets/955aeb2e-70b5-46b0-9aba-46bfea590720" />


## ✅ Funzionalità

- Interfaccia grafica moderna in tema scuro.
- Pulizia automatica delle seguenti directory di cache:
  - %LocalAppData%\NVIDIA\DXCache
  - %LocalAppData%\NVIDIA\GLCache
  - %LocalAppData%\NVIDIA\ComputeCache
  - %LocalAppData%\D3DSCache
  - %ProgramData%\NVIDIA Corporation\NV_Cache

## 🚀 Esecuzione locale

1. Installa Python 3.10+ da [python.org](https://www.python.org)
2. Clona il progetto:

```bash
git clone https://github.com/gulp79/shader-cache-cleaner.git
cd shader-cache-cleaner
```

3. Installa le dipendenze (Tkinter è incluso):

```bash
pip install -r requirements.txt
```

4. Avvia l'app:

```bash
python main.py
```

## 📦 Creazione EXE (locale)

Usa `pyinstaller`:

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole main.py
```

## ☁️ Build automatica con GitHub Actions

Il progetto include un workflow per creare automaticamente il `.exe` su ogni push.

## ⚠️ Attenzione

L'app cancella file nelle cartelle cache NVIDIA/DirectX. Usare con cautela.

## 📝 Licenza

MIT License
