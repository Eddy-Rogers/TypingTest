import random

configuration_values = [
    ("random_500", "length",500, '', True, ""),
    ("random_1000", "length", 1000, '', True, ""),
    ("random_2000", "length", 2000, '', True, ""),
    ("random_3000", "length", 3000, '', True, ""),
    ("contains_q", "letter", 3000, 'q', True, ""),
    ("contains_p", "letter", 3000, 'p', True, ""),
    ("left_hand", "analysis", 80, '', True, "left"),
    ("right_hand", "analysis", 80, '', True, "right")]

leftrighthand = {'q': "left",
'w': "left",
'e': "left",
'r': "left",
't': "left",
'a': "left",
's': "left",
'd': "left",
'f': "left",
'g': "left",
'z': "left",
'x': "left",
'c': "left",
'v': "left",
'b': "left",
'y': "right",
'u': "right",
'i': "right",
'o': "right",
'p': "right",
'h': "right",
'j': "right",
'k': "right",
'l': "right",
'n': "right",
'm': "right" }
p_output = "./Outputs/"

clean_array = []
output_files = dict()

def main():
    load_clean_file()
    initialize_output_files()

    random.shuffle(clean_array)

    current_count = 1

    for word in clean_array:
        populate_files(current_count, word)
        current_count += 1

def initialize_output_files():
    for configuration in clean_configuration():
        output_files[configuration[0] + "_C"] = open(p_output + configuration[0] + "_Capital.txt", "x")
        output_files[configuration[0] + "_L"] = open(p_output + configuration[0] + "_Lowercase.txt", "x")

def populate_files(current_count, word):
    for configuration in configuration_values:
        match configuration[1]:
            # Add words to the file until a certain length is achieved
            case "length":
                if(current_count < configuration[2]):
                    output_files[configuration[0] + "_C"].write(word.capitalize() + " ")
                    output_files[configuration[0] + "_L"].write(word + " ")
            # Add words to the file because they have a certain letter
            case "letter":
                if(word.find(configuration[3]) != -1):
                    output_files[configuration[0] + "_C"].write(word.capitalize() + " ")
                    output_files[configuration[0] + "_L"].write(word + " ")
            # Perform some analysis on the word, and only accept certain words that meet the configured threshold
            case "analysis":
                if(perform_analysis(word, configuration[5]) >= configuration[2]):
                    output_files[configuration[0] + "_C"].write(word.capitalize() + " ")
                    output_files[configuration[0] + "_L"].write(word + " ")

def load_clean_file():
    file = open("Inputs/words", "r")
    text = file.read()

    word_array = text.split('\n')

    for word in word_array:
        clean = word.strip()

        # Cleaning the File
        if (len(clean) > 1
                and clean.find(" ") == -1
                and clean.find(".") == -1)\
                and not clean[0].isupper()\
                and clean.find("'") == -1:
            clean_array.append(clean)

def clean_configuration():
    new_configuration = []
    for configuration in configuration_values:
        if configuration[1]:
            new_configuration.append(configuration)
    return new_configuration

def perform_analysis(word, configuration):
    acceptablechars = 0
    matchingchars = 0
    match configuration:
        case "left":
            for letter in word:
                if letter in leftrighthand:
                    acceptablechars += 1
                    if leftrighthand[letter] == "left":
                        matchingchars += 1

        case "right":
            for letter in word:
                if letter in leftrighthand:
                    acceptablechars += 1
                    if leftrighthand[letter] == "right":
                        matchingchars += 1

    return (matchingchars / acceptablechars) * 100

if __name__ == "__main__":
    main()