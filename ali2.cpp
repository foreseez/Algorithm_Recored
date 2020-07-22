#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
    int t;
    cin>>t;
    ll n,k;
    while(t--){
        scanf("%lld%lld",&n,&k);
        if(n%k!=0){
            printf("-1\n");
            continue;
        }
        ll ans=n/k;
        if(ans-3<3){
            printf("-1\n");
        }
        else{
            if((ans-3)%2==1){
                if(ans-3>=3){
                    printf("%lld %lld %lld\n",k,2*k,(ans-3)*k);
                }
                else{
                    printf("-1\n");
                }


            }
            else{

                if(ans/2%2==0){
                    if(ans/2-1>1)
                        printf("%lld %lld %lld\n",k,(ans/2-1)*k,(ans/2+1)*k);
                    else{
                        printf("-1\n");
                    }
                }
                else{
                    if(ans/2-2>1)
                        printf("%lld %lld %lld\n",k,(ans/2-2)*k,(ans/2+2)*k);
                    else{
                        printf("-1\n");
                    }
                }

            }
        }
    }
    return 0;
}