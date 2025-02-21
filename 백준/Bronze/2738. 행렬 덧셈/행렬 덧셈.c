#include <stdio.h>

int main(){
	int a, b, k;
	scanf("%d %d", &a, &b);
	
	int arr[100][100];
	
	for(int i=0; i<a; i++){
		for(int j=0; j<b; j++){
			scanf("%d", &arr[i][j]);
		}
	}
	for(int i=0; i<a; i++){
		for(int j=0; j<b; j++){
			scanf("%d", &k);
			printf("%d ", arr[i][j]+k);
			//arr[i][j] += k;
		}
		printf("\n");
	}
}