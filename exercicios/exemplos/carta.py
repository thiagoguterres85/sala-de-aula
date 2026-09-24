class Carta:
    conteudo: str 
    destinatario: str
    remetente: str


def __init__ (self, conteudo: str, destinatario: str, remetente: str):
    self.conteudo = conteudo 
    self.destinatario = destinatario
    self.remetente = remetente 

#Instancia 
carta = Carta ('conta_de_luz', 'cee', 'alguem')
carta_de_conta = Carta (conteudo='conta_de_luz', destinatario='cee', remetente='alguem') 

