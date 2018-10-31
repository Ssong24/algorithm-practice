#include <iostream>

using namespace std;

int memo[41] = {1,1,};

int fibonacci(int n) {
    if(n <= 1) {
        return memo[n];
    } else if(memo[n] >0) 
        return memo[n];
    else{ 
        memo[n] = fibonacci(n-1) + fibonacci(n-2);
        return memo[n];
    }
    
}


int main(void) {
	int test_num;


	scanf("%d", &test_num);

	for (int i = 0; i < test_num; i++) {
		int N;
		scanf("%d", &N);
    
        if(N == 0) {
            printf("1 0\n");
        } else if (N==1) {
            printf("0 1\n");
        }else {
		    fibonacci(N);
            printf("%d %d\n", memo[N-2], memo[N-1]);
        }

	}
    return 0;
}

	 
