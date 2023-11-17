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
print(files_names)

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

print(Nompres1)

