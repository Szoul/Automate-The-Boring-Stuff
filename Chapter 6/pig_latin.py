#! python 3.8.3
#pig_latin : Translate a text (input) into "Pig Latin"

""" 
If a word begins with a consonant or consonant cluster 
(like ch or gr), that consonant or cluster is moved to 
the end of the word followed by ay [vowels ->add "yay" at end]. For Example:
text_sample would turn into: Ymay amenay isyay ALYAY EIGARTSWAY andyay Iyay amyay 4,000 yearsyay oldyay.
"""

text_sample = "My name is AL SWEIGART and I am 4,000 years old."


original_input = input()
text_list = original_input.split(" ")
pig_speak_list = []
pig_speak = ""
vowels = ["a","e","i","o","u"]

for word in text_list:
    if word.isdigit():
        pig_speak_list.append(word)
    if not word.isalpha() and ("." in word or "," in word):
        pig_speak_list.append(word)
    else:
        special_marks_end = ""
        special_marks_start = ""
        while not word.isalpha():       
            if not word[0].isalpha():
                special_marks_start = special_marks_start + word[0]
                word = word[1:]
            if not word[-1].isalpha():
                special_marks_end = word[-1] + special_marks_end
                word = word[:-1]

        if word.isalpha():
            if word.isupper() and len(word) > 1:
                uppercase = True
            else:
                uppercase = False
            if word[0].isupper():
                first_is_uppercase = True
            else:
                first_is_uppercase = False
            word = word.lower()

            if word[0] in vowels:
                word = word + "yay"
            else:
                for x in range (len(word)):
                    if word[x] not in vowels:
                        consonant_cluster_potition = x+1
                    else:
                        break
                word = word[consonant_cluster_potition:] + word[:consonant_cluster_potition]
                word = word + "ay"

            if uppercase == True:
                word = word.upper()
            elif first_is_uppercase == True:
                word = word[0].upper() + word[1:]
            
            word = special_marks_start + word + special_marks_end
            pig_speak_list.append(word)



pig_speak = " ".join(pig_speak_list)
print(pig_speak)


#todo
    #turn in input (DONE)
    #Split text into list (DONE)
    #--> new list for "Pig-Speak" (DONE)
    #check if each list item  is starting with vowel or consonant (DONE)
    #   if vowel add "yay"; (DONE) 
    #       if consonant(-cluster) put cluster at end and add "ay"  (DONE)
    #       a consonant cluster == all consonants until first vowel (DONE)
    #if word starts with uppercase -> changed word starts with uppercase (DONE)
    #if word isuppercase -> stay uppercase (DONE)
    #if isdigit -> stay the same    (DONE)
    #look for any possible mistakes, like double(or more) spacebars; words with "-" in them; single digit words(DONE)
        #words with upper and lowercase on random potitions... AND HOW TO DEAL WITH THEM (if not explicetly named in how pig-latin works)
        #CONCLUSION: FAULTY GRAMMAR OR SPE-CIAL USE OF LANGUAGE MEANS CODE WON'T WORK/IGNORES THE WORD (moreorlessDONE) - because too many possible exeptions and nothing (really) to learn from it
    #if it contains punctuation marks [./!/?/...] or quotation marks ["",''] let them stay at their intended potition (DONE)
        #how-to: both are not included through .isalpha() ; since these marks are only at beginning or end of a word -> word[0] and word[-1] if QM or just word[-1] if PM
    #re-join them into string and return string/print string (DONE)

    #Look up and collect all possible/neccesary methods to identify certain strings
    #and how to efficiently manipulate strings (at any potition) <-- slices
