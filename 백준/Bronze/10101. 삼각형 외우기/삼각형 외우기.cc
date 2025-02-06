#include <stdio.h>
int main(){
	int a, b, c;
	scanf("%d\n%d\n%d", &a, &b, &c);
	
	if(a+b+c==180){
		if(a== 60 && b==60 && c==60) printf("Equilateral");
		else if(a!=b && b!=c && a!=c) printf("Scalene");
		else printf("Isosceles");
	}
	else printf("Error");
}