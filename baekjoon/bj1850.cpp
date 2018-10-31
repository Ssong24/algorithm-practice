#include <iostream>
using namespace std;

void max(long long int,long long int);
long long int gcd(long long int, long long int);
long long int n1, n2;

int main(void)
{
 scanf("%lld %lld", &n1, &n2);
 max(n1, n2);
 for(int i=0; i < gcd(n1, n2); i++){
  printf("1");
 }
 printf("\n");

 return 0;
}

void max(long long int a, long long int b)
{
 long long int temp;
 if(a < b)
 {
  temp = a;
  a = b;
  b = temp;
 }
}

long long int gcd(long long int a, long long int b)
{
 while(b != 0)
 {
  long long int r = a%b;
  a = b;
  b = r;
 }
 return a;
}
