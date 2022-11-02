#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
 
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
 
 
#define rep(i,a,n) for(int i = a; i < n; i++) 
#define INF (int)100000
int v,e;
 
int djikstra(vector<pii > adj[]){
     int D[100000];
     bool inMST[100000];
     for(int i = 0; i < 100000; i++){
        D[i] = INF; inMST[i] = false;
    }
     D[0] = 0;
     priority_queue<pii,vector<pii>,greater<pii> > q;
     q.push(make_pair(0,0));
      
    while(!q.empty()){
        int s = q.top().second; q.pop();
        vector<pii>::iterator it;
        inMST[s] = true;
        for(it = adj[s].begin(); it != adj[s].end(); ++it){
            int v = (*it).first;
            int weight = (*it).second;
            if(D[v] > D[s] + weight and inMST[v] == false){
                D[v] = D[s] + weight;
                q.push(make_pair(D[v],v));
            }
        }
    }
    int ans = 0;
    for(int i = 0; i < v; i++) ans += D[i];
    return ans/v;
    }
 
int main(){
    cin>>v>>e;
    vector<pii> adj[10000];
    for(int i = 0; i < e; i++){
        int x,y,z;
        cin>>x>>y>>z;
        adj[x].push_back(make_pair(y,z));
        adj[y].push_back(make_pair(x,z));
    }
    cout<<djikstra(adj)<<endl;
    return 0;
}
