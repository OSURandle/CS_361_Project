# CS_361

The purpose of this repository is to store assignments related to the CS_361 project

title 


participant magic_client


participant magic_server



activate magic_server
magic_client->magic_server:magic_rng_card()




activate magic_client
space
magic_client<--magic_server:card_name
space
destroy magic_client
destroy magic_server
