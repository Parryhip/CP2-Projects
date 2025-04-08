#Samuel Andelin, Pig Latin Converter
def switch(word):
    newword = []
    if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
        newword.append(word)
        newword.append("way")
    else:
        wordlist = []
        for i in word:
            wordlist.append(i)
        while True:
            if  wordlist[0] != "a" and wordlist[0] != "e" and wordlist[0] != "i" and wordlist[0] != "o" and wordlist[0] != "u":
                wordlist.append(wordlist[0])
                del wordlist[0]
            else:
                newword.append("".join(wordlist))
                newword.append("ay")
                break
    return newword
wordtochange = input("What word should I switch to piglatin?")
newword = switch(wordtochange)
newwordtostring = "".join(newword)
print(newwordtostring)