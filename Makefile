CFLAGS=-O2 -std=gnu11 -static -lm -mtune=native
SRCS=$(wildcard c/*.c)

OBJS=$(SRCS:.c=)

all: $(OBJS)
