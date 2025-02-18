#include <stdio.h>

#define max(x, y) (x)>(y) ? (x) : (y)

int main(){
	int n;
	int arr[300] = {};
	int dp[300] ={};
	
	scanf("%d", &n);
	
	for(int i=0; i<n; i++){
		scanf("%d", &arr[i]);
	}
	dp[0] = arr[0];
	if(n>1) dp[1] = arr[0] + arr[1];
	if(n>2) dp[2] = max(arr[2] + arr[0], arr[1] + arr[2]);
	if(n>3){
		for(int i=3; i<n; i++){
			dp[i] = max(arr[i] + dp[i-2], arr[i] + arr[i-1] + dp[i-3]);
		}
	}
	printf("%d", dp[n-1]);
}