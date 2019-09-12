import random

KREWES = {
    'orpheus': ['Emily','Kevin','Vishwaa','Eric','Jay'],
    'rex': ['William','Joseph','Calvin','Ethan','Moody'],
    'endymion': ['Grace','Nahi','Derek','Jun Tao','Connor']
}

def rando(tn):
    print(random.choice(KREWES[tn]))

rando('orpheus')
rando('rex')
rando('endymion')
