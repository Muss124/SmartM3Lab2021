# SmartM3Lab2021
Knowledge management course. Lab 2. Written in python.
Using Smart-m3 deployed in Docker (taker from [here](https://cais.iias.spb.su/gitlab/smart-m3/smart-m3-docker)).


## Task 1
Testing base functions: inster/query/update/remove. Inser few RDF-triples, check insert with Query with different patterns, Update existing triples, delete triples using Remove.

## Task 2
Subscriptions. Create agent that periodicaly insert triple in format [URI('Agent_X'), URI('has_item'), Literal(number)], subscribe to updates of data vault, make sure that subscription works. Create another agent, that will "listen" to updates and remove all even numbers. Make sure that removed numbers are correct

## Task 3
Guessing number game. Create two agents: server and player. Player trying to guess number by sending messages to vault. Server response back with result of comparison of guess and answer.
