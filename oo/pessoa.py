class Pessoa:
    olhos = 2
    def __init__(self ,*filhos, nome = None, idade=30):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'olá {id(self)}'

if __name__ == '__main__':
    warley = Pessoa(nome='Warley')
    liliane = Pessoa(warley,nome='Liliane')
    print(Pessoa.cumprimentar(liliane))
    print(id(liliane))
    print(liliane.cumprimentar())
    print(liliane.nome)
    print(liliane.idade)
    for filhos in liliane.filhos:
        print(filhos.nome)
    liliane.sobrenome = 'Pinheiro'
    del liliane.filhos
    liliane.olhos = 1
    del liliane.olhos
    print(liliane.__dict__)
    print(warley.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(liliane.olhos)
    print(warley.olhos)
    print(id(Pessoa.olhos), id(liliane.olhos),id(warley.olhos))

