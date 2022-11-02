#include <iostream>
#include <vector>
#include <algorithm>

#include <queue>

using namespace std;

int v ,e;
vector< pair<int, int> > node[100000];
int dist[100000] = {100000};
vector< pair<int, int> >::iterator it;
bool visited[100000];
void jikstra(){
	priority_queue<pair<int, int>,vector<pair<int, int> >,greater<pair<int, int> > > qiu;
	for (int i = 0; i < 100000; ++i)
	{
		visited[i] = false;
		dist[i] = 100000;
	}


	dist[0] = 0;
	qiu.push(make_pair(0, 0));

	visited[0] = true;
	while(qiu.empty() == 0){
		int temp = qiu.top().second;
 		qiu.pop();      visited[temp] = true; 
		for(it = node[temp].begin(); it != node[temp].end(); ++it){
            int node_v = (*it).first;
            int weight = (*it).second;
            if(dist[node_v] > dist[temp] + weight && visited[node_v] == false){
                dist[node_v] = dist[temp] + weight;
                qiu.push(make_pair(dist[v],node_v));
            }
        }

	}

	     


}

int main(int argc, char const *argv[])
{
	cin >> v >> e;
	int x, y, z;
	for (int i = 0; i < e; ++i)
	{
		cin >> x >> y >> z;
		node[x].push_back(make_pair(y, z));
		node[y].push_back(make_pair(x, z));
	}
	jikstra();
	int hasil = 0;
	for (int i = 1; i < v; ++i)
	{
		hasil += dist[i];
	}
	hasil = hasil / v;
	cout << hasil << endl;
	return 0;
}
