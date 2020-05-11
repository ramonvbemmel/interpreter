# Rampthon interpreter
Dit is een nederlandse versie van python/C. Dit is gemaakt als opdracht voor mijn opleiding technische informatica aan de hu.  Voor de opdracht moest de interpreter geheel functioneel zijn. 
#### Werking interpreter. 
**[In tokenize.py](https://github.com/ramonvbemmel/interpreter/blob/master/tokenize.py)** wordt een file omgezet naar tokens. Deze tokens worden in een 2d matrix terug gegeven. 
Het tokentype staat gespecificeert in token_type.py. Een token bevat: type, value en het line nummer. Mogelijke types zijn: 
 - INT
 - STRING
 - OPERATOR
 -  KEYWORD 
 - ID.  

In value word opgeslagen wat de waarde opgeslagen die ingelezen is. 

**[Interpreter.py:](https://github.com/ramonvbemmel/interpreter/blob/master/interpreter.py)  ** worden alle tokens afgegaan en waar nodig een bewerking uitgevoerd. Zo is het mogelijk om een wiskunde operatie uit te voeren of te printen doormiddel van het keyword `toon`.  Bij een assigment wordt de waarde opgeslagen in de program state. De programstate is een dict. Wanneer er bijvoorbeeld `i = 10` wordt ingegeven zal i met de waarde 10 opgeslagen worden in de dictionairy program state. Voor deze dictionairy is de file [program_state.py.](https://github.com/ramonvbemmel/interpreter/blob/master/program_state.py) 

In de file operators.py staan operators gespecificeerd.  
## Hoe te gebruiken? 
Door de file main.py uit te voeren wordt de interpreter gestart. De gebruiker zal hier om een source file gevraagd worden. Geef de naam van uw source file op (.txt)  wanneer de source file in de zelfde map als de main.py file staat anders geeft u het volledige path naar de file op (**gebruik forward slash /**). In de repo zit een voorbeeld.txt source file. 

|syntax Rampthon  |python syntax  |
|--|--|
|toon <variable of string>  | print()  |
| is | = | 
|""| ''|
|maal| * | 
| plus| + | 
|min|-| 
|deel| /|








