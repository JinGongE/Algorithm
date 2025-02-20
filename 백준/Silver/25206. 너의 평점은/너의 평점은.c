#include <stdio.h>

int main(){
	float sum=0;
	int c=0;
	
	for(int i=0; i<20; i++){
		char name[50];
		float crd;
		char g[2];
		scanf("%s %f %s", &name, &crd, &g);
		if(g[0] != 'P') c += crd;
				
		if(g[0] == 'A') sum+=4*crd;
		else if(g[0] == 'B') sum+=3*crd;
		else if(g[0] == 'C') sum+=2*crd;
		else if(g[0] == 'D') sum+=1*crd;
		
		if(g[1] == '+') sum+=0.5*crd;
	}
	printf("%f", sum/c);
}