#include <stdio.h>
#include <string.h>
int main(){
	char s[100];
	scanf("%s", &s);
	
	int l = strlen(s)-1;
	for(int i=0; i<l; i++){
		if(s[i] != s[l-i]){
			printf("0");
			return 0;
		}
	}
	printf("1");
}