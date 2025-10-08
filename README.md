# Video Cleaner 🎥🧹

A professional **Python** utility for automatic cleaning and organization of video collections.
The script detects **corrupted**, **duplicate**, and **incomplete** videos, moving them into dedicated subfolders to keep your source directory clean and organized.

---

## 🧩 Description

**Video Cleaner** was designed to simplify the maintenance of large video libraries.
It uses `ffprobe` (part of the **FFmpeg** package) to check file integrity and duration, and automatically manages subfolders based on the type of detected issue.

The project also includes a setup script (`setup.sh`) that automatically creates a Python virtual environment, installs all dependencies, and runs the program.

---

## ⚙️ Main Features

| Function                    | Description                                                                                            |
| --------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Move corrupted videos**   | Detects files that cannot be opened by `ffprobe` and moves them to the `Corrupted` folder.             |
| **Move duplicate videos**   | Compares SHA1 hashes of files and moves duplicates to the `Duplicates` folder.                         |
| **Move incomplete videos**  | Detects videos with very short duration (e.g., < 5 seconds) and moves them to the `Incomplete` folder. |
| **Folder selection dialog** | Uses `tkinter` to open a graphical file explorer for choosing the source folder.                       |
| **Automatic organization**  | Automatically creates the required subfolders (`Corrupted`, `Incomplete`, `Duplicates`).               |

---

## 🧰 Requirements

* **Python 3.8+**
* **FFmpeg** (installed automatically by `setup.sh`)
* Standard Python modules: `os`, `shutil`, `subprocess`, `hashlib`, `tkinter`

---

## 🚀 Automatic Setup and Execution

This project includes a `setup.sh` script that handles everything for you:

```bash
chmod +x setup.sh
./setup.sh
```

This command will:

1. Create and activate a Python virtual environment (`venv`)
2. Verify and install `FFmpeg` if missing
3. Install dependencies from `requirements.txt`
4. Launch the main program (`main.py`)

---

## 🖥️ Manual Execution (Optional)

If you prefer manual setup:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

---

## 🧭 Main Menu

When running the program, a simple text-based menu appears:

```
==== Video Cleaner ====
1 - Move corrupted videos
2 - Move duplicate videos
3 - Move incomplete videos
```

After choosing an option, a graphical window will open for you to select the source folder.

---

## 📂 Project Structure

```
📁 project/
├── main.py
├── requirements.txt
├── setup.sh
└── README.md
```

During execution, the script automatically creates these folders:

```
Corrupted/
Incomplete/
Duplicates/
```

---

## 🧑‍💻 Author

Developed by **Vinícius**, a technician and programmer specialized in automation and file analysis systems.

---

## 🪪 License

This project is free for personal and educational use.
