import nltk
nltk.download('punkt')
from nltk.parse import ShiftReduceParser

grammar = nltk.CFG.fromstring("""

S -> NP VP
NP -> PropN | N PP | Det N
VP -> V NP | V S | VP PP | NP PP
PP -> P NP 
PropN -> 'He'| 'Utsav'
Det -> 'some' | 'the'
N -> 'compilerdesign' | 'programming'
V -> 'eats' | 'studies'
P -> 'and' | 'in' | 'is'

""")

sr = ShiftReduceParser(grammar)
sentence1 = 'Utsav studies compilerdesign and some programming'
tokens = nltk.word_tokenize(sentence1)
for x in sr.parse(tokens):
    print(x)

    
    
    /*DESCRIPTION-: Shift Reduce parser attempts for the construction of parse in a similar manner as
done in bottom-up parsing i.e. the parse tree is constructed from leaves(bottom) to the root(up). A
more general form of the shift-reduce parser is the LR parser. This parser requires some data
structures i.e. An input buffer for storing the input string. A stack for storing and accessing the
production rules.
Basic Operations –
Shift: This involves moving symbols from the input buffer onto the stack.
Reduce: If the handle appears on top of the stack then, its reduction by using appropriate production
rule is done i.e. RHS of a production rule is popped out of a stack and LHS of a production rule is
pushed onto the stack.
Accept: If only the start symbol is present in the stack and the input buffer is empty then, the parsing
action is called accept. When accepted action is obtained, it is means successful parsing is done.
Error: This is the situation in which the parser can neither perform shift action nor reduce action and
not even accept action.
E -> E+T|E-T|T
T -> T*F| T/F | F
F -> (E) | digit


ALGORITHM-:
1. Start.
2. Push the current symbol in stack at each push action.
3. Replace the symbol by a non-terminal when pop is called.
4. Display and continue for each symbol until only $ is left, therefore it is accepted.
5. Stop.

*/
