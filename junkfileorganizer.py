

import argparse
from abc import ABC, abstractmethod
import os
import shutil
import stat
import time
import datetime


class Main(ABC):

    # abstract method
    @abstractmethod
    def fileOrganizer(self, directory):
        pass

    def createDestination(self, cwd, foldername, content):

        organized_path = os.path.join(cwd, "organized")

        if not os.path.exists(organized_path):
            os.mkdir(organized_path)
        destination_path = os.path.join(organized_path, foldername)

        if not os.path.exists(destination_path):
            os.mkdir(destination_path)

        try:

            shutil.copy2(content, destination_path)
            dest = os.path.join(destination_path, content)
            if os.path.exists(dest):
                os.remove(content)
                for (_path, _dirs, _files) in os.walk(cwd, topdown=False):
                    if _files:
                        continue    # skip remove
                    try:
                        os.rmdir(_path)
                    #  if directry has content
                    except OSError:
                        pass
        # if the file is already there
        except OSError:
            pass


class OrganizeBySize(Main):

    def fileOrganizer(self, directory):

        cwd = directory
        for root, sub, contents in os.walk(cwd):
            for content in contents:

                content = os.path.join(root, content)
                if os.path.isfile(content):

                    size = os.stat(content).st_size
                    # <20
                    if size < 20480:
                        file_size = "SMALL"

                    # 20-100KB
                    if size > 20481 and size < 102400:
                        file_size = "MEDIUM"

                    # 100 -500 KB
                    if size > 102401 and size < 512000:
                        file_size = "LARGE"

                    # 500 -2500 KB
                    if size > 512001 and size < 2560000:
                        file_size = "HUGE"

                    # above 2500
                    if size > 2560001:
                        file_size = "MASSIVE"
                    self.createDestination(cwd, file_size, content)


class OrganizeByDate(Main):

    def fileOrganizer(self, directory):
        cwd = directory
        for root, sub, contents in os.walk(cwd):
            for content in contents:
                content = os.path.join(root, content)
                if os.path.isfile(content):
                    # file_loc = os.path.abspath(content)
                    file_stats = os.stat(content)
                    modified_time = time.ctime(file_stats[stat.ST_MTIME])
                    # modified_time = time.ctime (file_stats[stat.ST_ATIME])
                    today = datetime.date.today()
                    yesterday = today - datetime.timedelta(days=1)

                    if modified_time[0:10] == today.ctime()[0:10]:
                        folder_name = "TODAY"
                    elif modified_time[0:10] == yesterday.ctime()[0:10]:
                        folder_name = "YESTERDAY"

                    elif modified_time[4:7] == today.ctime()[4:7] and \
                            modified_time[20:24] == today.ctime()[20:24]:
                        folder_name = "THIS MONTH"

                    elif modified_time[20:24] == today.ctime()[20:24]:
                        folder_name = modified_time[4:7] + \
                            "-" + modified_time[20:24]

                    else:
                        folder_name = modified_time[20:24]
                    self.createDestination(cwd, folder_name, content)


class OrganizeByExtn(Main):

    DIRECTORIES = {
        "PDF":
            [".pdf"],
        "EXE":
            [".exe"],
        "XML":
            [".xml"],
        "SHELL":
            [".sh"],
        "SSI":
            [".shtml"],
        "PYTHON":
            [".py"],
        "JAVA":
            [".java", ".jar", ".jsp", ".jspx", ".wss", ".do", ".action"],
        "JAVA_SCRIPT":
            [".js"],
        "C++":
            [".cpp"],
        "C":
            [".c"],
        "HTML":
            [".html5", ".html", ".htm", ".xhtml"],
        "CSS":
            [".css"],
        "PHP":
            [".php", ".php4", ".php3", ".phtml", ".phps"],
        "IMAGES":
            [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg",
                ".svg", ".heif", ".psd"],
        "VIDEOS":
            [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob",
                ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
        "DOCUMENTS":
            [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf",
                ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx",
                ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd",
                ".xls", ".xlsx", ".ppt", "pptx"],
        "ARCHIVES":
            [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                ".dmg", ".rar", ".xar", ".zip"],
        "AUDIO":
            [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p",
                ".mp3", ".msv", "ogg", "oga", ".raw", ".vox", ".wav",
                ".wma"],
        "TEXT":
            [".txt", ".in", ".out"]
        }

    FILE_FORMATS = {
        file_format: directory
        for directory, file_formats in DIRECTORIES.items()
        for file_format in file_formats
        }

    def fileOrganizer(self, directory):
        cwd = directory
        for root, sub, contents in os.walk(cwd):
            for content in contents:
                file_format = os.path.splitext(content)[1].lower()
                content = os.path.join(root, content)
                if os.path.isfile(content):
                    if file_format in self.FILE_FORMATS:
                        folder_name = self.FILE_FORMATS[file_format]
                    else:
                        folder_name = "OTHER_FILES"
                    self.createDestination(cwd, folder_name, content)


class OrganizeByName(Main):

    def fileOrganizer(self, directory):
        cwd = directory
        for root, sub, contents in os.walk(cwd):
            for content in contents:
                content_name = content
                content = os.path.join(root, content)
                if os.path.isfile(content_name):
                    folder_name = content_name[0].upper()
                self.createDestination(cwd, folder_name, content_name)


if __name__ == "__main__":

    ap = argparse.ArgumentParser()

    ap.add_argument("-d", "--directory", default=os.getcwd(),
                    help="The directory name which you want to organize")
    ap.add_argument("-o", "--option", default="date",
                    help="Different options [date,size,extn,alph]")

    args = vars(ap.parse_args())
    option = str(args["option"])
    directory = str(args["directory"])

    if not os.path.exists(directory):
        exit("Directory does not exist")

    elif option == "date":
        organizeByDate = OrganizeByDate()
        organizeByDate.fileOrganizer(directory)

    elif option == "size":
        organizeBySize = OrganizeBySize()
        organizeBySize.fileOrganizer(directory)

    elif option == "extn":
        organizeByExtn = OrganizeByExtn()
        organizeByExtn.fileOrganizer(directory)

    elif option == "alph":
        organizeByName = OrganizeByName()
        organizeByName.fileOrganizer(directory)
    else:
        exit("Please give correct option[alph,ext,date,size]")
