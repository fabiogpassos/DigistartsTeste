def ordenar(lista):
    lst = []
    
    for x in lista.split():
        if x not in ['\n', ' ', '/', ',']:
            try:
                x1 = int(x)
                if x1 not in lst:
                    lst.append(x1)
            except ValueError:
                return 'A lista deve conter somente números.'
    
    lst.sort()

    return lst
