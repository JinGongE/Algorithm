#include <stdio.h>
#include <string.h>
#include <math.h>

int main(){
    int B;
    char N[1000];
    long long int de=0;

    scanf("%s %d", &N, &B);
    if(B != 10){
        int j = 0;
        for(int i=strlen(N)-1; i>=0; i--){
            if(N[j]>='A' && N[j] <= 'Z'){
                de += ((int)N[j]-55)*pow(B, i);
            }
            else{
                de += ((int)N[j]-48)*pow(B, i);
            }
            j++;
        }
        printf("%lld", de);
    }
    else{
        printf("%s", N);
    }
}