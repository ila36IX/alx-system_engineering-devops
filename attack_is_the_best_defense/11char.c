#include <stdio.h>
#include <string.h>

void prog(int curr, int lv, int max) 
{
	double p;

	printf("[");
	for (int i = 0; i < curr; i++)
	{
		printf("=");
	}
	printf(">");
	for (int i = curr; i < max; i++)
	{
		printf(" ");
	}
	p = ((double) curr / (double) max) * 100;
	printf(" ] %d%%\r", (int) p);
}

int main()
{
	FILE *fp = fopen("pass.txt", "r");
	FILE *fp1 = fopen("pass1.txt", "a");
	char *line;
	long unsigned int length, progress, dot;
	size_t len = 0;
	ssize_t read;
	
	progress = 0, dot = 0;
	while((read = getline(&line, &len, fp) != -1))
	{
		length = strlen(line);
		if (length == 12)
		{
			fwrite(line, 1, 12, fp1);
		}
		if (!(progress % 500))
		{
			prog(dot, progress, 50);
			fflush(stdout);
			dot++;
		}
		progress++;
	}
	fclose(fp);
	fclose(fp1);
	
	return (0);
}
