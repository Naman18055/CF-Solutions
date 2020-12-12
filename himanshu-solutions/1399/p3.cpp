#include<bits/stdc++.h>
#define ll long long
#define pb push_back
using namespace std;
const int N = 1001;
int main(){
	ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

	ll i,j,k,n,r,t,a[N],x;
	ll ans;
	cin>>t;
	while(t--){
		cin>>n;
		multiset<ll> s;
		multiset<ll>::iterator itr;
		for(i=0;i<n;i++){
			cin>>a[i];
		}
		ans = 0;

		for(j=0;j<101;j++){
			s.clear();
			for(i=0;i<n;i++)
				s.insert(a[i]);
			r = 0;
			while(s.size()!=0){
				itr = s.begin();
				x = (*itr);			
				s.erase(itr);
				itr = s.find(j-x);
				if(itr!=s.end()){
					r++;
					s.erase(itr);
				}
			}
			ans = max(ans, r);
		}
		cout<<ans<<"\n";

	}


	return 0;
}