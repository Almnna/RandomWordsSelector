import sys, os;
from mnnakit import return_file_name;
from time import sleep
from datetime import date

class Load(object):
    def __init__(self, file=""):
        self.file = file
        self.file_name = None
        self.words_filter = []
        self.words = []
    
    def run(self, file=None):
        if(self.file == "" or self.file == None):
            self.file = input("# please enter words file full path ('Q' -> quit): ")
            if (self.file == 'Q' or self.file == 'q'):
                sys.quit();
            elif self.file == "":
                self.run(self.file)
            else:
                self.load()
                self.retrieveFile()
                return str(self.file);
        else:
            self.load();
            self.retrieveFile()
            return str(self.file);

    def load(self):
        if(os.path.isfile(self.file)):
            self.file_name = return_file_name(self.file);
            print("# file {name} is found!".format(name=self.file_name))
            print("# extracting words !");
        else:
            print("file {file} doesn't exist  or incorrect path !!!".format(file=return_file_name(self.file)))
            sys.exit()

    def divider(self, index_str, index):
        if index > 0 and index_str[0] != '0':
            if len(index_str) == 1:
                if index_str[0] == '5':
                    self.words.append("\n")
            elif len(index_str) == 2:
                if index_str[1] == '0' or index_str[1] == '5':
                    self.words.append("\n")
            elif len(index_str) == 3:
                if index_str[2] == '0' or index_str[2] == '5':
                    self.words.append("\n")

    def retrieveFile(self):
        if(os.path.isfile(self.file)):
            words_file = open(self.file, 'r+')
            words_list = words_file.readlines()

            for index, word in enumerate(words_list):
                if word != "\n" and word != "":
                    self.words_filter.append(word.rstrip("\n"))

            self.words = []
            for index, word in enumerate(self.words_filter):
                index_str = str(index)
                self.words.append(word.rstrip("\n"))
                self.divider(index_str, index)

            words_file.close();
            print("# file %s is fully loaded"%(self.file_name))

    def updateFile(self, words, file, overwrite=False, time=False):
        if overwrite:
            newFile = open(file, 'w+')
        else:
            newFile = open(file, 'a+')
        newFile.write('\n\n')
        if(time):
            newFile.write("\n{t} \n\n".format(t=date.today()))
        for word in words:
            newFile.write(word + '\n')
        newFile.close()