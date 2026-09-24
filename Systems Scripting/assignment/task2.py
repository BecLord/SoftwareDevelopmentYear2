import os
import shutil
import zipfile
# Task 2
# function to accept a string parameter representing a folder name provided by user.
# automate the creation of a folder starting with the name.
# if it exists, delete it and recreate it.
# Inside the folder create two subfolders 'store' and 'keeping'
# In 'Keeping' create 3 subfolders 'pics', 'docs', 'movie'
# In 'docs' 'HUNTING.txt', 'GAMES.txt', 'WHEEL.txt', 'ARROW.txt', 'CROSSBAR.txt'
# Add content and 2 subfolders 'work', 'play'

# Second function to rename all the files in 'docs' to lowercase
# make sure the folder exists first and do not change the subfolders

# third function archive the 'docs' folder using Python zipefile module
# create 5 backip archives in the top-level 'store' folder
# output the content of the store folder & one of the zip archives for verification

def folder(folder_name):
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name) #delete folder
        os.makedirs(folder_name) #create folder
    else:
        os.makedirs(folder_name) #create folder
    
    #create subfolders
    os.makedirs(os.path.join(folder_name, "store"))
    os.makedirs(os.path.join(folder_name, "keeping"))

    #keeping subfolders
    os.makedirs(os.path.join(folder_name, "keeping", "pics"))
    os.makedirs(os.path.join(folder_name, "keeping", "docs"))
    os.makedirs(os.path.join(folder_name, "keeping", "movie"))

    #text files in docs
    with open(os.path.join(folder_name, "keeping", "docs", "HUNTING.txt"), "w") as hunting_file:
        hunting_file.write("Hello")
    with open(os.path.join(folder_name, "keeping", "docs", "GAMES.txt"), "w") as games_file:
        games_file.write("Hello")
    with open(os.path.join(folder_name, "keeping", "docs", "WHEEL.txt"), "w") as wheel_file:
        wheel_file.write("Hello")
    with open(os.path.join(folder_name, "keeping", "docs", "ARROW.txt"), "w") as arrow_file:
        arrow_file.write("Hello")
    with open(os.path.join(folder_name, "keeping", "docs", "CROSSBAR.txt"), "w") as crossbar_file:
        crossbar_file.write("Hello")

    #subfolders in docs
    os.makedirs(os.path.join(folder_name, "keeping", "docs", "work"))
    os.makedirs(os.path.join(folder_name, "keeping", "docs", "play"))



def lowercase(folder_name):
    docs_files = os.path.join(folder_name, "keeping", "docs") #path to docs folder

    if not os.path.exists(docs_files):
        print(docs_files, " folder does not exist")
        return

    for filename in os.listdir(docs_files):
        filename_path = os.path.join(docs_files, filename)

        if os.path.isdir(filename_path):
            continue
        
        rename = filename.lower() #make file names lowercase
        rename_path = os.path.join(docs_files, rename)

        if filename != rename:
            os.rename(filename_path, rename_path) #rename file if name changed


def archive(folder_name):

    docs_folder = os.path.join(folder_name, "keeping", "docs")
    store_folder = os.path.join(folder_name, "store")

    if not os.path.exists(docs_folder):
        print(docs_folder, "folder does not exist")
        return
    
    main_archive = os.path.join(store_folder, "docs_backup.zip") #main zip

    os.makedirs(store_folder, exist_ok=True)   

    with zipfile.ZipFile(main_archive, "w", zipfile.ZIP_DEFLATED) as zip:
        for root, subfolders, files in os.walk(docs_folder):
            for filename in files:
                file_path = os.path.join(root, filename)
                archived = os.path.relpath(file_path, docs_folder)
                zip.write(file_path, archived) 
            
        print("Main archive created")
    
    backup1 = os.path.join(store_folder, "docs_backip1.zip") #backup 1
    shutil.move(main_archive, backup1) 

    for backup in range(2, 6):
        backup_path = os.path.join(store_folder, f"docs_backup_{backup}.zip")
        shutil.copy(backup1, backup_path)

    print("Store Folder: ")
    for i in os.listdir(store_folder):
        print(" ", i)

    print("first backup zip: ", backup1)
    with zipfile.ZipFile(backup1, "r") as zip_read:
        for archived in zip_read.namelist():
            print(" ",archived)
    

folder_name = input("What is the name of the folder you want to create? ")
folder(folder_name)
lowercase(folder_name)
archive(folder_name)

#I created the folder function and made the folder_name a input from the user.
#I then created the if statement to see if a folder with that name existed and if it did I used shutil.rmtree() to delete it
#next I created the folder using os.makedirs(). 
#I created 2 subfolders store and keeping using the os.paath.join and os.makedirs() function.
#and repeated the same for the keeping subfolders.
#then i created the 5 text files inside the docs folder.
#I then set their file type to "w" to be able to write to the files.
#then i created the final two subfolders work and play

#for the second function I once again checked if the folders existed
#then i used a for loop to go through all the folders in the docs folder and use the .lower function on each one.

#the last function archive checks agaon if the docs folder exists and if so create a backip zip file for it inside the store folder.
#i used a loop to create 4 more backups.
#print each filename so that we can see archived files

#References
#Python Standard Library - os, shutil, zipfile
#GeeksforGeeks os.path.join
#GeeksforGeeks os.listdir()