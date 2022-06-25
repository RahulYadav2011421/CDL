#include <stdio.h>
#include <string.h>
int main()
{
char icode[10][30], str[20], opr[10];
int i = 0;
printf("\nEnter Set Of Intermediate Code:\n");
do
{
scanf("%s", icode[i]);
} while (strcmp(icode[i++], "exit") != 0);
printf("\nTarget Code Generation");
printf("\n*******************");
i = 0;
do
{
strcpy(str, icode[i]);
switch (str[3])
{
case '+':
strcpy(opr, "ADD");
break;
case '-':
strcpy(opr, "SUB");
break;
case '*':
strcpy(opr, "MUL");
break;
case '/':
strcpy(opr, "DIV");
break;
}
printf("\n\tMov %c,R%d", str[2], i);
printf("\n\%s%c,,R%d", opr, str[4], i);
printf("\n\tMov R%d%c", i, str[0]);
} while (strcmp(icode[++i], "exit") != 0);
return 1;
}



/*DESCRIPTION-: A compiler is a computer program that implements a programming language
specification to “translate” programs, usually as a set of files which constitute the source code written
in source language, into their equivalent machine readable instructions (the target language, often
having a binary form known as object code). Code generation: The transformed language is translated
into the output language, usually the native machine language of the system. This involves resource
and storage decisions, such as deciding which variables to fit into registers and memory and the
selection and scheduling of appropriate machine instructions along with their associated modes.
Debug data may also need to be generated to facilitate debugging.
ALGORITHM-:
1. Start.
2. Open the source file and store the contents as quadruples.
3. Check for operators, in quadruples, if it is an arithmetic operator generator it or if assignment
operator generates it, else perform unary minus on register C.
4. Write the generated code into output definition of the file in outp.c
5. Print the output.
6. Stop*/
