mtype = { nice, rude };

chan request = [0] of { mtype, chan };

active [2] proctype Server() {
    mtype msg;  chan ch;
    do :: request ? msg, ch -> ch ! msg
    od
}

active proctype ClientNice() {
    chan reply = [0] of { mtype };
    mtype msg;
    request ! nice, reply;  reply ? msg;
    assert(msg == nice);
}

active proctype ClientRude() {
    chan reply = [0] of { mtype };
    mtype msg;
    request ! rude, reply;  reply ? msg;
    assert(msg == rude);
}
