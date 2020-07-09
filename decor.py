import time

def timer(fun):
    def tmp(*args, **kwargs):
        t = time.time()
        res = fun(*args, **kwargs)
        print("Время выполнения функции: %fun" % (time.time()-t))
        return res

    return tmp
