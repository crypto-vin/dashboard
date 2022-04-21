#strip text

full_msg = 'Vin Nairobi2020'

def strip_msg(msg):
    half = msg.find(' ')
    username = (msg[: half ])
    password = (msg[half + 1 :])
    print(username, password)

strip_msg(full_msg)

