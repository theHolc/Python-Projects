import json
from difflib import get_close_matches

# load json file which is stored as dict object 
data = json.load(open("data.json"))

def get_definitions(word):
    if word.lower() in data:
        return data[word.lower()]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        feedback = input("Did you mean %s instead? Y/N: " % get_close_matches(word, data.keys())[0])
        while feedback.lower() != 'y' and feedback.lower() != 'n':
                print("Please enter Y or N")
                feedback = input("Did you mean %s instead? Y/N: " % get_close_matches(word, data.keys())[0])
                if feedback.lower() == 'y' or feedback.lower() == 'n':
                    break
        if feedback.lower() == "y":
            print()
            return data[get_close_matches(word, data.keys())[0]]
        elif feedback.lower() == "n":
            for i in range(1, len(get_close_matches(word, data.keys()))):
                feedback = input("Did you mean %s instead? Y/N: " % get_close_matches(word, data.keys())[i])
                while feedback.lower() != 'y' and feedback.lower() != 'n':
                    print("Please enter Y or N")
                    feedback = input("Did you mean %s instead? Y/N: " % get_close_matches(word, data.keys())[i])
                    if feedback.lower() == 'y' or feedback.lower() == 'n':
                        break
                if feedback.lower() == "y":
                    print()
                    return data[get_close_matches(word, data.keys())[i]]
            print()
            return "Sorry, we can't guess the word you're looking for."
    else:
        return "That word seems like nonsense. Try a new word."

word = input("Enter a word: ")
print()
output = get_definitions(word)

# modify this later to determine if def is a noun verb or adjective
if type(output) == list:
    for i in range(len(output)):
        num = i + 1
        print("Definition %s: " % num + output[i])
        print()
else:
    print(output)