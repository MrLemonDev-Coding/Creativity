#include <iostream>
#include <string>

int main() {
    using namespace std;

    cout << "Enter a a number to count to: ";
    int e = 0;
    cin >> e;
    for(int i = 0; i <= e; i++) {
        cout << i << " ";
    }
    return 0;
}