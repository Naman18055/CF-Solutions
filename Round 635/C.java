import java.util.*;
public class Main{
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int n = input.nextInt();
		int k = input.nextInt();
		ArrayList<Integer>[] arr = new ArrayList[n];
		for (int i=0;i<n;i++){
			arr[i] = new ArrayList<Integer>();
		}
		for (int i=0;i<n;i++){
			int a = input.nextInt();
			int b = input.nextInt();
			arr[a-1].add(b-1);
			arr[b-1].add(a-1);
		}
		int[][] depth = new int[n][2];
		depth[0][0]=0;
		depth[0][1]=0;
		ArrayList<Integer>[] height = new ArrayList[n];
		int[] visited = new int[n];
		visited[0]=1;

	}
	public void bfs(int root){
		Queue<Integer> queue = new LinkedList<>();
		int[] vis = new int[n];
		for (int i=0;i<n;i++){
			vis[i]=0;
		}
		
	}
	public void dfs(int root){

	}
}