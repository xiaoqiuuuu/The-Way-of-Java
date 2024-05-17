#include<bits/stdc++.h>
#define long long int
using namespace std;
int n,m;
int tmp=0;
int fa[300005],d[300005];
unordered_map<int,int>q;
int g(int pp){
    if(q.count(pp)==0)q[pp]=++tmp;
    return q[pp];
}
int find(int w){
    if(fa[w]!=w){
        int tmp=find(fa[w]);
        d[w]^=d[fa[w]];
        fa[w]=tmp;
    }
    return fa[w];
}
int ans;
signed main()
{
     cin>>n;
     cin>>m;
     ans=m;
     int x,y;
     string tt;
     for(int i=1;i<=5*m;i++){
         fa[i]=i;
     }
     for(int i=1;i<=m;i++){
         cin>>x>>y;
         cin>>tt;
         x = g(x-1),y=g(y);
         int t=0;
         if(tt=="odd")t=1;
         int p1,p2;
         p1=find(x),p2=find(y);
         if(p1==p2){
            if((d[x]^d[y])!=t){
                ans=i-1;
                break;
            }
         }
         else{
             fa[p1]=p2;
             d[p1]=(d[x]^d[y]^t);
             
         }
         
     } 
     cout<<ans;
   return 0;
}