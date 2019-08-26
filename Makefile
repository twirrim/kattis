CFLAGS=-O2 -std=gnu11 -static -lm -mtune=native -flto -Wall
SRCS=$(wildcard c/*.c)

OBJS=$(SRCS:.c=)

all: $(OBJS)
