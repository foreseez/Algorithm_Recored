#include<cstdio>
#include<algorithm>
using namespace std;
int n,m;
int main()
{
    scanf("%d %d",&n,&m);
    int k=__gcd(n,m);//最大公约数
    printf("%d",k);
    return 0;
}
