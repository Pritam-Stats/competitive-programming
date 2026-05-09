// ================================
// Author: Pritam
// ================================
// Link: https://codeforces.com/problemset/problem/1831/A


#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
// #include <bits/stdc++.h>
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
    vector <int> a(n);
    for (int i=0; i <n; i++) cin >> a[i];

    for (int i=0; i<n; i++)
    {
        cout << n-a[i]+1 << " ";
    }
    cout << nl;
    return;
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