#include <stdio.h>
#include <string.h>
#include <stdbool.h>

static bool unique(char* comp, int slength, int count) {
    for (int k = 0; k < slength - 1; k++ ) {
        for (int l = k + 1; l < slength; l++) {
            if (comp[k] == comp[l]) {
                return false;
            }
        }
    }
    return true;
}

static int shift(char* comp, int slength) {
    for (int i = 0; i < slength - 1; i++) {
        comp[i] = comp[i+1];
    }
    return 0;
}

int main(int argc, char *argv[])
{
    char *filename = "input.txt";
    FILE *fp = fopen(filename, "r");
    int slength = 4;
    char comp[slength];
    char ch;
    int count = 0;

    if (argv[1]) {
        slength = 14;
    }

    if (fp == NULL)
    {
        return 1;
    }

    while ((ch = fgetc(fp)) != EOF) {
        // check if array has been filled
        if (count >= slength) {
            // naive compare
            if (unique(comp, slength, count)) {
                goto end;
            }
            // shift array values left
            shift(comp, slength);
            comp[slength-1] = ch;
        } else {
            comp[count] = ch;
        }
        count++;
    }

    end:
    fclose(fp);
    printf("start-of-packet marker: %d\n", count);
    return 0;
}