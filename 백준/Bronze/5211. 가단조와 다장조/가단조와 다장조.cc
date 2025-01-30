#include <stdio.h>
#include <string.h>

int main(){
	char Cm[] = "CGF";
	char Am[] = "ADE";
	char music[100];
	
	scanf("%s", &music);
	
	bool checker = true;
	int C=0, A=0;
	char lastc[100];

	for(int i=0; i<sizeof(music); i++){
		char k = music[i];
		if (k =='\0'){
			char l = music[i-1];
			if (l =='C' || l == 'G' || l == 'F') strcpy(lastc, "C-major");
			else strcpy(lastc, "A-minor");
			break;
		}
		if(checker == true){
			for(int j=0; j<3; j++){
				if(k==Cm[j]){
					C+=1;
					break;
				}
				else if(k==Am[j]){
					A+=1;
					break;
				}
			}
			checker = false;
		}
		else if(music[i] == '|') checker = true;
	}
	
	if(C==A){
		printf("%s", lastc);
	}
	else if (C>A) printf("C-major");
	else printf("A-minor");
}