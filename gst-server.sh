#!/bin/tcsh

set myip=192.168.1.8
set port=5001
set width=320
set height=240

gst-launch-1.0\
  v4l2src !\
  videoconvert !\
  video/x-raw,format=YUY2,width=${width},height=${height},framerate=30/1 !\
  jpegenc !\
  #xvimagesink !\
  tcpserversink host=${myip} port=${port} sync=false
