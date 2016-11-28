#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

int main(void) {
    char *name[] = {NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL};
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
	  printf("%s", a);
	   
	   int j = 0;
	   while(a!=NULL){
		
		name[j] = a;
		++j;
		a = strtok(NULL, " \n\0");  
	} 	
		
	name[j] = NULL;
    
    strcat(path, name[0]);
    printf("\n <%s> \n", path);
    printf("\n <%s> \n", name);
   
    pid_t pid = fork();	
    	
   if (pid == 0){ 
	   	
    execve(path, name, env);
    
    _exit(EXIT_FAILURE);
    
    
	}else if(pid > 0){
		wait(NULL);	
	}else{
		printf("Fuu"); 
	}
	
	return 0;
}


/*
int main(void)
{
    char *argv[] = { "/bin/sleep", "3", "env", 0 };
    char *envp[] =
    {
        "HOME=/",
        "PATH=/bin:/usr/bin",
        "TZ=UTC0",
        "USER=beelzebub",
        "LOGNAME=tarzan",
        0
    };
    execve(argv[0], &argv[0], envp);
    fprintf(stderr, "Oops!\n");
    return -1;
}
*/
