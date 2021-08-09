#include <iostream>
using namespace std;

long powers[200001];
long mod = 1000000007;

int pow(long long x, unsigned int y, int p)
{
	int res = 1;     // Initialize result
 
	x = x % p; // Update x if it is more than or
				// equal to p
  
	if (x == 0) return 0; // In case x is divisible by p;
 
	while (y > 0)
	{
		// If y is odd, multiply x with result
		if (y & 1)
			res = (res*x) % p;
 
		// y must be even now
		y = y>>1; // y = y/2
		x = (x*x) % p;
	}
	return res;
}

int main(){
	long nt, n, k;
	cin>>nt;
	powers[0] = 1;
	for(int i=1;i++;i<200001){
		powers[i] = (powers[i-1]*2)%mod;
	}
	while(nt--){
		cin>>n>>k;
		if (n%2==1){
			long ans = pow(2, n*k, mod);
			for (int i=0;i<k;i++){
				ans -= ((((pow(powers[n-1]+1, i, mod)) * (powers[n-1]-1))%mod) * pow(2, n*(k-i-1), mod))%mod;
				ans = ans%mod;
			}
			cout<<ans<<'\n';
		}else{
			long ans = pow(2, n*k, mod);
			for (int i=0;i<k;i++){
				ans -= ((((pow(powers[n-1]-1, i, mod)) * (powers[n-1]))%mod) * pow(2, n*(k-i-1), mod))%mod;
				ans = ans%mod;
			}
			cout<<ans<<'\n';
		}
	}
}