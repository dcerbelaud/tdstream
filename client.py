#!/usr/bin/python
# -*-coding:utf-8 -*

import pycurl,yaml,json
import sys, datetime, time
from functions import *
from config import *
from math import *
import csv


"""
Functions below are used to decode json.loads to utf-8
"""

def _decode_list(lst):
    newlist = []
    for i in lst:
        if isinstance(i, unicode):
            i = i.encode('utf-8')
        elif isinstance(i, list):
            i = _decode_list(i)
        newlist.append(i)
    return newlist

def _decode_dict(dct):
    newdict = {}
    for k, v in dct.iteritems():
        if isinstance(k, unicode):
            k = k.encode('utf-8')
        if isinstance(v, unicode):
             v = v.encode('utf-8')
        elif isinstance(v, list):
            v = _decode_list(v)
        newdict[k] = v
    return newdict


class Client:  
    def __init__(self):  
        self.buffer = ""  
        self.conn = pycurl.Curl()
        self.attempts = 0
    
    def connect(self, url):
        print("Connecting to url: {0}.".format(url))
        self.conn.setopt(pycurl.URL, url)  
        self.conn.setopt(pycurl.WRITEFUNCTION, self.on_receive)
        #self.conn.setopt(pycurl.TIMEOUT,timeout)
        try:
            self.conn.perform()
        except pycurl.error:
            self.attempts+=1
            t = datetime.datetime.now().strftime("%Y/%m/%d - %T")
            append_to_file("[{0}] Error {1} - {2}\n".format(t,sys.exc_info()[0],sys.exc_info()[1]),errlog_file)
            self.reconnect(url)
    
    def on_receive(self, data):  
        #print("Receiving....\n")
        self.attempts = 0
        self.buffer += data  
        if data.endswith("\r\n") and self.buffer.strip(): 
            content = json.loads(self.buffer,object_hook=_decode_dict)
            self.buffer = ""
            append_to_csv([content["loc"][0],content["loc"][1],content["date"],content["thumb"],content["user"]["twitter"],content["qidx"]["tags"]],data_file)

    def reconnect(self,url):
        time.sleep(min(2^(self.attempts),MAX_SLEEP))
        print("Reconnecting")
        self.connect(url)
