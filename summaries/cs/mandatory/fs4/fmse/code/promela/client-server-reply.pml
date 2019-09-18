mtype = { nice, rude };

chan request = [0] of { mtype };
chan reply   = [0] of { mtype };

active [2] proctype Server() {
    mtype msg;
    do :: request ? msg -> reply ! msg
    od
}

active proctype ClientNice() {
    mtype msg;
    request ! nice;  reply ? msg;
    assert(msg == nice);
}

active proctype ClientRude() {
    mtype msg;
    request ! rude;  reply ? msg;
    assert(msg == rude);
}
