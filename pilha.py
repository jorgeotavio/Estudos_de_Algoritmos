class Pilha:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.__tamanho = 0
        self.__iterando = None

    class No:
        def __init__(self, conteudo):
            self.proximo = None
            self.anterior = None
            self.conteudo = conteudo

    def __len__(self):
        return self.__tamanho

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        return self

    def __next__(self):
        if self.__iterando is None:
            self.__iterando = self.primeiro
        else:
            self.__iterando = self.__iterando.proximo

        if self.__iterando is not None:
            return self.__iterando.conteudo

        raise StopIteration

    def __getitem__(self, i):
        if self.ultimo is not None:
            atual = self.ultimo
            indice = len(self)-1
            while indice >= 0:
                if i == indice:
                    return atual.conteudo

                atual = atual.anterior
                indice -= 1

    def __str__(self):
        retorno = '['
        for i, e in enumerate(self):
            retorno += e.__repr__()
            if i < len(self)-1:
                retorno += ', '

        retorno += ']'
        return retorno


    def __delitem__(self, i):
        if self.__tamanho != 0:
            atual = self.ultimo
            self.ultimo = self.ultimo.anterior
            self.ultimo.proximo = None
            atual.anterior = None
            atual.proximo = None

            self.__tamanho -= 1
            self.__iterando = None

    def inserir(self, conteudo):
        novo = self.No(conteudo)

        if self.__tamanho == 0:
            self.primeiro = novo
            self.ultimo = novo

        else:
            last = self.ultimo
            self.ultimo.proximo = novo
            self.ultimo = novo
            novo.anterior = last

        self.__tamanho += 1
        self.__iterando = None

    def pop(self):
        del self[len(self)-1]
