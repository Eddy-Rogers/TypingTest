import random

def main():
    file = open("Inputs/commonwords.csv", "r")

    text = file.read()

    wordarray = text.split(',')
    cleanarray = []

    for word in wordarray:
        clean = word[0:word.find("(")-1].strip()

        if len(clean) > 1 and clean.find(" ") == -1 and clean.find(".") == -1:
            cleanarray.append(clean.capitalize())

    random.shuffle(cleanarray)

    wfile = open("./Outputs/CapitalTypingTest.txt", "x")

    for word in cleanarray:
        wfile.write(word + " ")

if __name__ == "__main__":
    main()