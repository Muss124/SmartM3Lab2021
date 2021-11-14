# SmartM3Lab2021
Knowledge management course. Lab 2. Written in Python.
Using Smart-m3 deployed in Docker (taken from [here](https://cais.iias.spb.su/gitlab/smart-m3/smart-m3-docker)).
You need to deploy your own instance of smart-m3 and of course installed Python interpreter to be able to run tasks successfully. 

## Task 1
Testing base functions: inster/query/update/remove. Inser few RDF-triples, check insert with Query with different patterns, Update existing triples, delete triples using Remove.

### Lauching 
In folder with Task1.py file open command line and run next line: 
```
python .\Task1.py
```

## Task 2
Subscriptions. Create agent that periodicaly insert triple in format [URI('Agent_X'), URI('has_item'), Literal(number)], subscribe to updates of data vault, make sure that subscription works. Create another agent, that will "listen" to updates and remove all even numbers. Make sure that removed numbers are correct

### Lauching 
Require to run a few programs simultaneously. For this you can open two command lines. Next you need to open folder with Task2Generator.py and Task2Generator.py files. First you need to run this line:
```
python .\Task2Listener.py
```
Then in second command line run this line:
```
python .\Task2Generator.py
```

## Task 3
Guessing number game. Create two agents: server and player. Player trying to guess number by sending messages to vault. Server response back with result of comparison of guess and answer.

### Lauching 
This task also require to run a few programs simultaneously. You whould need to run game program and then run any amount of player instances. 
First you need to open folder with Task3Game.py and Task3Player.py files. Open command lines. First you need to run this line:
```
python .\Task3Game.py
```
Then in second and any other command lines run this line to add players:
```
python .\Task3Player.py
```

