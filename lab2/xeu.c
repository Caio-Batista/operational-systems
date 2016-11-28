#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {


while(1){

char *line = NULL;
size_t linecapp = 0;
getline(&line, &linecapp, stdin);

char *input =line;
char delimiter[] = " ";
char *firstWord, *secondWord, *remainder, *context;

int inputLength = strlen(input);
char *inputCopy = (char*) calloc(inputLength + 1, sizeof(char));
strncpy(inputCopy, input, inputLength);

firstWord = strtok_r (inputCopy, delimiter, &context);
secondWord = strtok_r (NULL, delimiter, &context);
remainder = context;

printf("%s\n", firstWord);
printf("%s\n", secondWord);
printf("%s\n", remainder);

//getchar();
//free(inputCopy);


char *name[3];

name[0] = firstWord;
name[1] = secondWord;
execvp(remainder, name);
}


 return 0;
}
