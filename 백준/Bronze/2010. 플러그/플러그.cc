#include <stdio.h>
int main(){
	int n, ans=0;
	scanf("%d", &n);
	for(int i=0; i<n; i++){
		int hole;
		scanf("%d", &hole);
		ans += hole;
	}
	if(n>1) ans -= (n-1);
	printf("%d", ans);
}