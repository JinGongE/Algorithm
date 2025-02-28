#include <stdio.h>

int main(){
	int N,M, t;
	int arr[100001];
	int i, j;
	scanf("%d %d", &N, &M);
	
	for(int k=1; k<=N; k++){
		scanf("%d", &t);
		if(k>0){
			arr[k] = arr[k-1]+t;
		}
		else{
			arr[k] = t;
		}
	}
	
	for(int k=0; k<M; k++){
		scanf("%d %d", &i, &j);
		printf("%d\n", arr[j]-arr[i-1]);
	}
}