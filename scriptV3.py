import shutil,os,requests

file_source = '/home/ubunserver/github/antivirus/virustotal/'
file_destination1 = '/home/ubunserver/github/antivirus/virustotalrevisando/'
file_destination2 = '/home/ubunserver/github/antivirus/virustotalrevisado/'
file_destination3 = '/home/ubunserver/github/antivirus/virustotalcuarentena/'

get_file = os.listdir(file_source)

contador=1

def upload(file):
    url = "https://www.virustotal.com/api/v3/files"
    files = {"file": open(file, "rb")}
    headers = {
        "accept": "application/json",
        "x-apikey": "206706e5d63a9393a5786e3191ba9c471dcbb00305f4a32d49de38c45f20c4c7"
    }
    response = requests.post(url, files=files, headers=headers)
    print(response.text)

#MEJORAS V2.2 (SACAR FICHEROS DE SUBCARPETAS HASTA REVISANDO)
for root, dirs, files in os.walk(file_source):
    for filename in files:
        filepath = os.path.join(root, filename)
        shutil.move(filepath, file_destination1)
        print(filename + " moved")
        upload(file_destination1)

shutil.rmtree(file_source)
os.mkdir(file_source)

