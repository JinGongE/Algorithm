#include <stdio.h>
int main(void){
	int n;
	scanf("%d", &n);
	
	for(int i=0; i<n; i++){
		char str[21];
		int j=0;
		scanf("%s", &str);
//		printf("%c", str[-1]);
		while(str[j]!='\0'){
			if(str[j] >= 'A' && str[j] <= 'Z'){
				str[j]+=32;
			}
			j++;
		}
		printf("%s\n", str);
	}
}