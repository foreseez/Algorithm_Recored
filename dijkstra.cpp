#include<bits/stdc++.h>
#define Inf 0x3f3f3f3f
const int maxn=1e5+5;
typedef long long ll;
using namespace std;
struct edge
{
    int u,v,w;
    int next;
}Edge[10*maxn];

struct node
{
    int pos,w;
    node(int x,int y)
    {
        pos=x;
        w=y;
    }
    bool friend operator < (node x,node y)
    {
        return x.w>y.w;
    }
};
int head[1005],dis[1005],vis[1005],cnt=0;
void add(int u,int v,int w)
{
    Edge[cnt].u=u;
    Edge[cnt].v=v;
    Edge[cnt].w=w;
    Edge[cnt].next=head[u];
    head[u]=cnt++;
}
void Dijkstra(int s)
{
    dis[s]=0;
    priority_queue<node>q;
    q.push(node(s,0));
    while(!q.empty())
    {
        node now=q.top();
        q.pop();
        if(vis[now.pos])continue;
        vis[now.pos]=1;
        
        for(int i=head[now.pos];i!=-1;i=Edge[i].next)
        {
            if(dis[now.pos]+Edge[i].w<dis[Edge[i].v])
            {
                dis[Edge[i].v]= dis[now.pos]+Edge[i].w;
                q.push(node(Edge[i].v,dis[Edge[i].v]));
            } 
        }
    } 
    return ;
}
class Solution{
     public :
     int Getans(vector<vector<int> >times,int n,int k){
       memset(head,-1,sizeof(head));
       memset(dis,Inf,sizeof(dis)); 
         int m=times.size();
         for(int i=0;i<m;i++){
            add(times[i][0],times[i][1],times[i][2]);
         }
         Dijkstra(k);
         int ans=0;
         for(int i=1;i<=n;i++){
          ans=max(ans,dis[i]);
         }
         if(ans==Inf){
          return -1;
         }
         else{
          return ans;
         }
     }

};
int main()
{
   Solution s;
   vector< vector<int> > vec(3);  
  for(int i=0;i<vec.size();i++)
    vec[i].resize(3);
   for(int i=0;i<3;i++){
      for(int j=0;j<3;j++){
        int x;
        cin>>x;
        vec[i][j]=x;
      }
   }
   
   cout<<s.Getans(vec, 4, 2)<<endl;
   return 0;
}
