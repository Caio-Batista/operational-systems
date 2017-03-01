#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

int main(void) {
	
	char *history[100];
	char *username;
	username = getenv("USER");
	
	int contador = 1;
	while(contador){
	printf("%s@shell2.0$ ", username);
    char *name[] = {NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL};
    char *name2[] = {NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL};
    char path[30];
    strcpy(path,"/bin/");
    char *env[] = {
		
		"HOME=/",
        "PATH=/bin:/usr/bin",
        "TZ=UTC0",
        NULL
		
		};
    char *line = NULL;
    size_t linecapp = 0;
    getline(&line, &linecapp, stdin);
    
	  char *a= strtok(line, " \n\0");
	  
	   
	   int j = 0;
	   while(a!=NULL){
		
		name[j] = a;
		++j;
		a = strtok(NULL, " \n\0");  
	} 	
		
	name[j] = NULL;
    
    strcat(path, name[0]);
    history[contador] = name[0];
    pid_t pid = fork();	
   char *track= "track";
   if (strcmp(name[0], track) == 0 && pid == 0){
	 
       int i;
		for (i=1;i < sizeof(history) ;i++) {
			if (history[i] != NULL || history[i] > 0 ){
				
			    printf("%d. %s\n", i, history[i]);
			    if (strcmp(history[i], track) == 0)
				{break;}
			}    
		}

   } 	
   else if (pid == 0){ 
	   	
    execve(path, name, env);
    
    _exit(EXIT_FAILURE);
    
    
	}else if(pid > 0){
		wait(NULL);	
	}else{
		printf("Fuu"); 
	}
	contador++;
}
	return 0;
}



