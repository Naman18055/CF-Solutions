#include<bits/stdc++.h>
#define ll long long
#define pb push_back
using namespace std;
const int N = 1001;
int main(){
	ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

	ll i,j,k,n,r,t,p,r1,r2;
	string s;
	ll maxx;
	cin>>t;
	while(t--){
		cin>>n;
		cin>>s;
		maxx = 0;
		vector<ll> v;
		r1 = 0;
		r2 = 0;
		r = 0;
		set<ll> s1,s2;
		set<ll>::iterator itr;
		r = 0;
		for(i=0;i<n;i++){
			p = s[i]-'0';
			if(p==0){
				if(s1.size()==0){
					r++;
					s2.insert(r);
					v.pb(r);
				}
				else{
					itr = s1.begin();
					s2.insert(*itr);
					v.pb(*itr);
					s1.erase(itr);
				}
			}
			else{
				if(s2.size()==0){
					r++;
					s1.insert(r);
					v.pb(r);
				}
				else{
					itr = s2.begin();
					s1.insert(*itr);
					v.pb(*itr);
					s2.erase(itr);
				}
			}

		}
		// ans = max(ans)
		cout<<r<<"\n";
		for(i=0;i<n;i++)
			cout<<v[i]<<" ";
		cout<<"\n";
	}


	return 0;
}