#include <stdio.h>

int main(){
	int n, k, coin=0;
	scanf("%d %d", &n, &k);
	
	int arr[n];
	for(int i=0; i<n; i++){
		scanf("%d", &arr[i]);
	}
	
	for(int i=n-1; i>=0; i--){
		if (arr[i] <= k){
			coin += k/arr[i];
			k%=arr[i];
		}
	}
	printf("%d", coin);
}