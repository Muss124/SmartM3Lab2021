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
        print("*******************")

if __name__ == '__main__':
    kp = m3_kp_api();
    subscription_triple = Triple(URI('Listener'), None, None)
    handler = KpHandler(kp)
    handler_subscription = kp.load_subscribe_RDF(subscription_triple, handler)

    kp.load_rdf_insert([
            Triple(URI('Listener'), URI('Test'), Literal(123)),
            Triple(URI('Listener'), URI('Test'), Literal(321)),
            Triple(URI('Listener'), URI('Test'), URI('TEST')),
            Triple(URI('Listener'), URI('Test'), URI('TSET'))
        ])
    kp.load_rdf_remove(Triple(URI('Listener'), URI('Test'), None))
    
    random.seed(None, 2);
    amount = 20
    while(amount > 0):
        time.sleep(0.5)
        kp.load_rdf_insert([
            Triple(URI('Listener'), URI('Number'), Literal(random.randrange(0, 100, 1)))
        ])
        amount-=1
    
    
    time.sleep(0.05)
    kp.load_unsubscribe(handler_subscription)
    kp.clean_sib()
    
    kp.leave()
    time.sleep(0.05)
    raise os._exit(0)
