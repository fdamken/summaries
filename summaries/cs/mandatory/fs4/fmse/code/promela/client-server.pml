chan request = [0] of { byte };

active proctype Server() {
    byte num;
    do :: request ? num ->
          printf("Serving client %d\n", num)
    od
}

active proctype Client0() {
    request ! 0
}

active proctype Client1() {
    request ! 1
}
