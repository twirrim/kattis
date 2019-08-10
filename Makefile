SRCS=$(wildcard c/*.c)

OBJS=$(SRCS:.c=)

all: $(OBJS)
