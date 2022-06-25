import re
j = 1
y = []
op = ['+', '-', '/', '*']
x = input("ENTER THE EXPRESSION : ")
m = re.split('([+-/*])', x)
def comp(m, j):
  for word in m:
    if word in op:
      y.append(''.join(m[0:3]))
      m.pop(0)
      m.pop(0)
      m[0] = 't'+str(j)
      j += 1
  return m, j
while len(m) > 1:
  m, j = comp(m, j)
k = len(y)
y.reverse()
for i in range(0, len(y)):
  print('t'+str(k)+'='+y[i])
  k -= 1

  
  
 /*DESCRIPTION-: The compilation process can be divided into a number of subtasks called phases.
The different phases involved are
• Lexical analysis
• Syntax analysis
• Intermediate code generation
• Code Optimization
• Code generation.
Intermediate Code Generation Once the syntactic constructs are determined, the compiler can generate
object code for each construct. But the compiler creates an intermediate form.
It helps in code optimization and also to make a clear-cut separation between machine independent
phases (lexical, syntax) and machine dependent phases (optimization, code generation). One form of
intermediate code is a parse tree.
A parse tree may contain variables as the terminal nodes. A binary operator will be having a left and
right branch for operand1 and operand2. Another form of intermediate code is a three-address code.
It has got a general structure of A = B op C, where A, B and C can be names, constants, temporary
names etc. op can be any operator. Postfix notation is yet another form of intermediate code.
ALGORITHM-:
1. Start.
2. Get an expression as input.
3. Scan the statement from left to right.
4. Frame new statements such that it performs one operation at a time, either assignment or
arithmetic or relational operations.
5. Display the new set of statements.
6. Stop.
*/
