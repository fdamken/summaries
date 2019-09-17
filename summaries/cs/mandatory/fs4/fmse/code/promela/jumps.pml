#define N 10

active proctype P() {
    int sum = 0;
    byte i = 1;
    do
        :: i > N -> goto exitloop
        :: else  -> sum = sum + i; i++
    od
    exitloop:
    printf("End of loop.\n")
}
