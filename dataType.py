# ============================================================
# PYTHON DATA TYPES
# ============================================================
#
# En programmation, le "data type" (type de donnee) est un concept
# important. Les variables peuvent stocker differents types de
# donnees, et chaque type peut faire des choses differentes.
#
# Python possede les types de donnees suivants, integres par
# defaut, repartis dans ces categories :
#
#   Texte             -> str
#   Numerique         -> int, float, complex
#   Sequence          -> list, tuple, range
#   Mapping           -> dict
#   Ensembles (Set)   -> set, frozenset
#   Booleen           -> bool
#   Binaire           -> bytes, bytearray, memoryview
#   Type Vide         -> NoneType


# ------------------------------------------------------------
# 1. Obtenir le type d'une donnee
# ------------------------------------------------------------
# La fonction type() renvoie le type de n'importe quel objet.

x = 5
print(type(x))  # <class 'int'>


# ------------------------------------------------------------
# 2. Definir le type (implicitement)
# ------------------------------------------------------------
# En Python, le type est defini automatiquement selon la valeur
# que tu assignes a la variable.

x = "Hello World"                          # str
x = 20                                     # int
x = 20.5                                   # float
x = 1j                                     # complex
x = ["apple", "banana", "cherry"]          # list
x = ("apple", "banana", "cherry")          # tuple
x = range(6)                               # range
x = {"name": "John", "age": 36}            # dict
x = {"apple", "banana", "cherry"}          # set
x = frozenset({"apple", "banana", "cherry"})  # frozenset
x = True                                   # bool
x = b"Hello"                               # bytes
x = bytearray(5)                           # bytearray
x = memoryview(bytes(5))                   # memoryview
x = None                                   # NoneType


# ------------------------------------------------------------
# 3. Definir un type precis (explicitement)
# ------------------------------------------------------------
# Si tu veux forcer un type precis, utilise les fonctions
# "constructeur" correspondantes.

x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name="John", age=36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))


# ============================================================
# EXERCICES - a faire toi-meme
# ============================================================
#
# Ecris ton code juste en dessous de chaque question,
# puis lance "python dataType.py" pour verifier le resultat.

# Exercice 1
# ----------
# Si x = 5, quelle est la bonne syntaxe pour afficher le type
# de la variable x ?
#   a) print(dtype(x))
#   b) print(type(x))
#   c) print(x.dtype())
#
# -> Ecris ta reponse ici en code :


# Exercice 2
# ----------
# Cree une variable y contenant le texte "Python" et affiche
# son type avec type().


# Exercice 3
# ----------
# Cree une variable z contenant le nombre 3.14 et affiche
# son type. Quel type Python va-t-il lui donner ?


# Exercice 4
# ----------
# Cree une liste contenant 3 fruits de ton choix, puis affiche
# son type.


# Exercice 5
# ----------
# Utilise le constructeur bool() pour convertir le nombre 0 en
# booleen, et affiche le resultat. Que se passe-t-il avec bool(1) ?


# ============================================================
# CORRECTION (ne regarde qu'apres avoir essaye !)
# ============================================================
#
# Exercice 1 : reponse b) print(type(x))
#              "dtype" n'existe pas en Python standard (c'est
#              un terme utilise par la librairie NumPy).
#
# Exercice 2 :
#   y = "Python"
#   print(type(y))   # <class 'str'>
#
# Exercice 3 :
#   z = 3.14
#   print(type(z))   # <class 'float'>
#
# Exercice 4 :
#   fruits = ["pomme", "banane", "kiwi"]
#   print(type(fruits))   # <class 'list'>
#
# Exercice 5 :
#   print(bool(0))   # False
#   print(bool(1))   # True
#   -> 0 est toujours considere comme "Faux", tout le reste
#      (nombres non nuls, textes non vides, listes non vides...)
#      est considere comme "Vrai".
