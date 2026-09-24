#import os - to work with folders and files
#import shutil - delete folders and copy files
#import zipfile - create zip archives
#Define a function to set up the folder structure
#if the folder exists, delete it - shutil.rmtree
#create the main folder and subfolders - os.makedirs
#create a list of 5 file names and 5 file contents
#for each file, create a text file in docs and write the content
#rename files in docs to lowercase - function make_files_lowercase
#list all files in docs - os.listdir
#for each file, check if its a file - os.path.isfile
#split the name and extensions, make them lowercase and then rename them - os.rename
#create a zip archive of docs - zipfile.ZipFile
#for each file in docs, add it to the zip
#make 4 more backup copies of the zip - shutil.copy
#print the list of files in store - os.listdir
#print the contents of one zip archive - zipfile.Zipfile.printdir
#Lecture notes, GeeksforGeek - os module in python with examples, shutil module in python, working with zip files in python

import os
import shutil
import zipfile

def setup_game_folder(game_folder):
    if os.path.exists(game_folder):
        shutil.rmtree(game_folder)

    os.makedirs(os.path.join(game_folder, "store"))
    os.makedirs(os.path.join(game_folder, "keeping", "pics"))
    os.makedirs(os.path.join(game_folder, "keeping", "docs", "work"))
    os.makedirs(os.path.join(game_folder, "keeping", "docs", "play"))
    os.makedirs(os.path.join(game_folder, "keeping", "movie"))

    docs_folder = os.path.join(game_folder, "keeping", "docs")
    
    file_names = ["HUNTING.txt", "GAMES.txt", "WHEEL.txt", "ARROW.txt", "CROSSBAR.txt"]
    file_contents = [
        "This is the hunting file.",
        "Games are fun and relaxing.",
        "Wheels spin round and round.",
        "An arrow is sharp and fast.",
        "Crossbars are strong."
    ]

    for i in range(5):
        with open(os.path.join(docs_folder, file_names[i]), "w") as f:
            f.write(file_contents[i])

def make_files_lowercase(game_folder):
    docs_folder = os.path.join(game_folder, "keeping", "docs")
    for filename in os.listdir(docs_folder):
        old_path = os.path.join(docs_folder, filename)
        if os.path.isfile(old_path):
            file_title, file_extension = os.path.splitext(filename)
            new_path = os.path.join(docs_folder, file_title.lower() + file_extension)
            os.rename(old_path, new_path)
            
def zip_and_backup(game_folder):
    docs_folder = os.path.join(game_folder, "keeping", "docs")
    store_folder = os.path.join(game_folder, "store")
    main_zip = os.path.join(store_folder, "docs_backup.zip")
    with zipfile.ZipFile(main_zip, "w") as zipf:
        for foldername, subfolders, files in os.walk(docs_folder):
            for file in files:
                file_path = os.path.join(foldername, file)
                name_in_zip = os.path.relpath(file_path, docs_folder)
                zipf.write(file_path, name_in_zip)
    for i in range(1, 5):
        shutil.copy(main_zip, os.path.join(store_folder, f"docs_backup_copy{i}.zip"))

    print("\nStore folder has these files:")
    for thing in os.listdir(store_folder):
        print(thing)
    print("\nFiles inside zip file:")
    with zipfile.ZipFile(main_zip, "r") as zipf:
        zipf.printdir()

game_folder_name = input("What should the main folder be called? ")
setup_game_folder(game_folder_name)
make_files_lowercase(game_folder_name)
zip_and_backup(game_folder_name)
