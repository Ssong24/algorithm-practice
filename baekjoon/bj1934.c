#include <stdio.h>

int main() {
	int a, b, temp1, temp2;
	int r;
	int inputNum;

	scanf("%d", &inputNum);

	while (inputNum--)
	{
		r = 1; // while 문에 넣어주기!

		scanf("%d %d", &a, &b);
		temp1 = a;	temp2 = b;

		if (a > b)
		{
			a = temp2;
			b = temp1;
		}
		// 유클리드 호제법 - LCM
		while (r > 0)
		{
			r = b % a;
			b = a;
			a = r;
		}
		printf("%d\n", temp1 * temp2 / b);
	}
	return 0;
}
