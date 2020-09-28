#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
const int maxn = 400000 + 10;
const int maxe = 1000000 + 10;
char s1[maxn];
int len;
int nextv[maxn];
int ans[maxn];
void getnext(){
	int i = 0,j = -1;
	nextv[0] = -1;
	while(i<len){
		if(j == -1 || s1[j] == s1[i]){
			nextv[++i] = ++j;
		}
		else
			j = nextv[j];
	}
}
int main(){
	int n;
	while(scanf("%s",s1)!=EOF){
		// memset(nextv,0,sizeof(nextv));
		len = strlen(s1);
		getnext();
		int tmp = len;
		ans[0] = len;
		int cnt = 1;
		while(nextv[tmp]!=0){ 
			ans[cnt++]=nextv[tmp];
			tmp = nextv[tmp];
		}
		for(int i=cnt-1;i>0;i--)
			printf("%d ",ans[i]);
		printf("%d\n",ans[0]);
	}
	return 0;
}
