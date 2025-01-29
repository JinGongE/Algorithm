#include <stdio.h>

int f(int n){
	int result = 1;
	for(int i=n; i>0; i--){
		result *= i;
	}
	return result;
}


int main(void){ 
	int n=1;
	while(1){
		scanf("%d", &n);
		if(n==0) break;
		else{
			int c=1, sum=0;
			while(1){
				int m = n%10;
			//	printf("n: %d, m=%d\n", n, m);
				sum += f(c)*m;
				c++;
				if(n<10) break;
				else n/=10;
			}
			printf("%d\n", sum);
		}
		
	}
}