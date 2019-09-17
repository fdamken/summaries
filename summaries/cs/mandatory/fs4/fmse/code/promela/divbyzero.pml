int a, b, c;

active proctype P() {
    a = 1;  b = 1;  c = 1;
    if
        :: a != 0 -> c = b / a
        :: else   -> c = b
    fi
}

active proctype Q() {
    a = 0
}
