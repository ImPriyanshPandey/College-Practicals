#include<iostream>

void insertionSort(int arr[],int size) {
    for(int i=1;i<size;++i)
{   int key = arr[i];
    int j=i-1;

    while(j>=0 && arr[j]>key) {
        arr[j+1]=arr[j];
        --j;
    }
    arr[j+1]=key;
}
}

void displayArray(int arr[],int size) {
    for(int i=0; i<size; ++i) {
        std::cout<<arr[i]<<"";
    }
    std::cout<<std::endl;
}

int main()
{
   int size;
   std::cout<<"Enter the size of the array:";
   std::cin>>size;

   int arr[size];
   std::cout<<"Enter the elements of the array: ";
   for(int i=0;i<size; ++i) {
    std::cin>>arr[i];
   }

   std::cout<<"Original Array: ";
   displayArray(arr,size);

   insertionSort(arr,size);

   std::cout<<"Sorted Array: ";
   displayArray(arr, size);
   
   return 0;
}