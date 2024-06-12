#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

int main() {
    int fd = open("/flag.txt", O_RDONLY);
    if (fd == -1) {
        perror("Error opening flag.txt");
        return 1;
    }
    char buffer[1025];
    ssize_t bytes_read = read(fd, buffer, 1024);
    if (bytes_read == -1) {
        perror("Error reading from flag.txt");
        close(fd);
        return 1;
    }
    buffer[bytes_read] = '\0';
    printf("%s\n", buffer);
    close(fd);
    return 0;
}
