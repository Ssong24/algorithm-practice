#include <queue>
#include <iostream>

using namespace std;

int a[100][100];
int dist[100][100];
int dx[] = { 1,0,-1,0 };
int dy[] = { 0, 1, 0, -1 };

int main(void) {
	int n, m;
	queue <pair<int, int>> q;

	scanf("%d %d", &n, &m);
	//printf("put number\n");
	// 자료값을 받아올 때 순서를 제대로 (j를 안의 반복문!!) -> 토마토 문제랑 다름 ㅠ
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			
			scanf("%1d", &a[i][j]);
			dist[i][j] = -1;
			
			if (a[i][j] == 1)
			{
				dist[i][j] = 1;
							//	q.push(make_pair(i, j));    // 여기서 가로부터 q에 담아서 밑에 문제. 
			} 
			
		}

	}
	q.push(make_pair(0, 0));
	dist[0][0] = 0;


	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;

		q.pop(); // 체크 한건 빼줘야 함.. 아니면 무한 루프
		for (int k = 0; k < 4; k++) {
			int nx = x + dx[k];
			int ny = y + dy[k];
			if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
				if (a[nx][ny] == 1 && dist[nx][ny] == 1)
				{
					dist[nx][ny] = dist[x][y] + 1;
					q.push(make_pair(nx, ny));
				}
			}
		}
	}


	
	/*
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			printf("%d ", dist[i][j]);
		}
		printf("\n");
	}
	*/

	printf("%d\n", dist[n-1][m-1]+1);
	return 0;

}
