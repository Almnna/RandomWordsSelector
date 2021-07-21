# RandomWordsSelector
small project i made to select a random english word from a txt file that contains a bunch of new english words to me
that i came across & saved it into it to check it out later, so when u run it it ask u for the 'source file' that u wanna load the words from it
u can edit the count of the words u want it to return from that file.

[#] it removes the word/s that returned completely from the 'source file' & added to the 'update file' that stores the words that the script 
returns from the 'source file', the default 'update file' is in the project source directory './src/read.txt' u can edit the path to a new
file in the 'chooseTwo.py' script -> 'updateFile' variable, also there is a 'backupFile' variable that points to a a backup file
its set to 'None' as default; so u can provide a certain backup file path
