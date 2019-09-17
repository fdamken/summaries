active [2] proctype P() {
    printf("Process P%d, statement 1\n", _pid);
    printf("Process P%d, statement 2\n", _pid)
}

active [2] proctype Q() {
    printf("Process Q%d, statement 1\n", _pid);
    printf("Process Q%d, statement 2\n", _pid)
}
