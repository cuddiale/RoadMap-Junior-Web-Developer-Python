class Libreria:
    def __init__(self, nome, libri):
        self.nome = nome
        self.libri = libri  # lista di stringhe

    def __str__(self):
        return f"Libreria '{self.nome}' con {len(self)} libri"

    def __repr__(self):
        return f"Libreria('{self.nome}', {self.libri})"

    def __len__(self):
        return len(self.libri)

    def __add__(self, other):
        if isinstance(other, Libreria):
            nuovo_nome = f"{self.nome} & {other.nome}"
            nuovi_libri = self.libri + other.libri
            return Libreria(nuovo_nome, nuovi_libri)
        return NotImplemented

    def __eq__(self, other):

        if isinstance(other, Libreria):
            return self.libri == other.libri
        return False


# Creazione oggetti
lib1 = Libreria("Fantasy", ["Harry Potter", "Il Signore degli Anelli"])
lib2 = Libreria("Classici", ["1984", "Il Conte di Montecristo"])
lib3 = Libreria("Fantasy Copia", ["Harry Potter", "Il Signore degli Anelli"])

# __str__
print(lib1)

# __repr__
print(repr(lib1))

# __len__
print("Numero libri:", len(lib1))

# __add__
lib_totale = lib1 + lib2
print(lib_totale)

# __eq__
print("lib1 == lib3 ?", lib1 == lib3)
