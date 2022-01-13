#include <iostream>

using namespace std;

void shellsort(int lst[], int len)
{
    for (int slot = len/2; slot > 0; slot /= 2)
    {
        for (int x = slot; x < len; x += 1)
        {
            int plhdr = lst[x];
            
            int y;
            
            for(y = x; y >= slot && lst[y - slot] > plhdr; y -= slot)
                lst[y] = lst[y - slot];
                
            
            lst[y] = plhdr;
            
        }   
    }
    return;
}

void printList(int lst[], int len)
{
    for (int x = 0; x < len; x++)
        cout << lst[x] << " ";
}

int main()
{
    int lst[] = {45, 235, 173, 93, 310, 19, 101}, x;
    
    int len = sizeof(lst)/sizeof(lst[0]);
    
    cout << "Pre-Sort: ";
    printList(lst, len);
    
    shellsort(lst, len);
    
    cout << "\nPost-Sort: ";
    printList(lst, len);

    return 0;
}
