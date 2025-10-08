import os
import shutil
import subprocess
import hashlib
import tkinter as tk
from tkinter import filedialog

# Extensões de vídeo comuns
VIDEO_EXTENSIONS = (".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv")

def select_folder():
    """Abre o explorador de arquivos para o usuário escolher a pasta."""
    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory(title="Selecione a pasta de origem dos vídeos")
    return folder

def create_subfolder(base_dir, name):
    """Cria subpasta dentro da pasta de origem."""
    dest = os.path.join(base_dir, name)
    os.makedirs(dest, exist_ok=True)
    return dest

def is_broken_video(file_path):
    """Verifica se o vídeo está corrompido (não abre)."""
    try:
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries",
             "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="ignore"
        )
        if result.returncode != 0 or not result.stdout.strip():
            return True
        duration = float(result.stdout.strip())
        return duration <= 0
    except:
        return True

def is_incomplete_video(file_path, min_duration=5.0):
    """Verifica se o vídeo é muito curto ou truncado (incompleto)."""
    try:
        result = subprocess.run(
            ["ffprobe", "-v", "warning", "-show_entries",
             "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="ignore"
        )
        if result.returncode != 0 or not result.stdout.strip():
            return True
        duration = float(result.stdout.strip())
        return duration < min_duration
    except:
        return True

def hash_file(file_path):
    """Calcula hash SHA1 para detectar duplicados."""
    sha1 = hashlib.sha1()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                sha1.update(chunk)
        return sha1.hexdigest()
    except:
        return None

def move_file(file_path, dest_dir):
    """Move arquivo para a pasta de destino."""
    file_name = os.path.basename(file_path)
    dest_path = os.path.join(dest_dir, file_name)
    if os.path.exists(dest_path):
        base, ext = os.path.splitext(file_name)
        i = 1
        while os.path.exists(dest_path):
            dest_path = os.path.join(dest_dir, f"{base}_{i}{ext}")
            i += 1
    shutil.move(file_path, dest_path)
    print(f"Movido: {file_name}")

def move_corrupted_videos(base_dir):
    dest_dir = create_subfolder(base_dir, "Corrupted")
    for file in os.listdir(base_dir):
        file_path = os.path.join(base_dir, file)
        if not file.lower().endswith(VIDEO_EXTENSIONS):
            continue
        if is_broken_video(file_path):
            move_file(file_path, dest_dir)

def move_incomplete_videos(base_dir):
    dest_dir = create_subfolder(base_dir, "Incomplete")
    for file in os.listdir(base_dir):
        file_path = os.path.join(base_dir, file)
        if not file.lower().endswith(VIDEO_EXTENSIONS):
            continue
        if is_incomplete_video(file_path):
            move_file(file_path, dest_dir)

def move_duplicate_videos(base_dir):
    dest_dir = create_subfolder(base_dir, "Duplicates")
    seen_hashes = {}
    for file in os.listdir(base_dir):
        file_path = os.path.join(base_dir, file)
        if not file.lower().endswith(VIDEO_EXTENSIONS):
            continue
        file_hash = hash_file(file_path)
        if file_hash in seen_hashes:
            move_file(file_path, dest_dir)
        else:
            seen_hashes[file_hash] = file_path

def main():
    print("==== Video Cleaner ====")
    print("1 - Mover vídeos corrompidos")
    print("2 - Mover vídeos duplicados")
    print("3 - Mover vídeos incompletos")
    choice = input("Escolha uma opção (1/2/3): ").strip()

    base_dir = select_folder()
    if not base_dir:
        print("Nenhuma pasta selecionada. Saindo...")
        return

    if choice == "1":
        move_corrupted_videos(base_dir)
    elif choice == "2":
        move_duplicate_videos(base_dir)
    elif choice == "3":
        move_incomplete_videos(base_dir)
    else:
        print("Opção inválida.")

    print("Processo concluído.")

if __name__ == "__main__":
    main()
