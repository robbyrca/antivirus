import shutil,os,requests,json, time
from urllib import response
from pathlib import Path

file_source = '/Users/ruben/Documents/GitHub/antivirus/id/'
file_destination1 = '/Users/ruben/Documents/GitHub/antivirus/verificado/'
file_destination2 = '/Users/ruben/Documents/GitHub/antivirus/procesandoid/'
file_destination3 = '/Users/ruben/Documents/GitHub/antivirus/cuarentena/'
file_destination4 = '/Users/ruben/Documents/GitHub/antivirus/logs/'
file_destination5 = '/Users/ruben/Documents/GitHub/antivirus/procesandorep/'
timesleepcount=0

def upload(id):
    global bucle
    global timesleepcount
    url = "https://www.virustotal.com/api/v3/analyses/"+id
    headers = {
        "accept": "application/json",
        "x-apikey": "206706e5d63a9393a5786e3191ba9c471dcbb00305f4a32d49de38c45f20c4c7"
    }
    timesleepcount = timesleepcount + 1
    if timesleepcount == 5:
        print('Control de tiempo de 60 segundos')
        time.sleep(60)
        timesleepcount=0
    else:
        response = requests.get(url, headers=headers)
        if(response.status_code == 429):
            print("Error de cuota excedida :! o Error de demasiadas solicitudes controlate ;)")
            print("Codigo de error : " + str(response.status_code))
            exit()
        if response.status_code == 200:
            #print(response.text)
            jsonresp = response.json()
            if jsonresp.get("data").get("attributes").get("status") != "queued":  
                malget = jsonresp.get("data").get("attributes").get("stats").get("malicious")
                #print (malget)
                responsesave(malget,id)
            if  malget>0:
                #print('entro m')
                print('\n'+'Archivo malicioso detectado!')
                filepath = os.path.join(root, filename)
                shutil.move(filename, file_destination3)
                os.remove(rutaid)
                bucle = True
            else:
                #print('entro r')
                print(enviocheck+'1')
                filepath = os.path.join(root, filename)
                shutil.move(filename, file_destination1)
                os.remove(rutaid)
                bucle = True

        else:
            print ("No s'ha pogut obtenir la URL :(")
            print ("ERROR al pujar el archiu :!")
            print ("Status code: " + str(response.status_code))


def checkFileExistance(enviocheck):
    try:
        with open(enviocheck, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

def responsesave(malget, file):
    with open(file_destination4+id, "w") as fp:
        json.dump(malget, fp, indent=2)

for root, dirs, files in os.walk(file_source):
    for filename in files:
        filepath = os.path.join(root, filename)
        enviocheck = filepath
        idenruta = checkFileExistance (enviocheck)
        if idenruta == True:
            if filepath != ('/Users/ruben/Documents/GitHub/antivirus/id/.DS_Store'):
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
                rutaid = filepath
                enviocheck = filename
                existe = checkFileExistance(enviocheck)
                if existe == True:
                    if filepath != ('/Users/ruben/Documents/GitHub/antivirus/id/.DS_Store'):
                        bucle=False
                        while bucle == False:
                            upload(id)
                    else:
                        os.remove(filepath)
                        print(filepath)
                        print('removed')
                else:
                    print ('No se ha encontrado el archivo')
                    os.remove(rutaid)
            else:
                print(filepath)
                print('removed')
                os.remove(filepath)
        else:
            print('No hay ningun archivo a analizar')

count=0

for path in os.listdir(file_destination2):
    if os.path.isfile(os.path.join(root, filename)):
            count = count + 1

#print('Quedan ' + str(count) + ' archivos por analizar')

if count > 0:
    if filepath != (file_source+'.DS_Store'):
        print('\n'+'Quedan ' + str(count) + ' archivos por analizar')