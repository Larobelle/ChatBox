import os


def list_of_files(directory, extension):
    """
    Extracts name of the files and puts it into a list
    :param directory: dir
    :param extension: .txt
    :return:
    """
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


# Call of the function
directory = "./speeches"
files_names = list_of_files(directory, "txt")


def extraction_names(files_names):
    """
    Extracts the names of the presidents and puts it in a list
    :param: files_names = list
    :return: noms_prez1 = list
    """""
    noms_prez1 = []
    for i in range(len(files_names)):
        Ltemp = []
        str = ""
        for j in range(len(files_names[i])):
            Ltemp.append(files_names[i][j])
        for k in range(11):
            Ltemp.pop(0)
        for l in range(4):
            Ltemp.pop(-1)
        if not (Ltemp[-1] == "1" or Ltemp[-1] == "2"):
            for m in range(len(Ltemp)):
                str = str + Ltemp[m]
            noms_prez1.append(str)
        elif Ltemp[-1] == "1":
            for m in range(len(Ltemp) - 1):
                str = str + Ltemp[m]
            noms_prez1.append(str)
    return noms_prez1


def association_1st_names(nompres1):
    """
    Associates a First name to the Last name of the presidents
    :param: Nompres1 = list
    :return: Nompres2 = list
    """
    nompres2 = []
    for elmt in nompres1:
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


noms_presidents = extraction_names(files_names)
noms_presidents2 = association_1st_names(noms_presidents)
print(noms_presidents2)
