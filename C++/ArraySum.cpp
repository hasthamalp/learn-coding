#include <bits/stdc++.h>

using namespace std; 

int main(){
  int n;
  vector<int> nums;
  cout << "Enter the number of elements in the array: ";
  cin >> n;
  cout << endl;
  cout << "Enter the elements of the array separated by a space: ";
  for(int i = 1; i <= n; i++){
     int k;
     cin >> k;
     nums.push_back(k);
  }
  cout << endl;
  cout << "Sum of the array is: " << accumulate(nums.begin(), nums.end(), 0) << endl;
}
