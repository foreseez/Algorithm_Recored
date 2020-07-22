//
// Created by 曾玉健 on 2020/7/20.
//

#include<bits/stdc++.h>
using namespace std;
bool check(int x){

    int a[15];
    while(1){
        int tmp=x;
        if(x>=0&&x<10){
            if(x==7)return true;
            else return false;
        }
        int cnt=0;
        while(tmp){
            a[cnt]=tmp%10;
            cnt++;
            tmp/=10;
        }
        x=0;
        for(int i=cnt-1;i>=1;i--){
            x=x*10+abs(a[i]-a[i-1]);
        }
        //cout<<x<<endl;
    }
}
int main(){
    int T;
    cin>>T;
    while(T--){
        int l,r;
        scanf("%d%d",&l,&r);
        int ans=0;
        for(int i=l;i<=r;i++){
            ans+=check(i);
        }
        printf("%d\n",ans);
    }
    return 0;
}