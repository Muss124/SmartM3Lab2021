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
            if str(data[1]) == 'Test':
                print("TEST DATA ADDED")
                break
        print("*******************")

if __name__ == '__main__':
    # подключились к пространству, подписали агента на выбранный паттерн
    kp = m3_kp_api();
    subscription_triple = Triple(URI('AgentX'), None, None)
    handler = KpHandler(kp)
    handler_subscription = kp.load_subscribe_RDF(subscription_triple, handler)

    # вставляем несколько RDF-троек 
    kp.load_rdf_insert([
            Triple(URI('AgentX'), URI('Test'), Literal(123)),
            Triple(URI('AgentX'), URI('Test'), Literal(321)),
            Triple(URI('AgentX'), URI('Test'), URI('TEST')),
            Triple(URI('AgentY'), URI('Test'), URI('TSET'))
        ])

    # Проверим вставку троек, подходящик под паттерн
    time.sleep(0.05)
    kp.load_query_rdf(Triple(Triple(URI('AgentY'), None, None)))
    print('Query results are: {}'.format(kp.result_rdf_query))

    # изменим тройки, подходящие под паттерн
    #time.sleep(0.05)
    kp.load_query_rdf(Triple(URI('AgentX'), None, None))
    #print('Query results before update are: {}'.format(kp.result_rdf_query))
    if len(kp.result_rdf_query) > 0:
        updated = []
        value = 666;
        for old in kp.result_rdf_query:
            updated.append(Triple(old[0], URI('NOTATEST'), Literal(value)))
            value+=111
    kp.load_rdf_update(updated, kp.result_rdf_query)
    
    time.sleep(0.05)
    kp.load_query_rdf(Triple(URI('AgentX'), None, None))
    #print('Query results are: {}'.format(kp.result_rdf_query))

    # удалим все записанные тройки, подходящие под паттерны       
    kp.load_rdf_remove(Triple(URI('AgentX'), None, None))
    kp.load_rdf_remove(Triple(URI('AgentY'), None, None))
    

    # отписываем агента и полностью очищаем записанные данные
    kp.load_unsubscribe(handler_subscription)
    kp.clean_sib()

    # отключаем соединение с брокером и отправляем сигнал на завершение программы
    kp.leave()
    time.sleep(0.05)
    raise os._exit(0)
