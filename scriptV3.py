import shutil,os,requests

file_source = '/home/ubunserver/github/antivirus/virustotal/'
file_destination1 = '/home/ubunserver/github/antivirus/virustotalrevisando/'
file_destination2 = '/home/ubunserver/github/antivirus/virustotalrevisado/'
file_destination3 = '/home/ubunserver/github/antivirus/virustotalcuarentena/'

get_file = os.listdir(file_source)

contador=1

#MEJORAS V2.2 (SACAR FICHEROS DE SUBCARPETAS HASTA REVISANDO)
for root, dirs, files in os.walk(file_source):
    for filename in files:
        filepath = os.path.join(root, filename)
        shutil.move(filepath, file_destination1)
        print(filename + " moved")

shutil.rmtree(file_source)
os.mkdir(file_source)

url = 'https://www.virustotal.com/vtapi/v2/file/scan'
params = {'apikey': '206706e5d63a9393a5786e3191ba9c471dcbb00305f4a32d49de38c45f20c4c7'}
files = {'file': ('myfile.exe', open('myfile.exe', 'rb'))}
response = requests.post(url, files=files, params=params)
print(response.json())