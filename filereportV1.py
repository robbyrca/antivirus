import shutil,os,requests,json
from urllib import response

file_source = '/home/user/github/antivirus/virustotalid/'
file_destination1 = '/home/user/github/antivirus/virustotalrevisando/'
file_destination2 = '/home/user/github/antivirus/virustotalrevisado/'
file_destination3 = '/home/user/github/antivirus/virustotalcuarentena/'

def upload(id, filename):
    url = "https://www.virustotal.com/api/v3/analyses/"+id
    headers = {
        "accept": "application/json",
        "x-apikey": "206706e5d63a9393a5786e3191ba9c471dcbb00305f4a32d49de38c45f20c4c7"
    }
    response = requests.get(url, headers=headers)
    print(response.text)
    jsonresp = response.text
    responsesave(jsonresp,id)
    if 'malicious' in jsonresp:
        filepath = os.path.join(root, filename)
        shutil.move(filename, file_destination3)
    

def responsesave(jsonresp, file):
    print(jsonresp)
    with open(file_destination2+id, "w") as fp:
        json.dump(jsonresp, fp, indent=2)

for root, dirs, files in os.walk(file_source):
    for filename in files:
        filepath = os.path.join(root, filename)
        with open(filepath, 'r') as r:
            contenido = r.read()
        contsplit = contenido.split(":")
        idcont = contsplit[1]
        filename = contsplit [0]
        idesp = idcont.split('"')
        id = idesp[0]
        print(id)
        upload(id)