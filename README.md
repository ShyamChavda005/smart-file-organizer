# 🗂️ Smart File Organizer (Python)

This is a simple and effective Python script that helps you automatically organize your files and folders based on their types. It's a perfect utility for cleaning up cluttered directories like `Downloads`, `Projects`, or any other folder with mixed file types.

---

## 📌 Features

- ✅ Automatically categorizes files into folders like:
  - `Images`, `Videos`, `Documents`, `Audio`, `Archives`, `Code`, `Executables`
- 📁 Detects and moves sub-folders into a separate `Folders` directory
- ❓ Files with unknown extensions go into the `Others` folder
- 🧠 Easy to use and modify for custom needs
- 🐍 Written in pure Python — no external dependencies required

---

## 🚀 How It Works

1. You provide the path to the unorganized folder.
2. The script scans each file and folder in that directory.
3. Based on file extensions, it moves them into categorized folders.
4. Any subdirectories are moved into a folder named `Folders`.
5. Unknown file types are moved to an `Others` folder.

---

## 🔧 File Types Handled

| Category      | Extensions |
|---------------|------------|
| Images        | `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`, `.svg`, `.webp` |
| Videos        | `.mp4`, `.mkv`, `.avi`, `.mov` |
| Audio         | `.mp3`, `.wav`, `.flac`, `.aac` |
| Documents     | `.docx`, `.pdf`, `.txt`, `.xlsx`, `.csv`, `.pptx`, `.ppt` |
| Archives      | `.zip`, `.rar`, `.7z`, `.tar`, `.gz` |
| Code Files    | `.py`, `.js`, `.html`, `.php`, `.css`, `.cpp`, `.java`, `.c`, `.json`, `.xml` |
| Executables   | `.exe`, `.msi`, `.apk`, `.bat` |
| Others        | Any unrecognized extensions |
| Folders       | All subdirectories |

---

## 📥 How to Use

```bash
# Step 1: Clone the repo
git clone https://github.com/ShyamChavda005/smart-file-organizer.git

# Step 2: Navigate to the project
cd smart_file_organizer

# Step 3: Run the script
python cleanFiles.py

```

## 🛠️ Requirements
Python 3.x

## 📄 License
This project is licensed under the MIT License.
