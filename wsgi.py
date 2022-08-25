# import os
#
# from dotenv import load_dotenv
#
# dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
# if os.path.exists(dotenv_path):
#     load_dotenv(dotenv_path)
#
import time

def eventStream():
    print('dsfgh')
    a = 0
    while True:
        time.sleep(1)
        a += 1
        print(a)
        yield 'haha'
f=eventStream()
next(f)
next(f)

next(f)




