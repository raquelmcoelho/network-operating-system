import json


# file methods
def ler():
    with open("users.json", "r") as f:
        txt = json.load(f)
        return txt


def salvar(txt):
    with open("users.json", "w", encoding="utf-8") as f:
        json.dump(txt, f)


def atualizar(dados):
    txt = ler()
    txt.append(dados)
    salvar(txt)


def deleteuser(user):
    txt = ler()
    for i in txt:
        if i[0] == user[0]:
            txt.remove(i)
            salvar(txt)


def replace(substituto):
    txt = ler()
    for i in txt:
        if i[0] == substituto[0]:
            txt.remove(i)
            txt.append(substituto)
            salvar(txt)


def acessaruserinfo(clientid):
    txt = ler()
    for i in txt:
        if i[0] == str(clientid):
            return i


def cleanfile():
    salvar([])