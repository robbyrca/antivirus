import shutil,os

file_source = '/home/ubunserver/github/antivirus/virustotal/'
file_destination1 = '/home/ubunserver/github/antivirus/virustotalrevisando/'
file_destination2 = '/home/ubunserver/github/antivirus/virustotalrevisado/'
file_destination3 = '/home/ubunserver/github/antivirus/virustotalcuarentena/'

get_file = os.listdir(file_source)

contador=1

#MEJORAS V2.2 (SACAR FICHEROS A RAIZ)
for root, dirs, files in os.walk(file_source):
    for filename in files:
        filepath = os.path.join(root, filename)
        shutil.move(filepath, file_destination1)
"""
for x in get_file:
   contador=contador+1                                #MEJORAS V2.2 nº1 (limitacion de lectura de archivos a 10)
   if contador <11 :                                  #MEJORAS V2.2 nº1
    shutil.move(file_source + x, file_destination1)   
    if get_file:
        print (x + 'moved')
    else:
        f = open ('logs.txt', "w")
        f.write('Error moving ' + x)
        f.close()
"""
