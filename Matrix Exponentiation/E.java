import java.util.*;
import java.math.*;

public class Main{
	public static void main(String[] args) {
		long mod = 4294967296l;
		Scanner input = new Scanner(System.in);
		int k = input.nextInt();
		if (k==1){
			System.out.println(3);
			System.exit(0);
		}else if(k==0){
			System.out.println(1);
			System.exit(0);
		}
		long[][] a = new long[65][1];
		for (int i=0;i<65;i++){
			a[i][0] = 0;
		}
		a[10][0] = 1;
		a[17][0] = 1;
		a[0][0] = 1;
		a[64][0] = 1;
		long[][] mat = new long[65][65];
		for (int i1=0;i1<8;i1++){
			for (int i2=0;i2<8;i2++){
				for (int j1=0;j1<8;j1++){
					for (int j2=0;j2<8;j2++){
						if (reach(i1,j1,i2,j2)){
							mat[i1*8+j1][i2*8+j2] = 1;
						}
					}
				}
			}
		}
		mat[0][64] = 1;
		mat[64][64] = 1;
		long[][] ans = new long[65][1];
		ans = mult(exp(k-1,mat,mod),a,mod);
		long res = 0;
		for (int i=0;i<64;i++){
			res += ans[i][0];
			res = res%mod;
		}
		System.out.println(res%mod);
	}
	static long[][] mult(long[][] a, long[][] b,long mod){
		long[][] ans = new long[a.length][b[0].length];
		for (int i=0;i<a.length;i++){
			for (int j=0;j<b[0].length;j++){
				BigInteger s= BigInteger.ZERO;
				for (int k=0;k<a[0].length;k++){
					s = s.add(((BigInteger.valueOf(a[i][k])).multiply(BigInteger.valueOf(b[k][j]))).mod(BigInteger.valueOf(mod)));
					s = s.mod(BigInteger.valueOf(mod));
				}
				ans[i][j] = s.longValue();
				// System.out.println(s);
			}
		}
		return ans;
	}
	static long[][] exp(long n, long[][] mat,long mod){
		if (n==1){
			return mat;
		}
		long[][] x = exp(n/2,mat,mod);
		if (n%2==1){
			return mult(mat,mult(x,x,mod),mod);
		}else{
			return mult(x,x,mod);
		}
	}
	static boolean reach(int i1,int i2,int i3,int i4){
		if ((i1==i3) && (i2==i4)){
			return false;
		}
		if (((i1-i3)==2 || (i1-i3)==-2) && ((i2-i4)==1 || (i2-i4)==-1)){
			return true;
		}
		if (((i1-i3)==1 || (i1-i3)==-1) && ((i2-i4)==2 || (i2-i4)==-2)){
			return true;
		}
		return false;
	}
}