import os
import shutil

files_type = {
    "Images": ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.webp'],
    "Videos": ['.mp4', '.mkv', '.avi', '.mov'],
    "Audio": ['.mp3', '.wav', '.flac', '.aac'],
    "Documents": ['.docx', '.pdf', '.txt', '.xlsx', '.csv', '.pptx', '.ppt'],
    "Archives": ['.zip', '.rar', '.7z', '.tar', '.gz'],
    "Code": ['.py', '.js', '.html', '.php', '.css', '.cpp', '.java', '.c', '.json', '.xml'],
    "Executables": ['.exe', '.msi', '.apk', '.bat'],
}

folder_path = input("Enter Path to Organized : ")

for filename in os.listdir(folder_path):
    # print(filename)

    file_path = os.path.join(folder_path,filename)

    if os.path.isdir(file_path):
        folders = os.path.join(folder_path,"Folders")
        if not os.path.exists(folders) :
            os.makedirs(folders)
        shutil.move(file_path,os.path.join(folders,filename))
        continue

    _,ext = os.path.splitext(filename)
    # print(ext)

    move = False
    for category,extensions in files_type.items() :
        # print(category)
        # print(extensions)
        if ext.lower() in extensions :
            
            category_path = os.path.join(folder_path,category)
            if not os.path.exists(category_path) :
                os.makedirs(category_path)
            
            shutil.move(file_path,os.path.join(category_path,filename))
            move = True
            break

    if not move :
        category_path = os.path.join(folder_path,'Others')

        if not os.path.exists(category_path):
            os.makedirs(category_path)

        shutil.move(file_path,os.path.join(category_path,filename))

print(f"✔ path {folder_path} All Files has been SuccessFully Organised..")