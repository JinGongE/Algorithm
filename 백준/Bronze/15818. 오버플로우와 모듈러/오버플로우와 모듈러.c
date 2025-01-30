#include <stdio.h>
int main(){
	int n, m, k;
	long long int result=1;
	scanf("%d %d", &n, &m);
	for(int i=0; i<n; i++){
		scanf("%d", &k);
		result = ((result%m)*(k%m))%m;
	}
	printf("%d", result);
}
