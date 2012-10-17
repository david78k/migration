#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <sys/resource.h>

main (int argc, char **argv) { 
	//printf ("double %d bytes\n", sizeof (double));

	int i = 0;
	// total memory allocated in MB
	int mem_alloc = 400; 
	int mem_alloc_bytes = 0; 
	// memory update rate in MB
	int mem_update = 4; 
	int sleep_time = 1; 
	double *d;

	if(argc < 2) {
		printf("usage: %s size\n", argv[0]);
		//perror("usage: %s size", argv[0]);
		exit (1);
	}

	mem_alloc = atoi (argv[1]);
	mem_alloc_bytes = mem_alloc * 1024 * 1024; 

	d = malloc (mem_alloc_bytes);
	printf ("mem allocated: %d\n", mem_alloc);
	for (i = 0; i < mem_alloc_bytes/sizeof(double); i ++) {
		d[i] = i;
	}

	while (1) {
		sleep (sleep_time);
	}
}

