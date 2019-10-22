raspivid -o - -t 99999 -w 640 -h 360 -fps 25 | cvlc stream:///dev/stdin --sout '#standard{access=http, mux=ts, dst=5001}' :demux=h264
