import os


#IT IS EASIEST TO PUT THIS SCRIPT DIRECTLY OUTSIDE OF THE FOLDER YOU WANT TO WORK WITH, THEN WHEN PROMPTED TYPE 'folder/' INCLUDING A SLASH (REPLACE 'folder' WITH THE NAME OF YOUR GAME FOLDER)
source = input('file directory: ')

#THIS IS HOW MANY DIGITS TO REMOVE FROM THE BEGINNING OF THE FILE NAME. EXAMPLE: if your files look like '001 Pokemon Ruby' and you input 4, the output will turn into 'Pokemon Ruby'
spaces = int(input('how many digits to remove: '))


list = []

def main() :

    for i in enumerate(os.listdir(source)) :
        list.append(i[1])

    for x in list :
        if x == '.DS_Store' :
            continue
        else :
            dest = x[(spaces):]
            src = source + x
            dest = source + dest

            os.rename(src, dest)



main()