# changeFileTittle
Automatic  change the file name. Changes the current name to the date of its creation
This is program exctract metadata from mp4 video file.

The program gets the path to the folder with files or the path to the file itself.

When it gets the path to the folder:
1.  Reading the names of all files from the getFilesName(path) folder.
2.  Getting the date and time of video creation get_media_properties(filename).
3. change of file name change_tittle(path,newTittle,oldTittle)

get_media_properties(filename)
Gets the input path to the file. subprocess gets the date of video creation and returns it.

change_tittle(path,newTittle,oldTittle)
Gets the input path to the folder where the file is stored, new file name, old file name.Changes the file name using the rename method

getFilesName(path)
Gets the path to the folder. Returns the list of names of all files in the folder.

changeAllFilesInPath(path):
Gets the path to the folder. Program operation mode. Changes the name of all files in the folder to the date and time of creation of this file.

---

You can use bash script execute file cd_photo.sh. This script move all file highlighted masks to months directory | work in Unix system
Youd should execute file in directory, where is your files, which you want move.
1. Run script
2. write mask for file
3. Wait ...

All files will move to directory based on the time of creation
