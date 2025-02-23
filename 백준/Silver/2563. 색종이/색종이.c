#include <stdio.h>
int main(){
	int n, area = 0;
	int sq[100][100] = {0};
	int x, y;
	
	scanf("%d", &n);
	
	for(int i=0; i<n; i++){
		scanf("%d %d", &x, &y);
		for(int j=y; j<y+10; j++){
			for(int k=x; k<x+10; k++){
				if(sq[j][k] == 0){
					area += 1;
					sq[j][k] = 1;
				}
			}
		}
	}
	printf("%d", area);
}