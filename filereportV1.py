import shutil,os,requests,json
from urllib import response

file_source = '/home/user/github/antivirus/id/'
file_destination1 = '/home/user/github/antivirus/verificado/'
file_destination2 = '/home/user/github/antivirus/procesando/'
file_destination3 = '/home/user/github/antivirus/cuarentena/'
file_destination4 = '/home/user/github/antivirus/logs/'

def upload(id):
    url = "https://www.virustotal.com/api/v3/analyses/"+id
    headers = {
        "accept": "application/json",
        "x-apikey": "206706e5d63a9393a5786e3191ba9c471dcbb00305f4a32d49de38c45f20c4c7"
    }
    response = requests.get(url, headers=headers)
    #print(response.text)
    jsonresp = response.json()
    if jsonresp.get("data").get("attributes").get("status") != "queued":  
        malget = jsonresp.get("data").get("attributes").get("stats").get("malicious")
        #print (malget)
        responsesave(malget,id)
        if  malget>0:
            #print('entro m')
            print('Archivo malicioso detectado!')
            print(filename)
            filepath = os.path.join(root, filename)
            shutil.move(filename, file_destination3)
        else:
            #print('entro r')
            filepath = os.path.join(root, filename)
            shutil.move(filename, file_destination1)

def responsesave(malget, file):
    with open(file_destination4+id, "w") as fp:
        json.dump(malget, fp, indent=2)

for root, dirs, files in os.walk(file_source):
    for filename in files:
        filepath = os.path.join(root, filename)
        with open(filepath, 'r') as r:
            contenido = r.read()
        contsplit = contenido.split(":")
        idcont = contsplit[1]
        filename1 = contsplit [0]
        filename2 = filename1.split('"')
        filename = filename2 [1]
        idesp = idcont.split('"')
        id = idesp[0]
        #print(id)
        upload(id)
        count=0

for path in os.listdir(file_destination2):
    if os.path.isfile(os.path.join(root, filename)):
            count = count + 1

print('Quedan ' + str(count) + 'archivos por analizar')

if count > 0:
    print('Quedan ' + str(count) + 'archivos por analizar')