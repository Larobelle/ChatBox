import os
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names
# Call of the function
directory = "./speeches"
files_names = list_of_files(directory, "txt")


def Extraction_names(files_names):
    """
    Extracts the names of the presidents and puts it in a list
    :param files_names: list
    :return: Nompres1
    """""
    Nompres1 = []
    for i in range (len(files_names)) :
        Ltemp = []
        str=""
        for j in range (len(files_names[i])):
            Ltemp.append(files_names[i][j])
        for k in range (11):
            Ltemp.pop(0)
        for l in range (4):
            Ltemp.pop(-1)
        if not(Ltemp[-1] == "1" or Ltemp[-1] == "2"):
            for m in range(len(Ltemp)):
                str=str+Ltemp[m]
            Nompres1.append(str)
        elif Ltemp[-1] == "1":
            for m in range(len(Ltemp)-1):
                str=str+Ltemp[m]
            Nompres1.append(str)
    return Nompres1

def Association_1stnames (Nompres1):
    Nompres2 = []
    Nompres1=Extraction_names(files_names)
    for elmt in Nompres1 :
        if elmt == "Chirac" :
            elmt = "Jacques " + elmt
            Nompres2.append(elmt)
        elif elmt == "Giscard dEstaing" :
            elmt = "Valéry " + elmt
            Nompres2.append(elmt)
        elif elmt == "Hollande" or elmt == "Mitterrand":
            elmt = "François " + elmt
            Nompres2.append(elmt)
        elif elmt == "Macron" :
            elmt = "Emmanuel " + elmt
            Nompres2.append(elmt)
        elif elmt == "Sarkozy" :
            elmt = "Nicolas " + elmt
            Nompres2.append(elmt)

    return (Nompres2)

nomprez= Extraction_names(files_names)
nomprez2=Association_1stnames(nomprez)
print(nomprez2)
