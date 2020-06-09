import java.util.Scanner;
public class Main{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		int w1=input.nextInt();
		int h1=input.nextInt();
		int w2=input.nextInt();
		int h2=input.nextInt();
		int w3=input.nextInt();
		int h3=input.nextInt();
		while (h1!=0){
			w1=h1+w1;
			if (h1==h2){
				w1=w1-w2;
				if (w1<0){
					w1=0;
				}
			}else if(h1==h3){
				w1=w1-w3;
				if (w1<0){
					w1=0;
				}
			}
			h1=h1-1;
		}
		System.out.println(w1);
	}
}