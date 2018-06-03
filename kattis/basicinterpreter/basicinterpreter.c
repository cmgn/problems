#include <stdio.h>
#include <string.h>

int variables[26];

typedef enum {
    STRING,
    NUMBER,
    IDENTIFIER,
    OPERATOR,
} token_type;

typedef struct {
    token_type type;
    int length;
    union {
        const char *string;
        const char *identifier;
        const char *operator;
        int number;
    } value;
} token;