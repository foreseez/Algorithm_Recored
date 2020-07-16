#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    scanf("%d",&t);
    while(t--){
    int n;
    scanf("%d",&n);
    string s;
    cin>>s;
    if(s[0] == '8'){
    int sz = s.size();
    if(sz>=11)
        puts("YES");
    else
        puts("NO");
    } else{
        int ma = -1;
        int sz = s.size();
        for (int i = 0;i<sz;i++){
        if(s[i]=='8'){
        ma = i;
        break;


        }


        }
        if(ma == -1||sz-ma<11)
            puts("NO");
        else
            puts("YES");

    }

    }

return 0;

    }
