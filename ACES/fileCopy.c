#include <stdio.h>
#include <stdlib.h>

int file_copy(FILE *in, FILE *out);

int main()
{
	FILE *in, *out;

	in = fopen("file.in", "r");
	out = fopen("file.out", "w");

	printf("%d\n", file_copy(in, out));
	return 0;
}

int file_copy(FILE *in, FILE *out)
{
	char c;
	int a, b;

	a = fileno(in);
  	b = fileno(out);
 
  	if(a == -1 || b == -1)
	{	
		printf("error\n");
		return -1;
  		
	}
	while(read(a, &c, 1) == 1)
    		write(b, &c, 1);

  	return 0;
}






