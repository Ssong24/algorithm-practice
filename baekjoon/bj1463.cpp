#include <iostream>

using namespace std;

int memo[1000001];

int leastNum(int n) {
    if(n == 1) 
        return 0;
    if(memo[n] > 0)
        return memo[n];

    memo[n] = 1 + leastNum(n-1);
    
    if((n % 2)==0){
        int temp = 1 + leastNum(n/2);   // 나누기를 나머지 연산으로 착각함...ㅜㅡ
        memo[n] = min(memo[n], temp);
    }
    if((n % 3)==0) {
        int temp = 1 + leastNum(n/3);
        memo[n] = min(memo[n], temp);
    }  
    return memo[n];
}


int main(void) {
    int num;
    scanf("%d", &num);
    printf("%d\n", leastNum(num));
    
    return 0;
    
}
