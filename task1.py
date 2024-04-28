import os
import shutil
import sys

def copy_files(source, dest):
    try:
        for item in os.listdir(source):
            source_path = os.path.join(source, item)
            dest_path = os.path.join(dest, item)

            if os.path.isdir(source_path):
                copy_files(source_path, dest_path)
            elif os.path.isfile(source_path):
                file_extension = os.path.splitext(item)[1]
                file_extension_dir = os.path.join(dest, file_extension[1:])

                os.makedirs(file_extension_dir, exist_ok=True)
                shutil.copy2(source_path, file_extension_dir)

    except Exception as e:
        print(f"Помилка копіювання: {e}")

def main():
    if len(sys.argv) < 2:
        print("Потрібно вказати валідні вхідні дані")
        return

    source_dir = sys.argv[1]
    destination_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    if not os.path.exists(source_dir):
        print("Вихідна директорія не існує.")
        return

    os.makedirs(destination_dir, exist_ok=True)

    copy_files(source_dir, destination_dir)

if __name__ == "__main__":
    main()
