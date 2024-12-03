#include <stdio.h>
#include <string.h>
#include <stdbool.h>

static bool unique(char* comp, int slength, int count) {
    for (int k = 0; k < slength - 1; k++ ) {
        for (int l = k + 1; l < slength; l++) {
            printf("compare %c to %c, count %d \n ", comp[k], comp[l], count);
            printf("-------------------: ");
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
    int i = 0;

    if (argv[1]) {
        slength = 14;
    }

    if (fp == NULL)
    {
        printf("Error: could not open file %s", filename);
        return 1;
    }

    while ((ch = fgetc(fp)) != EOF) {
        // check if array has been filled
        if (i >= slength) {
            printf("\n before shift: \n");
            for (int x = 0; x < slength; x++) {
                printf("%c ", comp[x]);
            }
            // i = 0;
            if (unique(comp, slength, count)) {
                goto end;
            }
            printf("before shift: \n");
            for (int x = 0; x < slength; x++) {
                printf("%c ", comp[x]);
            }
            // memmove(&comp[0], &comp[1], sizeof(comp) - sizeof(*comp));
            shift(comp, slength);
            comp[slength-1] = ch;
            printf("\nset last value to %c", ch);
            printf("\nafter shift: \n");
            for (int x = 0; x < slength; x++) {
                printf("%c ", comp[x]);
            }
        } else {
            comp[i] = ch;
            printf("\n ch is %c\n", ch);
            i++;
        }
        count++;
    }

    end:
    fclose(fp);
    printf("\n chars before duplicate: %d", count);
    printf("\n arguments: %s", argv[1]);
    printf("\n slength: %d", slength);
    return 0;
}