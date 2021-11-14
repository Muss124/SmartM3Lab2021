import os
import random
import time
from datetime import datetime

from smart_m3.m3_kp_api import *

random.seed(None, 2)
global curId
curId = 0;
global data
data = {}

class KpHandler:
    def __init__(self, kp=None):
        self.kp = kp

    def handle(self, added, removed):


        global data
        global curId
        
        print("*******************")
        print("Added ", added)
        print("Removed ", removed)
        print("*******************")
        
        if len(added) > 0:
            if str(added[0][1])[:5] == 'Guess':
                
                current = int(str(added[0][1])[5:])
                value = int(str(added[0][2]))
                data[current][1] += 1
                answer = data[current][0]

                if data[current][2]:
                    if value < answer:
                        kp.load_rdf_insert([
                            Triple(URI('Game'), URI('Result' + str(current)), Literal('<' + str(data[current][1])))
                        ])
                    elif value > answer:
                        kp.load_rdf_insert([
                            Triple(URI('Game'), URI('Result' + str(current)), Literal('>' + str(data[current][1])))
                        ])
                    else:
                        kp.load_rdf_insert([
                            Triple(URI('Game'), URI('Result' + str(current)), Literal('=' + str(data[current][1])))
                        ])
                        data[current][2] = False
                        print("Game with id {} is over".format(current))
            elif str(added[0][1]) == 'Init':
                curId += 1;
                data[curId] = [random.randrange(0, 100, 1), 0 , True];
                kp.load_rdf_insert([
                    Triple(URI('Game'), added[0][2], Literal(curId))
                ])
                print("Id {} is registered, answer is {}".format(curId, data[curId][0]))

if __name__ == '__main__':
    kp = m3_kp_api();
    subscription_triple = Triple(URI('Game'), None, None)
    handler = KpHandler(kp)
    handler_subscription = kp.load_subscribe_RDF(subscription_triple, handler)

    while(True):
        time.sleep(0.005)

    kp.load_unsubscribe(handler_subscription)

    kp.leave()
    time.sleep(0.05)
    raise os._exit(0)
