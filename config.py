#!/usr/bin/python
# -*-coding:utf-8 -*

""" Config file for connection to the teleportd api - streaming version"""

base_url = "http://v1.api.teleportd.com"
apikey = "ac31508573402ae15367c87d66372e21"
port = "8080"
stream = "yes"
loc = "[48.857,2.352,1,1]"
meta = "yes"
window = "1000"

teleportd_url ="{0}:{1}/search?apikey={2}&stream={3}&loc={4}&meta={5}".format(base_url,port,apikey,stream,loc,meta)

timeout = 60
MAX_SLEEP = 600

data_file = "output_stream"
errlog_file = "err.log"
