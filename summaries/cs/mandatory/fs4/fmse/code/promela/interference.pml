byte n = 0;

active proctype P() {
    n = 1;
    printf("Process P; n: %d\n", n)
}

active proctype Q() {
    n = 2;
    printf("Process Q; n: %d\n", n)
}
