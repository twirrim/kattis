# kattis
My answers to Kattis problems.  Mix of Python, Rust, and C.



# Random notes

Python:
    Dreamer - I'm not entirely happy with the python speed, but obvious tricks aren't speeding it up.  I'm assuming there are optimisations I'm missing.

Rust:
    Dreamer - Profiling showed hashset as responsible for about half the runtime.  "Polluting" the permutations generator with application logic reduced runtime on the kattis servers to 0.05s from 0.25s.  Alternatively I guess I could move the uniqueness outside of the permutations generator.  If I wasn't restricted to stdlib there are a number of faster hashing crates out there.
