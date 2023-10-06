#include<vector>
#include<queue>
#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

int solution(vector<vector<int> > maps)
{
    int visited[101][101]={-1,};
    memset(visited, -1, sizeof(visited));
    int n = maps.size();
    int m = maps[0].size();
    visited[0][0] =1;
    
    queue<pair<int,int>> q;
    q.push({0,0});
    
    int dx[4] = {1, -1 ,0,0};
    int dy[4] = {0,0,1,-1};
    
    while(!q.empty()){
        int y = q.front().first;
        int x = q.front().second;
        q.pop();
        
        for(int i =0; i<4; i++){
            int nx = dx[i] + x;
            int ny = dy[i] + y;
            if(0<= nx && nx < m && 0<= ny && ny < n){
                if(maps[ny][nx] ==1 && visited[ny][nx] == -1){
                    visited[ny][nx] = visited[y][x]+1;  
                    q.push({ny, nx});
            }
            }
        }
        
    }
    
    
    
    return visited[n-1][m-1];
}