import random, re
from loadFile import Load
from mnnakit import  CusExceptions, return_file_name

two = [] 

updateFile = './src/read.txt';
backupFile = None

def containsNum(s):
    return bool(re.search(r'\d', s))



def chooseTwo(words, file, count):
    global two, updateFile, backupFile;

    wordList = Load();

    count -= 1; #cuz index start at 0 aka count -> 1 == 2 elements 
    counter = 0;
    try:
        while counter <= count:
            if(len(words) < 1):
                wordList.updateFile(words, file, overwrite=True)
                raise CusExceptions.EmptyList("Source words list is empty!!");
                break
            
            word = words.pop(random.randrange(len(words)))
            if word == "\n" or containsNum(word):
                continue

            two.append(word);
            counter += 1;
    except Exception as e:
        print("{error} -> list size: {size} | list: {array}".format(error=e, size=counter, array=two))
        return counter, two;

    print("# words -> {words} (removed from {f1} & added to {f2})!".format(words=two, f1=return_file_name(file), f2=return_file_name(updateFile)))
    wordList.updateFile(words, file, overwrite=True)#update (overwrite it with the current words list) source file
    wordList.updateFile(two, updateFile, time=True)#update storing file
    if not None:
        wordList.updateFile(two, backupFile, time=True)
    return counter, two;


