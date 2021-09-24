#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

#define MAX 100

int strindex(char[], char[]);
int main(int argc, char *argv[])
{
	int opt;
	FILE *in= fopen("file.in", "r");
	int i = 0, index = 0;
	char str[MAX];

	while((opt = getopt(argc, argv, "rf:")) != -1) {
		switch(opt) {
		case 'r':
			if(!in)
			{
				printf("Can't find file\n");
				break;
			} else
			{
				fgets(str, sizeof(str), in);
				printf("%s\n", str);
				fclose(in);	
				break;
			}
			case 'f':
				if(!in)	
				return 1;
			fgets(str, sizeof(str), in);
			printf("str: %s", str);
			printf("optarg: %s\n", optarg);

			if((index = strindex(str,optarg)) >= 0) {
				printf("%d\n", index);
				str[index] = 'L';
				str[index+1] = 'I';
				str[index+2] = 'N';
				str[index+3] = 'U';
				str[index+4] = 'X';
				printf("changed str: %s\n", str);
			}
			fclose(in);

			/* write changed string to file */
			in = fopen("file.in", "w");
			if(!in)
			{
				printf("can't find the file\n");
				return 1;
			}
			fprintf(in, str);
			//fclose(in);
		}
		return 0;
		
	} fclose(in);
}

/* strindex: return of t in s, -1 if non */
int strindex(char s[], char t[])
{
	int i, j, k;
	for(i = 0; s[i] != '\0' ; i++) {
		for(j = i, k = 0; t[k] != '\0' && s[j] == t[k]; j++, k++)
			;
		if(k > 0 && t[k] == '\0')
			return i;
	}
	return -1;
}

					
