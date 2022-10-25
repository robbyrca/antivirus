import shutil,os,requests,json
from urllib import response

file_source = '/home/user/github/antivirus/virustotal/'
file_destination1 = '/home/user/github/antivirus/virustotalrevisando/'
file_destination2 = '/home/user/github/antivirus/virustotalrevisado/'
file_destination3 = '/home/user/github/antivirus/virustotalcuarentena/'
file_destination4 = '/home/user/github/antivirus/virustotalid/'

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
    jsonresp = response.json()
    idget = jsonresp.get("data").get("id")
    idsave(idget,file)


def idsave(id,file):
    print(id)
    with open(file_destination4+id, "w") as fp:
        json.dump(file+":"+id, fp, indent=2)

#MEJORAS V2.2 (SACAR FICHEROS DE SUBCARPETAS HASTA REVISANDO)
for root, dirs, files in os.walk(file_source):
    for filename in files:
        filepath = os.path.join(root, filename)
        shutil.move(filepath, file_destination1)
        print(filename + " moved")
        print(file_destination1+filename)
        upload(file_destination1+filename)

shutil.rmtree(file_source)
os.mkdir(file_source)

