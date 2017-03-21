#!/bin/bash

[ -z "$1" ] && exit 1
fname="$1"
name=$(basename $1 | sed 's/\.ser/.txt/')
d1="b64-data/$name"
function mac {
    # do this on mac
    base64 "$fname" -b 0 > "$d1"
}

function linux {
    # do this on Linux
    base64 "$fname" -w 0 > "$d1" 2>/dev/null
}

linux || mac
python urlencode.py "$d1"
