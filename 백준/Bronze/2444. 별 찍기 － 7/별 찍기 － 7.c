#include <stdio.h>
int main(){
	int n;
	scanf("%d", &n);
	
	int m = 2*n-1;
	
	for(int i=1; i<=m; i++){
		int sp, st;
		if(i<=n){
			sp = n-i;
			st = 2*i-1;
		}
		else{
			sp = i-n;
			st = 2*(m-i)+1;
		}
		for(int j=1; j<=sp; j++){
			printf(" ");
		}
		for(int j=1; j<=st; j++){
			printf("*");
		}
		printf("\n");
	}
}