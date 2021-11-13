import os
import random
import time
from datetime import datetime

from smart_m3.m3_kp_api import *

global left
left = 0
global right
right = 100
global game
game = True

global id
id = -1
global timestamp
timestamp = time.time()

class KpHandler:
    def __init__(self, kp=None):
        self.kp = kp

    def handle(self, added, removed):

        global left
        global right
        global game
        global id
        global timestamp

        # Добавить проверку, что уже инициализировались и не надо заходить в проверку айди
        # Добавить переподписку после получения айдишника
        print("*******************")
        print("Added ", added)
        print("Removed ", removed)
        print("*******************")
        
        if len(added) > 0:
            if str(added[0][1])[:6] == 'Result':
                if str(added[0][2])[:1] == '>':
                    right = round((left + right) / 2)
                    print('left {} right {}'.format(left, right))
                elif str(added[0][2])[:1] == '<':
                    left = round((left + right) / 2)
                    print('left {} right {}'.format(left, right))
                else:
                    print("Victory")
                    print("Correct Answer is {}".format(round((left + right) / 2)))
                    game = False
            elif (id == -1) & (str(added[0][1]) == str(timestamp)):
                id = int(str(added[0][2]))
                print("Registered as id {}".format(id))

if __name__ == '__main__':
    # подключились к пространству, подписали агента на выбранный паттерн
    kp = m3_kp_api();
    subscription_triple = Triple(URI('Game'), URI(timestamp), None)
    handler = KpHandler(kp)
    handler_subscription = kp.load_subscribe_RDF(subscription_triple, handler)


    kp.load_rdf_insert([
        Triple(URI('Game'), URI('Init'), Literal(timestamp))
    ])

    while (id == -1):
        time.sleep(0.05)

    kp.load_rdf_remove(Triple(URI('Game'), URI(timestamp), None))
    kp.load_rdf_remove(Triple(URI('Game'), URI('Init'), Literal(timestamp)))


    kp.load_unsubscribe(handler_subscription)
    subscription_triple = Triple(URI('Game'), URI('Result' + str(id)), None)
    handler = KpHandler(kp)
    handler_subscription = kp.load_subscribe_RDF(subscription_triple, handler)

    while(game):
        time.sleep(0.5)
        cur = round((left + right) / 2)
        kp.load_rdf_insert([
            Triple(URI('Game'), URI('Guess' + str(id)), Literal(cur))
        ])
    
    
    # отписываем агента и полностью очищаем записанные данные
    time.sleep(0.05)
    kp.load_unsubscribe(handler_subscription)
    #будет удалять всё, надо добавить удаление своих
    #kp.clean_sib()
    kp.load_rdf_remove(Triple(URI('Game'), URI('Result' + str(id)), None))
    kp.load_rdf_remove(Triple(URI('Game'), URI('Guess' + str(id)), None))

    # отключаем соединение с брокером и отправляем сигнал на завершение программы
    kp.leave()
    time.sleep(0.05)
    raise os._exit(0)
