#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

class Person
{

    public:

        Person(int count) : _next(NULL), _prev(NULL) { _count = count; }
        int shout(int shout, int nth)
        {
            if (shout < nth) return (shout + 1);
            _prev->_next = _next;


            _next->_prev = _prev;
            return 1;
        }
        int count() { return _count; }
        Person* next() { return _next; }
        void next(Person* person) { this->_next = person ; }
        Person* prev() { return _prev; }
        void prev(Person* person) { this->_prev = person; }
    private:
        int _count;
        Person* _next;
        Person* _prev;
};

class Chain
{
    public:
        Chain(int size) : _first(NULL)
        {
            Person* current = NULL;
            Person* last = NULL;
            for(int i = 0 ; i < size ; i++)
            {
                current = new Person(i);
                if (_first == NULL) _first = current;
                if (last != NULL)
                {
                    last->next(current);
                    current->prev(last);
                }
                last = current;
            }
            _first->prev(last);
            last->next(_first);
        }
        Person* kill(int nth)
        {
            Person* current = _first;
            int shout = 1;
            while(current->next() != current)



            {
                Person* tmp = current;
                shout = current->shout(shout,nth);
                current = current->next();
                if (shout == 1)
                {
                    delete tmp;
                }
            }
            _first = current;
            return current;
        }
        Person* first() { return _first; }
    private:
        Person* _first;
};

int main(int argc, char** argv)
{
    int ITER = 1000000;
    Chain* chain;
    struct timeval start, end;
    gettimeofday(&start,NULL);
    for(int i = 0 ; i < ITER ; i++)
    {
        chain = new Chain(40);
        chain->kill(3);


        delete chain;
    }
    gettimeofday(&end,NULL);
    fprintf(stdout,"Time per iteration = %d microseconds \n", (((end.tv_sec - start.tv_sec) * 1000000) + (end.tv_usec - start.tv_usec)) / ITER);
    //fprintf(stdout,"Last man standing is %dnr", (chain->first()->count() + 1));
    return 0;
}
