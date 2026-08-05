#include<iostream>
using namespace std;
int main()
{
    int m, n, p, q, i, j, A[5][5], B[5][5], C[5][5];
    cout<<"Enter rows and column of first matrix: ";
    cin>>m>>n;
    cout<<"Enter rows and column of second matrix: ";
    cin>>p>>q;
    if((m!=p)&&(n!=q))
    {
        cout<<"Matrices can't be added!";
        exit(0);
    }
    cout<<"Enter elements of first matrix: ";
    for(i=0;i<m;i++)
        for(j=0;j<n;j++)
            cin>>A[i][j];
    cout<<"Enter elements of second matrix: ";
    for(i=0;i<p;i++)
        for(j=0;j<q;j++)
            cin>>B[i][j];

    for(i=0;i<m;i++)
        for(j=0;j<n;j++)
            C[i][j]=A[i][j]+B[i][j];
    cout<<"Sum of matrices\n";
    for(i=0;i<m;i++)
    {    for(j=0;j<n;j++)
            cout<<C[i][j]<<"";
        cout<<"\n";
    }
    return 0;
}