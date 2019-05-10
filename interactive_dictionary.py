import json
from difflib import get_close_matches

# if the dataset is in the working directory of python file, we can open dataset directly by using open(dataset name)
# method. otherwise entire path has to be included in the parenthesis.
dataset = json.load(open("dataset.json"))


def meaning(w):
    w = w.lower()   # lower() method is used to convert input to lowercase string: apple
    if w in dataset:
        return dataset[w]
    elif w.upper() in dataset:  # upper() method is used to convert input to uppercase string: APPLE
        return dataset[w.upper()]
    elif w.title() in dataset:  # title() method is used to convert input to string with first letter capitalized: Apple
        return dataset[w.title()]
    elif len(get_close_matches(w, dataset.keys())) > 0:
        key = input("Did you mean {0} instead? Enter 0 if yes, or 1 if no: ".format(get_close_matches(w, dataset.keys())[0]))
        if key == "0":
            return dataset[get_close_matches(w, dataset.keys())[0]]
        elif key == "1":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter word: ")
output = meaning(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
