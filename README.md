# kattis
My answers to Kattis problems.  Mix of Python and Rust



# Random notes

Python:
    Dreamer - I'm not entirely happy with the python speed, but obvious tricks aren't speeding it up.  I'm assuming there are optimisations I'm missing.

Rust:
    Dreamer - 25 seconds?  I was hoping for better.  Profiling the code puts hashset and the hashing function as responsible for 52% of the runtime.  If I pollute the permutations code with dreamer specific logic (e.g. check to see if first digit is >= 2 etc.), I can probably trim that down a bit by cutting out hashing operations.
