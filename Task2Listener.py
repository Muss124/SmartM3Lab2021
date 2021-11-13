import os
import random
import time
from datetime import datetime

from smart_m3.m3_kp_api import *

class KpHandler:
    def __init__(self, kp=None):
        self.kp = kp

    def handle(self, added, removed):
        print("*******************")
        print("Added ", added)
        print("Removed ", removed)
        for data in added:
            print(type(data[2]))
            if (int(str(data[2])) % 2) == 0:
                self.kp.load_rdf_remove(data)
        for data in removed:
            if (int(str(data[2])) % 2) == 0:
                print("Correct number was removed")
        print("*******************")

if __name__ == '__main__':
    # подключились к пространству, подписали агента на выбранный паттерн
    kp = m3_kp_api();
    subscription_triple = Triple(URI('Listener'), URI('Number'), None)
    handler = KpHandler(kp)
    handler_subscription = kp.load_subscribe_RDF(subscription_triple, handler)

    while(True):
        time.sleep(0.005)
        
    

    # отписываем агента
    kp.load_unsubscribe(handler_subscription)

    # отключаем соединение с брокером и отправляем сигнал на завершение программы
    kp.leave()
    time.sleep(0.05)
    raise os._exit(0)
