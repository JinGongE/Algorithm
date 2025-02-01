#include <stdio.h>
int main(){
	char str[15][15];
	
	for(int i=0; i<15; i++){
		for(int j=0; j<15; j++){
			 str[i][j] = '\0';
		}	
	}
	
	for(int i=0; i<5; i++){
		scanf("%s", &str[i]);
	}
	for(int i=0; i<15; i++){
		for(int j=0; j<15; j++){
			if(str[j][i] != '\0'){
				printf("%c", str[j][i]);
			}
		}	
	}
}