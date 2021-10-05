#include <iostream>
using namespace std;

int BinarySearch(int arr[], int size, int target) {
	int start = 0;
	int end = size - 1;
	while(start<=end) {
		int mid = start + (end-start)/2;
		if(arr[mid] == target)
			return mid;
		else if(arr[mid]<target)
			start = mid+1;
		else
			end = mid-1;
	}
	return -1;
}

int main() {
	int size;
	cin>>size;
	int arr[size];
	for(int i=0; i<size; i++)
		cin>>arr[i];
	int target;
	cin>>target;
	cout<<BinarySearch(arr,size,target)<<endl;
}
