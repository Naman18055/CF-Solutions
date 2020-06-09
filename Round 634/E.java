import java.util.*;
public class Main{
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int test = input.nextInt();
		while (test!=0){
			int n = input.nextInt();
			int[] arr = new int[n];
			for (int i=0;i<n;i++){
				arr[i] = input.nextInt();
			}
			if (n==1){
				System.out.println(1);
				test-=1;
				continue;
			}else if(n==2){
				if (arr[0]==arr[1]){
					System.out.println(2);
				}else{
					System.out.println(1);
				}
				test-=1;
				continue;
			}
			HashMap<Integer,HashMap<Integer,Integer>> map = new HashMap<>();
			int[][] counts = new int[200][n];
			int flag=0;
			for (int i=1;i<201;i++){
				int count=0;
				map.put(i,new HashMap<>());
				for (int j=0;j<n;j++){
					if (arr[j]==i){
						count+=1;
						(map.get(i)).put(count,j);
					}
					counts[i-1][j]=count;
					if (count>=2){
						flag=1;
					}
				}
			}
			if (flag==0){
				System.out.println(1);
				test-=1;
				continue;
			}
			int ans=0;
			for(int i=1;i<201;i++){
				for (int j=1;j<201;j++){
					for (int k=0;k<((map.get(i)).size())/2;k++){
						// System.out.println();
						int first = (map.get(i)).get(k+1);
						int second = (map.get(i)).get(counts[i-1][n-1]-k);
						int temp = 2*(k+1) + counts[j-1][second-1] - counts[j-1][first];
						if (temp>ans){
							ans=temp;
						}
					}
				}
			}
			System.out.println(ans);
			test-=1;
			// System.out.println(test);
		}
	}
}