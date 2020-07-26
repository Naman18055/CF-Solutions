import java.util.*;

public class Main{
	public static void main(String[] args) {
		long mod = 1000000007;
		Scanner input = new Scanner(System.in);
		int n = input.nextInt();
		int m = input.nextInt();
		int k = input.nextInt();
		ArrayList<Integer>[] incoming = new ArrayList[n];
		for (int i=0;i<n;i++){
			incoming[i] = new ArrayList<Integer>();
		}
		for (int i=0;i<m;i++){
			int x = input.nextInt();
			int y = input.nextInt();
			incoming[y-1].add(x-1);
		}
		if (k==1){
			System.out.println(m);
			System.exit(0);
		}
		long[][] a = new long[n][1];
		for (int i=0;i<n;i++){
			a[i][0] = incoming[i].size();
		}
		long[][] mat = new long[n][n];
		for (int i=0;i<n;i++){
			for (int j=0;j<incoming[i].size();j++){
				mat[i][incoming[i].get(j)] = 1;
			}
		}
		long[][] ans = new long[n][1];
		ans = multiply(exp(k-1,mat,mod),a,mod);
		long res = 0;
		for (int i=0;i<n;i++){
			res += ans[i][0];
			res = res%mod;
		}
		System.out.println(res);
	}
	static long[][] multiply(long[][] a, long[][] b,long mod){
		// for (int i=0;i<a.length;i++){
		// 	for (int j=0;j<a[0].length;j++){
		// 		System.out.print(a[i][j]);
		// 	}
		// 	System.out.println();
		// }
		// for (int i=0;i<b.length;i++){
		// 	for (int j=0;j<b[0].length;j++){
		// 		System.out.print(b[i][j]);
		// 	}
		// 	System.out.println();
		// }
		long[][] ans = new long[a.length][b[0].length];
		for (int i=0;i<a.length;i++){
			for (int j=0;j<b[0].length;j++){
				long s=0;
				for (int k=0;k<a[0].length;k++){
					s += (a[i][k]*b[k][j])%mod;
					s = s%mod;
				}
				ans[i][j] = s%mod;
				// System.out.println(s);
			}
		}
		// for (int i=0;i<ans.length;i++){
		// 	for (int j=0;j<ans[0].length;j++){
		// 		System.out.print(ans[i][j]);
		// 	}
		// 	System.out.println();
		// }
		return ans;
	}
	static long[][] exp(long n, long[][] mat,long mod){
		if (n==1){
			return mat;
		}
		long[][] x = exp(n/2,mat,mod);
		if (n%2==1){
			return multiply(mat,multiply(x,x,mod),mod);
		}else{
			return multiply(x,x,mod);
		}
	}

}