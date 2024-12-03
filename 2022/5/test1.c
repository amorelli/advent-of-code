#include <stdio.h>
#include <string.h>

struct Books {
        char  title[100];
        char  author[100];
        char  subject[100];
    };  

int main()
{

    /* I like to separate the type definition from the object creation */
    struct potNumber aPot[3];
    /* with a C99 compiler you can use 'designated initializers' */
    struct potNumber bPot = {{[7] = 7, [3] = -12}, {[4] = "four", [6] = "six"}};

    for (i = 0; i < 20; i++) {
        aPot[0].array[i] = i;
    }

    // st_name is the name of the struct
    void print(T_THREAD *st, const char *st_name)
    {
        printf("Contents of structure %s are %lu, %d\n", st_name, st->thread_id, st->is_valid);
    }

    print()
    return 0;
}