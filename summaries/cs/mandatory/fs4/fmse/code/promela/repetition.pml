active proctype P() {
    int a = 15, b = 20;
    do
        :: a > b  -> a = a - b
        :: b > a  -> b = b - a
        :: a == b -> break
    od
}
