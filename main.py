import os
import collections
from math import log
import string


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
        speech = speech.replace("aª", "e")
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
        dico = collections.Counter(speech)#.most_common(285) #keep the 50 most common words from the speech
        del dico['']
        #dico = collections.OrderedDict(dico)
        dictionary.append(dico)

    return dictionary


def idf(dictionary, dico_general):
    """
    Takes in as a parameter the term frequency of all documents - not finished
    :param dictionary: list
    :param dico_general: list
    :return: idf_word: dict
    """

    list = []
    liste = []
    for elmt in dictionary[0].items():  # creates on big dictionary compiling all the words in the files
        a = elmt[0]
        list.append(elmt[1])
        liste.append(a)
        liste.append([elmt[1]])
    dico_general.append(liste)
    for i in range(1,len(dictionary)-1):
        for element in dictionary[i].items():
            for word in dico_general:
                if element[0] in word[i]:
                    print (element[0], word[0])

    print(dico_general)

    """IDF calculation w/log"""
    """idf_word = {}
    for key, value in dico_general.items(): # transforms the dict of tf (key-val) into an idf with the help from formula
        idf_word[key] = log(len(dictionary) / value)
    #return idf_word   #tf idf c'est tf times idf, le log calcule seulement idf"""

"""
def tf_idf_prez():
    print("To visualise the most common words per presidents, enter the number next to it in the console")
    for i in range(len(noms_presidents2)):
        print(noms_presidents2[i], i)
    choice = int(input("Choice:"))
    if choice == 0 or choice == 4:
        a = int(input("This president has 2 speeches, would you like to visualise the most common words per "
                      "speech (0) or both speeches combined (1)?"))
        if a == 1 and choice == 0:
            dict = []
            dico_final_chirac = {}
            dict.append(dictionary[0])
            dict.append(dictionary[1])
            for i in range(len(dict)):
                for elmt in list(
                        dict[i].items()):  # creates on big dictionary compiling all the words in the files
                    if elmt[0] not in dico_final_chirac:
                        dico_final_chirac[elmt[0]] = elmt[1]
                    else:
                        dico_final_chirac[elmt[0]] += elmt[1]
            p = idf(dict, dico_final_chirac)
            for key, value in p.items():
                for keys, values in m.items():
                    if keys == key and values == 2:
                        print(key)
"""


def tokanization ():
    """
    Processes the question (asked in french) and returns it cleaned
    :return question: string
    """
    question = input("Ask a question in french ! :")
    question = question.lower()  # puts the question in lower case
    for i in range(len(question)):


        """Text Processing = Cleaning"""

        # replace new lines
        question = question.replace("\n", " ")

        # replace apostrophes and commas
        question = question.replace("'", "e ")
        question = question.replace('\x92', " ")
        question = question.replace(',', "")

        # replace accents
        question = question.replace("ã©", "e")
        question = question.replace("ã", "a")
        question = question.replace("a¨", "e")
        question = question.replace("a¹", "u")
        question = question.replace("a®", "i")
        question = question.replace("a‰", "e")
        question = question.replace("a§", "c")
        question = question.replace("aª", "c")
        question = question.replace("\xa0", " ")
        question = question.replace("a¢", "a")
        question = question.replace("a¯", "i")
        question = question.replace("œ", "oe")
        question = question.replace("a€", "a")
        question = question.replace("â", "a")
        question = question.replace("  ", " ")

        # delete numbers and punctuation
        punctuation_num = '''!()[]{}-;:"\,<>`´./?@#$%^&*_~Â° Â«Â»1234567890'''
        question_without_punctuation = ""
        for char in question:
            if char not in punctuation_num:
                question_without_punctuation = question_without_punctuation + char
            else:
                question_without_punctuation = question_without_punctuation + " "

        question = question_without_punctuation

        """Creation of a new file 'Cleaned'"""


    return question

def list_of_question_words(quest):
    """
    to return the list of words in the question
    :param quest: string
    :return words_of_question: list
    """
    words_of_question = []
    words_of_question = quest.split(" ")
    words_of_question.remove("")
    print(words_of_question)
    return words_of_question


def intersection_question_files(a, dict):
    """
    to return all the words that appear in the question AND in the files
    :param a: list
    :param dict: dictionary
    :return: None
    """
    tmp_list = []
    for i in range (len(a)) :
        if a[i] in dict :
            tmp_list.append(a[i])
    print(tmp_list)

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

    answer = 4
    print ("Type 1 if you want the tf-idf of the docs.")
    print ("Type 2 if you want the list of the presidents' names.")
    print("Type 3 to display the most common words in the corpus of texts")
    print("Type 4 to display the least common words in the corpus of texts")
    print("Type 5 to ask a question")
    print("Type 0 to exit the code.")
    m = idf(dictionary, dico_general)

    while answer != 1 or 2 or 3 or 4 or 0 or 5:
        answer = int(input("Choice: "))

        if answer == 1:
            print(m)
        elif answer == 2:
            print(noms_presidents2)
        elif answer ==3:
            for elmt, value in m.items():
                if value < 1:
                    print(elmt)
        elif answer == 4 :
            for elmt, value in m.items() :
                if float(value) > 2:
                    print(elmt, value)
        elif answer == 5 :
            cleaned_question = tokanization()
            list_question = list_of_question_words(cleaned_question)
            intersection_question_files(list_question,dictionary)

        elif answer==0:
            exit()



"""files_names = list_of_files("txt")
noms_presidents = extraction_names(files_names)
noms_presidents2 = association_1st_names(noms_presidents)
dico_general = []
dictionary = (clean_docs_and_tf(files_names))
print(dico_general)

idf(dictionary, dico_general)"""
menu()