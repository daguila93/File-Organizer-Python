from pathlib import Path
import pathlib

scriptName = 'fileOrganizer.py' #Script`s name to ignore
currentPath = Path.cwd() #get the script`s current path

def fileOrganizer(currentPath, scriptName):
    #Create all the directories with the file`s extension
    for child in currentPath.iterdir():
        if(child.is_file() and child.name != scriptName):
            fileExtension = child.suffix.replace('.', '')
            pathlib.Path(currentPath).joinpath(fileExtension, '').mkdir(parents=True, exist_ok=True)

    #Move all the files to their respectives folders
    for child in currentPath.iterdir():
        if (child.is_file() and child.name != scriptName):
            fileExtension = child.suffix.replace('.', '')
            fileFullpath = pathlib.Path(currentPath).joinpath(pathlib.Path(child).name)
            fileDestination = pathlib.Path(currentPath).joinpath(fileExtension, pathlib.Path(child).name)
            #if the file already exists on destination, it will not move.
            if(not fileDestination.is_file()):
                pathlib.Path.rename(fileFullpath, fileDestination)

fileOrganizer(currentPath, scriptName)
