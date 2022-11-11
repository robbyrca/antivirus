import shutil,os,requests,json
from urllib import response

file_source = '/home/user/github/antivirus/virustotal/'
file_destination1 = '/home/user/github/antivirus/procesando/'
file_destination2 = '/home/user/github/antivirus/verificado/'
file_destination3 = '/home/user/github/antivirus/cuarentena/'
file_destination4 = '/home/user/github/antivirus/id/'

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

def uploadbig(file):
        files = {"file": open(file, "rb")}
        url = "https://www.virustotal.com/api/v3/files/upload_url"
        headers = {
            "accept": "application/json",
            "x-apikey": "206706e5d63a9393a5786e3191ba9c471dcbb00305f4a32d49de38c45f20c4c7"
        }
        response = requests.get(url, headers=headers)
        if(response.status_code == 429):
            print("Error de cuota excedida :! o Error de demasiadas solicitudes controlate ;)")
            print("Codigo de error : " + str(response.status_code))
            exit()

        if response.status_code == 200:
            result = response.json()
            url_upload = result.get("data")

        else:
            print ("No s'ha pogut obtenir la URL :(")
            print ("ERROR al pujar el archiu :!")
            print ("Status code: " + str(response.status_code))
        
        #Obtenim una id
        response = requests.post(url_upload, files=files, headers=headers)
        if(response.status_code == 429):
            print("Error de cuota excedida :! o Error de demasiadas solicitudes controlate ;)")
            print("Codigo de error : " + str(response.status_code))
            exit()

        if response.status_code == 200:
            result = response.json()
            idbig = result.get("data").get("id")
            idsave(idbig,file)

def idsave(id,file):
    #print(id)
    with open(file_destination4+id, "w") as fp:
        json.dump(file+":"+id, fp, indent=2)

for root, dirs, files in os.walk(file_source):
    for filename in files:
        filepath = os.path.join(root, filename)
        print(file_destination1+filename)
        if (os.path.getsize(os.path.join(root, filename)) >> 20) > 32:
            shutil.move(filepath, file_destination1)
            print(filename + " moved"+"\n")
            uploadbig(file_destination1+filename)
        else:
            shutil.move(filepath, file_destination1)
            print(filename + " moved"+"\n")
            upload(file_destination1+filename)

shutil.rmtree(file_source)
os.mkdir(file_source)

