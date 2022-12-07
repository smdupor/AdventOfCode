#include <stdio.h>
#include <malloc.h>
#include <sys/stat.h>

int main(){

    // Obtain the file size to read
    struct stat *buf = (struct stat *) malloc(sizeof(struct stat));
    stat("input.txt",buf);
    const int bytes = buf->st_size;
    free(buf);

    // Get memory, read in data, close file
    FILE *fp = fopen("input.txt", "r");
    char *data = (char *) malloc(bytes);
    char *data_base = data;
    fread(data, 1, bytes, fp);
    fclose(fp);

    int i = 0;
    const int j=0;

    for( ; i< bytes - 4; i++){

            // If this block contains non unique char
            if (data[j] == data[j+1] ||
                data[j] == data[j+2] ||
                data[j] == data[j+3]  ||

                data[j+1] == data[j+2] ||
                data[j+1] == data[j+3] ||

                data[j+2] == data[j+3]
                ){
                    data++; // Advance the pointer into this string
                }
            else {
                // Otherwise, found, exit
                printf("The tail of the header is at %d\n",i+4);
                break;
            }
    }
    free(data_base);
    return 0;
}