#include <stdio.h>

int main(){
	int arr[9][9];
	int max = 0;
	int r=0, c=0;
	for(int i=0; i<9; i++){
		for(int j=0; j<9; j++){
			scanf("%d", &arr[i][j]);
			if(max < arr[i][j]){
				max = arr[i][j];
				r = i;
				c = j;
			}
		}
	}
	printf("%d\n", max);
	printf("%d %d", r+1, c+1);
}