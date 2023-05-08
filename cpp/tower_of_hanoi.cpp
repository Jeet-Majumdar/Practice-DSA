#include <iostream>
#include<string>

using namespace std;

void tower_of_hanoi(int n, char source, char destination, char intermediate){
    if( n >= 1){
       tower_of_hanoi(n-1, source, intermediate, destination);
       cout << n << " " << source << " " << destination << endl;
       tower_of_hanoi(n-1, intermediate, destination, source);
    }
}
int main(){
    int n = 2;
    char source = 'A';
    char intermediate = 'B';
    char destination = 'C';

    tower_of_hanoi(3, source, destination, intermediate);

    return 0;
}