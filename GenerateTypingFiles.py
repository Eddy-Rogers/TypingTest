import random

configuration_values = [
    ("random_500", "length",500, '', True),
    ("random_1000", "length", 1000, '', True),
    ("random_2000", "length", 2000, '', True),
    ("random_3000", "length", 3000, '', True),
    ("contains_q", "letter", 3000, 'q', True),
    ("contains_p", "letter", 3000, 'p', True)]

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
            case "length":
                if(current_count < configuration[2]):
                    output_files[configuration[0] + "_C"].write(word.capitalize() + " ")
                    output_files[configuration[0] + "_L"].write(word + " ")
            case "letter":
                if(word.find(configuration[3]) != -1):
                    output_files[configuration[0] + "_C"].write(word.capitalize() + " ")
                    output_files[configuration[0] + "_L"].write(word + " ")



def load_clean_file():
    file = open("Inputs/third_of_a_mil.txt", "r")
    text = file.read()

    word_array = text.split('\n')

    for word in word_array:
        clean = word.strip()

        if len(clean) > 1 and clean.find(" ") == -1 and clean.find(".") == -1:
            clean_array.append(clean)

def clean_configuration():
    new_configuration = []
    for configuration in configuration_values:
        if configuration[1]:
            new_configuration.append(configuration)
    return new_configuration

if __name__ == "__main__":
    main()