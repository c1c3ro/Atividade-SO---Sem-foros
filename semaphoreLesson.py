import threading
import time
import random

semaforo = threading.Semaphore(3)

def atenderCliente(clientID):
    semaforo.acquire()
    print("Atendendo o cliente: {}".format(clientID))
    time.sleep(random.randint(3, 10))
    print("Atendimento finalizado com o cliente: {}".format(clientID))
    semaforo.release()

if __name__=="__main__":
    threads =  []
    for i in range(1, 31):
        threads.append(threading.Thread(target=atenderCliente, args=(i, )))
        threads[-1].start()

    for thread in threads:
        thread.join()