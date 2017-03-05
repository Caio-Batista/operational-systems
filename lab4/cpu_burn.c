#include <math.h>
#include <sched.h>
#include <string.h>
#include <limits.h>

 int main(int argc, char *argv[]) {
	int count = 524436200;
	if (strcmp(argv[1], "0") == 0) {
		while(count-- != 0) {
			pow(1.2, 2.3);
		}
		return 0;
	}
	else if (strcmp(argv[1], "1") == 0) {

		struct sched_param param;
		param.sched_priority = 99;
		sched_setscheduler(0, SCHED_FIFO, &param);

		while(count-- != 0) {
			pow(1.2, 2.3);
		}
		return 0;	
	}
	else if (strcmp(argv[1], "2") == 0) {

		struct sched_param param;
		param.sched_priority = 99;
		sched_setscheduler(0, SCHED_RR, &param);

		while(count-- != 0) {
			pow(1.2, 2.3);
		}
		return 0;
	}
 }
