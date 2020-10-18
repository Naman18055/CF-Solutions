#include<bits/stdc++.h>
#define ll long long
#define pb push_back
using namespace std;
const int N = 1001;
int main(){
	ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

	ll i,j,k,n,r,t,a[N],b[N];
	ll minn1,minn2,ans;
	cin>>t;
	while(t--){
		cin>>n;
		minn1 = minn2 = LLONG_MAX;
		for(i=0;i<n;i++){
			cin>>a[i];
			minn1 = min(minn1, a[i]);
		}
		for(i=0;i<n;i++){
			cin>>b[i];
			minn2 = min(minn2, b[i]);
		}
		ans = 0;
		for(i=0;i<n;i++){
			ans += max(a[i]-minn1, b[i]-minn2);
		}
		cout<<ans<<"\n";
	}


	return 0;
}