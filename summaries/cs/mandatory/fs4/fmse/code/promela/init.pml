proctype P() {
    printf("In process P%d\n", _pid)
}

proctype Q() {
    printf("In process Q%d\n", _pid)
}

init {
    run P();
    run P();
    run Q()
}
