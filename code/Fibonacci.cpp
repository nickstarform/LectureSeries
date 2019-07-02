#include <iostream>
#include <chrono> 

using namespace std::chrono; 
using namespace std;
 
main()
{
   int n = 10, c, first, second, next;
   int avg = 0, iter;
   cout << "The " << n << " term of Fibonacci series is :- " << endl;

   for (iter = 0 ; iter < 10000 ; iter++)
   {
        auto start = high_resolution_clock::now();
        first = 0, second = 1, next = 0;
        for ( c = 0 ; c < n ; c++ )
        {
            if ( c <= 1 )
                next = c;
            else
            {
                next = first + second;
                first = second;
                second = next;
            }
        }
        auto stop = high_resolution_clock::now();
        auto duration = duration_cast<nanoseconds>(stop - start);
        avg = avg + duration.count();
    }
    cout << next << endl;
    avg = avg / 10000.;
    cout << "Completed in " << avg << " nanoseconds averaged over 10000 trials." << endl;
   return 0;
}
