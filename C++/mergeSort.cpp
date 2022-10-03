#include "bits/stdc++.h"
using namespace std;

void display(int a[], int n)
{
    for (int i = 0; i < n; i++)
        cout << a[i] << " ";
    cout << "\n";
}

void merge_sort(int[], int, int, int);
void msort(int a[], int l, int r)
{
    int mid;
    if (l < r)
    {
        mid = (l + r) / 2;
        msort(a, l, mid);
        msort(a, mid + 1, r);
        merge_sort(a, l, r, mid);
    }
}

void merge_sort(int a[], int l, int r, int mid)
{
    int n1 = mid - l + 1;
    int n2 = r - mid;

    int L[n1], M[n2];

    for (int i = 0; i < n1; i++)
        L[i] = a[l + i];
    for (int j = 0; j < n2; j++)
        M[j] = a[mid + 1 + j];

    int i, j, k;
    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2)
    {
        if (L[i] <= M[j])
        {
            a[k] = L[i];
            i++;
        }
        else
        {
            a[k] = M[j];
            j++;
        }
        k++;
    }

    while (i < n1)
    {
        a[k] = L[i];
        i++;
        k++;
    }

    while (j < n2)
    {
        a[k] = M[j];
        j++;
        k++;
    }
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    int a[n];
    for (auto &it : a)
    {
        cin >> it;
    }
    msort(a, 0, n - 1);
    display(a, n);
}
