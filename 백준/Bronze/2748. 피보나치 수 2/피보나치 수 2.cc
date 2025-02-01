#include <stdio.h>
int main(){
	int n;
	unsigned long long int a=1, s=1, t;
	scanf("%d", &n);
	for(int i=2; i<n; i++){
		t=a;
		a+=s;
		s=t;
	}
	printf("%lld", a);
}