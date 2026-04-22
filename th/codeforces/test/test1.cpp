#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

// Custom comparator function
bool compareStrings(const string& a, const string& b) {
    // 1. If lengths are different, sort by length (shorter first)
    if (a.length() != b.length()) {
        return a.length() < b.length();
    }
    // 2. If lengths are equal, sort lexicographically (ASCII order)
    return a < b;
}

int main() {
    // Fast I/O to prevent Time Limit Exceeded (TLE)
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<string> strings(n);
    for (int i = 0; i < n; ++i) {
        cin >> strings[i];
    }

    // Sort using our custom logic
    sort(strings.begin(), strings.end(), compareStrings);

    // Print the sorted strings
    for (int i = 0; i < n; ++i) {
        cout << strings[i] << "\n";
    }

    return 0;
}