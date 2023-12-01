import os
import collections
from math import log, ceil


def list_of_files(extension):
    """
    Extracts name of the files and puts it into a list by going through the directory
    :param extension: .txt
    :return:
    """
    directory = "./speeches"
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def extraction_names(files_names):
    """
    Extracts the names of the presidents and puts it in a list
    :param: files_names = list
    :return: noms_prez1 = list
    """
    noms_prez1 = []
    for i in range(len(files_names)):
        temporary_list = []
        string = ""
        for j in range(len(files_names[i])):  # puts the name of the file into a list by separating every letters
            temporary_list.append(files_names[i][j])
        for k in range(11):  # removes the beginning of the first 11 charters of the list
            temporary_list.pop(0)
        for l in range(4):  # removes the lest 4 characters of the list
            temporary_list.pop(-1)
        if not (temporary_list[-1] == "1" or temporary_list[-1] == "2"):  # transforms from list to str the names of
            # presidents not appearing twice in the folder
            for m in range(len(temporary_list)):  # transforms a list of characters into a str and puts it into a list
                string = string + temporary_list[m]
            noms_prez1.append(string)
        elif temporary_list[-1] == "1":  # transforms from list to str the names of presidents appearing twice in the
            # folder
            for m in range(len(temporary_list) - 1):  # transforms one of the duplicates from the list
                string = string + temporary_list[m]
            noms_prez1.append(string)
    return noms_prez1


def association_1st_names(nompres1):
    """
    Associates a First name to the Last name of the presidents
    :param: nompres1 = list
    :return: nompres2 = list
    """
    nompres2 = []
    for elmt in nompres1:  # switch case for the names
        if elmt == "Chirac":
            elmt = "Jacques " + elmt
            nompres2.append(elmt)
        elif elmt == "Giscard dEstaing":
            elmt = "Valéry " + elmt
            nompres2.append(elmt)
        elif elmt == "Hollande" or elmt == "Mitterrand":
            elmt = "François " + elmt
            nompres2.append(elmt)
        elif elmt == "Macron":
            elmt = "Emmanuel " + elmt
            nompres2.append(elmt)
        elif elmt == "Sarkozy":
            elmt = "Nicolas " + elmt
            nompres2.append(elmt)

    return nompres2


def clean_docs_and_tf(files_names):
    """
    Clean the speeches and saves them in a new folder as well as returns tf in the form of a list of dictionaries
    :param files_names: list
    :return: dictionary: list of dict
    """
    dictionary = []
    for i in range(len(files_names)):  # loop to clean all the docs at once and calculates tf
        directory = "./speeches" + "/" + files_names[i]
        with open(directory, 'r') as f:  # Opens the text files
            speech = f.read().lower()  # puts the speech in lower case

        """Text Processing = Cleaning"""

        # replace new lines
        speech = speech.replace("\n", " ")

        # replace apostrophes and commas
        speech = speech.replace("'", "e ")
        speech = speech.replace('\x92', " ")
        speech = speech.replace(',', "")

        # replace accents
        speech = speech.replace("ã©", "e")
        speech = speech.replace("ã", "a")
        speech = speech.replace("a¨", "e")
        speech = speech.replace("a¹", "u")
        speech = speech.replace("a®", "i")
        speech = speech.replace("a‰", "e")
        speech = speech.replace("a§", "c")
        speech = speech.replace("aª", "c")
        speech = speech.replace("\xa0", " ")
        speech = speech.replace("a¢", "a")
        speech = speech.replace("a¯", "i")
        speech = speech.replace("œ", "oe")
        speech = speech.replace("a€", "a")
        speech = speech.replace("â", "a")
        speech = speech.replace("  ", " ")

        # delete numbers and punctuation
        punctuation_num = '''!()[]{}-;:"\,<>`´./?@#$%^&*_~Â° Â«Â»1234567890'''
        speech_without_punctuation = ""
        for char in speech:
            if char not in punctuation_num:
                speech_without_punctuation = speech_without_punctuation + char
            else:
                speech_without_punctuation = speech_without_punctuation + " "

        speech = speech_without_punctuation

        """Creation of a new file 'Cleaned'"""

        directory = "./clean/"
        with open(directory + "clean_" + files_names[i], 'w') as new_file_cleaned:
            new_file_cleaned.write(speech)  # stores the new cleaned file in the 'clean' folder

        """Dictionaries of words"""
        speech = speech.split(" ")  # transform the text into a dictionary
        dico = collections.Counter(speech)  # .most_common(285) keep the 50 most common words from the speech

        del dico['']  # dico = collections.OrderedDict(dico)
        dictionary.append(dico)

    return dictionary

unimportant_words = []
def idf(dictionary, dico_general):
    """
    Takes in as a parameter the term frequency of all documents
    :param dictionary: list
    :param dico_general: dict
    :return: tf_idf: dict
    """
    for i in range(len(dictionary)):  # takes out one by one the lists of tf of each files
        for elmt in list(dictionary[i].items()):  # creates on big dictionary compiling all the words in the files
            if elmt[0] not in dico_general:
                dico_general[elmt[0]] = elmt[1]
            else:
                dico_general[elmt[0]] += elmt[1]

    """IDF calculation w/log"""
    tf_idf = {}
    for key, value in dico_general.items():  # transforms the dict of tf (key-val) into an idf with the help from formula
        tf_idf[key] = int(round(log(len(dictionary) / value + 1), 0))
    return tf_idf


def menu():
    """
    Temporary menu
    :param  none
    :return: none
    """
    files_names = list_of_files("txt")
    noms_presidents = extraction_names(files_names)
    noms_presidents2 = association_1st_names(noms_presidents)
    dico_general = {}
    dictionary = (clean_docs_and_tf(files_names))

    answer = -1
    print ("Type 1 if you want the tf-idf of the docs.")
    print ("Type 2 if you want the list of the presidents' names.")
    print("Type 0 to exit the code.")
    while answer != 1 or 2 or 0:
        answer = int(input("Choice: "))

        if answer == 1:
            print(idf(dictionary, dico_general))
        elif answer == 2:
            print(noms_presidents2)
        elif answer==0:
            exit()


menu()
