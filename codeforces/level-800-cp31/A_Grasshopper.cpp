// ================================
// Author: Pritam
// ================================

// #include <bits/stdc++.h>
#include <iostream>
#include <vector>
using namespace std;

// ---------- Macros & Typedefs ----------
#define ll long long
#define pb push_back
#define all(v) v.begin(), v.end()
#define nl '\n'

// ---------- Solve Function ----------

void solve() {
    int x, k;
    cin >> x >> k;

    if (x%k != 0) {
        cout << 1 << nl;
        cout << x << nl;
    } else {
        cout << 2 << nl;
        cout << x-1 << " " << 1 << nl;
    }
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