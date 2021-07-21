import sys
from loadFile import Load;
from chooseTwo import chooseTwo;

wordList = Load();
#wordList.retrieveFile(file);
file = wordList.run();
count, words = chooseTwo(wordList.words, file, count=2);
print("count: {} words: {} ".format(count, words));