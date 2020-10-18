#include<bits/stdc++.h>
#define ll long long
#define pb push_back
using namespace std;
const int N = 1001;
int main(){
	ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

	ll i,j,k,n,r,t,a[N];

	cin>>t;
	while(t--){
		cin>>n;
		for(i=0;i<n;i++)
			cin>>a[i];
		ll f = 1;
		sort(a, a+n);
		for(i=1;i<n;i++){
			if(a[i]-a[i-1]>=2)
				f = 0;
		}
		if(f)
			cout<<"YES\n";
		else
			cout<<"NO\n";
	}

	return 0;
}