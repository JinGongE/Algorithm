#include <stdio.h>
#include <string.h>

int main(){
	int n, c=0;
	
	char word[100];
	
	scanf("%d", &n);
	c=n;
	
	for(int i=0; i<n; i++){
		int alph[26] = {};
		scanf("%s", &word);
		for(int j=0; j<strlen(word); j++){
			if(alph[(int)word[j]-97] != 0 && word[j] != word[j-1]){
				c-=1;
				break;
			}
			else alph[(int)word[j]-97] = 1;
		}
	}
	printf("%d", c);
}