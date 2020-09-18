# Junk File Organizer
### Introduction
Being a programmer, I always keep the files which I make /download for further reference. But rarely we use those old files; instead, we create a new file or download.
The reason behind that it is a tedious task to find the required file from an unorganized folder. 
So I developed the file organizer program to arrange the directories as per the requirement of the user (arrange by size, date, file extension, or the first alphabet of the file)
### Build using
1. Python 3.8 latest version python language. 

2. The code is built according to the standerd pep8 rules and regulations. 

3. We have to import the argparse,stat,datetime,time,shutil and os modules for this. 

4. Build and tested on windows 10
### Prerequisites
•	python 3.8 (Install this from the  official website https://www.python.org/)

•	Basic knowledge of how to use command prompt, how to copy and paste files .
### Product Features
With this project we can organize the files based on size, modified date, extension and alphabets.
It is a Python script that comes in handy and returns a folder “Organiser” where all the files are organized in a well-manner within seconds. 
It organizes by size(size), last modified date(date), extensions(extn) or alphabetically(alph).

You can run the project from command line , the directory and the option you can pass as arguments.

•	If user is not entering any directory and/or option then by default it will take Current working directory as the directory  and/or date as the option.

•	User can get the different arguments and its details with --help or -h.
      ie, python junkfileorganizer.py  -h
#### By Modified Date
If the user select date  option from command line. Then,
An “organized” folder will be created inside the directory.

Inside that the files will be organised in different folders as , TODAY,YESTURDAY,THIS MONTH, <month>-<current-year>,<Previous - Years>

This will happen recursively[for any folders inside another]
#### By Extension
It creates a parent folder "Organiser" inside the current directory. 
First take user input, If the user input is extn, then program checks for each file extension of each file .
Then according to the category in which it falls creates the folder inside parent folder 
ex: if pdf file it creates PDF directory,copies file there and delete old file. In the same manner it checks for every file inside that directory. 
#### By Size
If the user selects “size” then program check the size of the files. 
Then according to the size , the content will be placed on different folders. 
ie, if size is less than 20 KB -SMALL, 20-100KB -  MEDIUM, 100 -500 KB - LARGE, 500 -2500 KB – HUGE, above 2500KB – MASSIVE.
#### By Alphabet
If the user’s selected option is “alpha”, gets the starting alphabet of each file.
Then according to the category in which it falls creates the folder like A ,B,C etc.. and gets copied there and deletes the old file.
### Demo Video
https://drive.google.com/drive/folders/1_BMBBBqlNsOeTyHUH-18X78UmO6oYyD6?usp=sharing
### Screen shots
https://drive.google.com/drive/folders/11hTex4HH__IWc4p2sePCejVn_ngbm58x?usp=sharing
### Steps to run the program
1.	Copy  “junkfileorganizer.py” to your desired location.
2.	Execute the file from command prompt.
python junkfileorganizer.py –d <directory which you want to organize>  -o <option>
option can be size,date,extn,alph
3.	If you are not giving any directory and/or option , then by default system will take current working directory as directory and modified date(date) as option.
