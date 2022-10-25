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

shutil.rmtree(file_source)
os.mkdir(file_source)
