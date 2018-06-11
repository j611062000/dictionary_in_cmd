from PyDictionary import PyDictionary
from termcolor import colored, cprint
from colorama import init
from sentence import sentence

init()
dictionary=PyDictionary()

while True:

    lookup_word = input("Word: ")
    print()

    result = dictionary.meaning(lookup_word)

    if result != None:

        # definition
        for field in result:
            cprint(field, "red", "on_white")
            print()

            for count, meaning in enumerate(result[field]):
                print("{:>4}. {}".format(count+1, meaning))

            print("\n")

        # sentenc
        cprint("Sentence", "red", "on_white")
        print()
        sentence(lookup_word)

    else:

        print("no words match [{}]".format(lookup_word))

    print("_"*105,"\n")
