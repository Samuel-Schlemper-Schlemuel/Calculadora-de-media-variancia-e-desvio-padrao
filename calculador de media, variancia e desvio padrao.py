import numpy as np


def calculate(lista):

    if str(type(lista)) != "<class 'list'>":
        return 'Must be a list'
    elif len(lista) != 9:
        raise ValueError('List must contain nine numbers.')

    lista = np.array(lista)
    lista = lista.reshape((3, 3))
    result = {
        'mean': [lista.mean(axis=0).tolist(), lista.mean(axis=1).tolist(), lista.mean().tolist()],
        'variance': [lista.var(axis=0).tolist(), lista.var(axis=1).tolist(), lista.var().tolist()],
        'standard deviation': [lista.std(axis=0).tolist(), lista.std(axis=1).tolist(), lista.std().tolist()],
        'max': [lista.max(axis=0).tolist(), lista.max(axis=1).tolist(), lista.max().tolist()],
        'min': [lista.min(axis=0).tolist(), lista.min(axis=1).tolist(), lista.min().tolist()],
        'sum': [lista.sum(axis=0).tolist(), lista.sum(axis=1).tolist(), lista.sum().tolist()]
    }
    return result
