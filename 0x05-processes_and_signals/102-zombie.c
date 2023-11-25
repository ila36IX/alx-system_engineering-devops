#include <stdio.h>
#include <unistd.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>


/**
 * infinite_while - while that doesn't stop
 *
 * Return: 0 in seccess
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - The entry function
 *
 * Return: 0 in sessess
 */
int main(void)
{
	pid_t pid, child_pid;
	int i, status;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid == 0)
		{
			pid = getpid();
			printf("Zombie process created, PID: %d\n", (int) pid);
			return (0);
		}
		else
		{
			wait(&status);
		}
	}
	infinite_while();
	return (0);

}
