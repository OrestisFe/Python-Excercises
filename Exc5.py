'''
Γράψτε ένα πρόγραμμα σε Python το οποίο παίρνει ένα κείμενο από ένα αρχείο και το σπάει σε λεξεις.
Αν οι λέξεις έχουν μήκος πάνω από 3 γράμματα, αφαιρέστε το πρώτο γράμμα και προσθέστε το γράμμα στο τέλος μαζί με το ay.
'''
#Read file
f = open("text.txt", "r")
text = f.read()
f.close()

#Removal of punctuation marks
punctuation_marks = [".", ",", "!", "?", "(", ")", "[", "]", ";", "'"]
text_unmarked = ""
for letter in text:
    if letter not in punctuation_marks:
        text_unmarked += letter

#Rearrange the words list
words = text_unmarked.split(" ")
words_rearranged = []
for word in words:
    if len(word) > 3:
        first_letter = word[0]
        tmp = word[1:]
        tmp = tmp+first_letter+"ay"
        words_rearranged.append(tmp)
    else:
        words_rearranged.append(word)

#Printing data
print(words , "\n\n\n", words_rearranged)
