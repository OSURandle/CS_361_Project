

import zmq

def magic_rng_card():

    context = zmq.Context()
    start = input("Input 'start' to get a random card name or 'end' to leave rng ")

    if start == 'start':

#  Socket to talk to server
        print("Connecting to rng name server…")
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:5555")

        print("Sending request…")
        socket.send_string("Generating random card name...")

        #  Get the reply.
        message = socket.recv()
        card_name = message.decode('utf-8')
        return(card_name)
        
    elif start == 'end':
        print ("Ok thanks for playing!")

    else:
        print("Sorry you have entered the wrong input, try again")
        magic_rng_card()

magic_rng_card()