#include <stdio.h>
int main(){
	char str[1000000];
	int a = 0;
	scanf("%s", &str);
	for(int i=0; i<sizeof(str); i++){
		if (str[i] == '\0'){
			break;
		}
		else{
			a = ((a * 10) + (str[i]-'0')) % 20000303;
		} 
	}
	printf("%d", a);
}