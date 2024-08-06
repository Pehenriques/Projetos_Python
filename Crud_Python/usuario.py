class Usuario: #Classe usuario
    def __init__(self, nome, email, telefone): # aqui defini os atributos da classe como nome, email e telefone
        self.nome= nome
        self.email= email
        self.telefone= telefone
# aqui criei as funçoes get e set para chamar dentro do CRUD
    def get_nome(self):
        return self.nome

    def get_email(self):
        return self.email

    def get_telefone(self):
        return self.telefone

    def set_nome(self, nome):
        self.nome = nome

    def set_email(self,email):
        self.email = email

    def set_telefone(self,telefone):
        self.telefone = telefone