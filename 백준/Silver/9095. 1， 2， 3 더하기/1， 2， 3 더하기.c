#include <stdio.h>

int f(int n){
	if(n<=1) return 1;
	else{
		return (f(n-1) * n);
	}
}

int main(){
	int T,n, result;
	
	scanf("%d", &T);
	
	for(int k=0; k<T; k++){
		result=0;
		scanf("%d", &n);
		for(int i=0; i<=n/3; i++){		//3의 개수 
			for(int j=0; j<=n/2; j++){	//2의 개수
				if (n-3*i-2*j >= 0){
					result += f(n-2*i-j)/f(i)/f(j)/f(n-3*i-2*j);
				}
			}
		}
		printf("%d\n", result);
	}
}