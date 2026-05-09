// ================================
// Author: Pritam
// ================================

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
//#include <bits/stdc++.h>
using namespace std;

// ---------- Macros & Typedefs ----------
#define ll long long
#define pb push_back
#define all(v) v.begin(), v.end()
#define nl '\n'

// ---------- Solve Function ----------

void solve() {
    int n;
    cin >> n;
    vector<ll> nums(n);
    for (ll i = 0; i < n; i++) {
        cin >> nums[i];
    }

    int pc = 0;
    int nc = 0;
    for (int i=0; i<n; i++) {
        if (nums[i] == -1) nc += 1;
        else pc += 1;
    }

    int ans = 0;
    while (nc > pc || nc % 2 == 1) {
        if (nc == 0) break;
        ans ++;
        pc ++;
        nc --;
    }

    cout << ans << nl;
}


// ---------- Main ----------
int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t = 1;
    cin >> t;

    while (t--) {
        solve();
    }

    return 0;
}