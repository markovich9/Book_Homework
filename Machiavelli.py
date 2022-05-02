import certifi
import ssl
from urllib.request import urlopen
url = "https://gutenberg.org/files/1232/1232-0.txt"
local_name = "prince.txt"
#The same code will be applied to this book as it was to the first one
#This way we will determine which author had more distinct words
def save_locally():
    with open(local_name, "w") as local_fp:
        with urlopen(url, context = ssl.create_default_context(cafile=certifi.where())) as fp:
            for line in fp:
                line = line.decode("utf-8-sig").replace("\n","")
                local_fp.write(line)

punctuation = ",;!.?-()"
def find_unique_words():
    unique_words = {}
    with open(local_name) as fp:
        for line in fp:
            for p in punctuation:
                line = line.replace(p, " ")
            line = line.lower()
            # This is how we remove the punctuation from the text
            for word in line.split():
                unique_words[word] = unique_words.get(word, 0) + 1
            #And here we find the unique words
    return unique_words

save_locally()
unique_words = find_unique_words()
most_frequent = list(unique_words.values())
most_frequent.sort(reverse=True)
print(most_frequent)
for word_frequency in most_frequent[0:]:
    for unique_word, value in unique_words.items():
        if word_frequency == value:
            print(f"common word '{unique_word}' appears {value} times")
            #To ensure we don't get the same value if there are more words with the same frequency
            unique_words[unique_word] = -1
            break
print(len(unique_words))
file = open("prince.txt", "r")
read_data = file.read()
per_word = read_data.split()
print(len(per_word))
#We can clearly see that Machiavelli has almost 2,000 more unique words than Lewis Carrol
#This is not surprising as Alice in Wonderland is a simplistic children's book
#And Machiavelli's work is more serious and existential
print(53045/5809)
#dividing the total number and the number of unique words gives us 9.13
print(29594/3814)
#doing the same for the 1st book gives us 7.76
#in all cases, this leads us to a conclusion that Machiavelli has a wider vocabulary
#This is an expected result considering the types of books analysed



