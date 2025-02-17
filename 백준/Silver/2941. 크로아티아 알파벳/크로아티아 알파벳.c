#include <stdio.h>
#include <string.h>
int main(){
	char s[100];
	scanf("%s", &s);
	int len = strlen(s);
	for(int i=0; i<strlen(s); i++){
		if(s[i] == '-'){
			len-=1;
		}
		else if(s[i]=='='){
			if(s[i-1]=='z' && i>1 && s[i-2]=='d') len-=2;
			else len-=1;
		}
		else if(s[i]=='j' && i>0){
			if(s[i-1] == 'l' || s[i-1] == 'n') len-=1;
		}
	}
	printf("%d", len);
}