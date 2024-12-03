#include <stdio.h>

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
        // pass char to comparison array
        comp[i] = ch;

        // check if array has been filled
        if (i >= slength-1) {
            i = 0;
            int duplicates = 0;

            // compare elements of the array to each other
            for (int k = 0; k < slength - 1; k++ ) {
                for (int l = k + 1; l < slength; l++) {
                    printf("compare %c to %c, count %d \n ", comp[k], comp[l], count);
                    printf("-------------------: ");
                    if (comp[k] == comp[l]) {
                        printf("%c at position %d is the same as %c at position %d \n", comp[k], k, comp[l], l);
                        duplicates++;
                    }
                    //  else {
                    //     printf("no duplicates found at count %d \n", count-1);
                    // }
                }
                //
                if (k == slength - 2 && duplicates == 0) {
                    printf("\n---------------------------");
                    printf("\n no duplicate found, count = %d ", count-1);
                    printf("\n---------------------------");
                    goto end;
                }
            }
        } else {
            i++;
        }
        count++;
    }

    end:
    fclose(fp);
    printf("\n chars before duplicate: %d", count-1);
    printf("\n arguments: %s", argv[1]);
    printf("\n slength: %d", slength);
    return 0;
}