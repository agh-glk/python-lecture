# coding=utf-8

def iflatten_collection(collection, result_type=list):

    #WRITE ME

    for e in collection:
        yield e

def flatten_collection(collection, result_type=list):
    """
    Spłaszcza kolekcję, która jest dowolnie zagnieżdzona.
    Zwraca typ taki jak podano w argumencie, np. tuple lub list.
    Używa generatora.
    """
    return result_type(iflatten_collection(collection))


def flatten_dictionary(dictionary, name_crumbs=True):
    """
    Spłaszcza słownik. Jeśli name_crumbs jest włączone klucze tworzone są jako ścieżka wszsytkich kluczy zagłębień.
    """
    return dictionary