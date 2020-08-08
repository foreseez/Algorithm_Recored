#include<bits/stdc++.h>
using namespace std;
int main(){
    long long n,num,res = 0;
    cin >> n;
    for (int i = 0;i< n;i++){
        cin>>num;
        res += num / 2;
    }
    cout<<   res << endl;
    return 0;
}

