#include <stdio.h>

#define MAX(x, y) (x)>(y) ? (x) : (y)

int n;
int memo[301][3] = {};
int arr[301] = {};

void f(int stair, int score, int cnt){
	score += arr[stair];
	if(memo[stair][cnt] > score && stair < n-1){
		return;
	}
	else{
		if(memo[stair][cnt] < score) memo[stair][cnt] = score;
		
		if(stair == n){
			return;
		}
		else{
			if(stair+2 <= n) f(stair+2, score, 1);
			if(cnt<2) f(stair+1, score, cnt+1);
		}		
	}
}


int main(){
	scanf("%d", &n);
	
	for(int i=1; i<=n; i++){
		scanf("%d", &arr[i]);
	}
	f(0, 0, 0);
	
	printf("%d\n", MAX(memo[n][2], memo[n][1]));
}