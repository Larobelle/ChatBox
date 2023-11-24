import os
import collections


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
        if not (temporary_list[-1] == "1" or temporary_list[
            -1] == "2"):  # transforms from list to str the names of presidents not appearing twice in the folder
            for m in range(len(temporary_list)):
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


def clean_docs(files_names): #    Clean the speeches and put them into a new folder as well as collects the 50 most recurrent words
    """

    :param files_names: list
    :return: dictionary: list
    """
    dictionary=[]
    for i in range (len(files_names)):
        directory = "./speeches"+"/"+files_names[i]
        with open(directory, 'r') as f:  # Opens the text files
            speech = f.read().lower()

        """Text Processing = Cleaning"""

        # replace new lines
        speech = speech.replace("\n", " ")

        # replace apostrophes and commas
        speech = speech.replace("'", " ")
        speech = speech.replace('\x92', " ")
        speech = speech.replace(',', "")

        #replace accents
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

        #numbers and puntuation
        ponctuations_num = '''!()[]{}---;:"\,<>`´./?@#$%^&*_~Â° Â«Â»1234567890'''
        pas_ponct = ""
        for char in speech:
            if char not in ponctuations_num:
                pas_ponct = pas_ponct + char
            else:
                pas_ponct = pas_ponct + " "

        speech = pas_ponct

        """Creation of a new file 'Cleaned'"""

        directory = "./clean"
        with open(directory+files_names[i]+"_clean", 'w') as new_file_cleaned:
            new_file_cleaned.write(speech)

        """List of the most 50 most recurrent words"""

        speech = speech.split(" ")
        dico = collections.Counter(speech)  # keep the 50 most common words from the speech
        dico = collections.OrderedDict(dico)
        dictionary.append(dico)
    return dictionary



# Call of the functions
files_names = list_of_files("txt")
noms_presidents = extraction_names(files_names)
noms_presidents2 = association_1st_names(noms_presidents)
print(clean_docs(files_names))