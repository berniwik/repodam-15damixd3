""" Programa que guarda les dades de l'usuari en un fitxer, la constrasenya
    està encriptada amb SHA256. """
from getpass import getpass
from Crypto.Hash import SHA256

UID = input("Introdueix el teu identificador ")
NOMUSUARI = input("Introdueix el teu nom d'usuari ")
#Al executar-ho amb idle no deshabilita l'echo, executant-ho amb un terminal si ho fa.
#Es recomana executar-ho amb el terminal.
PASSWD = getpass("Introdueix una contrasenya ").encode('utf-8')
OBJH = SHA256.new(PASSWD)
PASSWD = OBJH.hexdigest()
str(PASSWD)

def creartxt():
    """ Crea el fitxer """
    archi = open('dades_usuari.txt', 'w')
    archi.close()

def escriuretxt(uid, nomusuari, passwd):
    """ Escriu en el fitxer """
    archi = open('dades_usuari.txt', 'a')
    archi.write("UID: "+uid+ " "+ "Nom d'usuari: "+ nomusuari+" "+ "Contrasenya: "+ passwd)
    archi.close()

creartxt()
escriuretxt(UID, NOMUSUARI, PASSWD)
