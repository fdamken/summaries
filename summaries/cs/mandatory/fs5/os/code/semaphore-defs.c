// Number of slots in the buffer.
#define N 100;

// The special semaphore int.
typedef int semaphore;

// Controls access to the critical section.
semaphore mutex = 1;
// Counts empty buffer slots preventing a buffer underflow.
semaphore empty = N;
// Counts full buffer slots preventing a buffer overflow.
semaphore full = 0;
