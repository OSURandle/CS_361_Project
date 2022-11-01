

import zmq

def magic_rng_card():

    context = zmq.Context()
    
#  Socket to talk to server
    print("Connecting to rng name server…")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    print("Sending request…")
    socket.send_string("Generating random card name...")

        #  Get the reply.
    message = socket.recv()
    return message.decode('utf-8')
    

card_name = magic_rng_card() 
print(card_name)