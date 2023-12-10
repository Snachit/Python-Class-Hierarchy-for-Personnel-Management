from abc import ABCMeta, abstractmethod

class Person(metaclass=ABCMeta):
    def __init__(self, nom, prenom, age, code):
        self._nom = nom
        self._prenom = prenom
        self._age = age
        self._code = code

    def get_name(self):
        return self._nom
    
    def get_prenom(self):
        return self._prenom
    
    def get_age(self):
        return self._age
    
    def get_code(self):
        return self._code
    
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

class Employe(Person):
    count = 0
    def __init__(self, nom, prenom, age, code, grad):
         super().__init__(nom, prenom, age, code)
         self.grad = grad
         Employe.count += 1
    
    def __str__(self):
         return f"""Nom: {self._nom}
prenom: {self._prenom}
age: {self._age} ans
code: {self._code}
grad: {self.grad}"""

    def __eq__(self, per2):
         if self._code == per2._code:
            return True
         else:
             return False

class Eleve(Person):
    count1 = 0
    def __init__(self, nom, prenom, age, code, niveau, moyenne):
        super().__init__(nom, prenom, age, code)
        self.niveau = niveau
        self.moyenne = moyenne
        Eleve.count1 += 1

    def __str__(self):
        return f"""Nom: {self._nom}
prenom: {self._prenom}
age: {self._age} ans
code: {self._code}
Niveau: {self.niveau}
Moyenne: {self.moyenne}"""

    def __eq__(self, other):
        if self._code == other._code:
            return True
        else:
            return False

# example of usage
per1 = Employe("mohamed", "nino", 19, 33, "A")
per2 = Employe("amin", "sal", 19, 44, "B")
per3 = Employe("Leo", "Messi", 37, 10, "A")
print(per1.__str__())
print("Nombre d'employe est:", Employe.count)
print("--------------------------------------------------------------------------")

ele1 = Eleve("alex", "morgan", 32, 50, 1, 19.12)
ele2 = Eleve("amin", "adeli", 20, 50, 2, 19.12)
print(ele1.__str__())
print("Nombre d'eleve dans la classe est :", Eleve.count1)
print("--------------------------------------------------------------------------")
