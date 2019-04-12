#! /bin/sh

set -e

PIPE="/tmp/mplayer.pipe"

[ -p $PIPE ] || mkfifo "$PIPE"

mplayer -slave -idle -input file="$PIPE" -vo x11 -mf fps=10 -pausing 2 -fs
