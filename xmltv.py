import gzip
import shutil
import requests
import time
import os
from bs4 import BeautifulSoup
from datetime import datetime
from pymongo import MongoClient
from config import XML_URL, DB_URL, DB_NAME, COLLECTION_NAME
from schemas import Channel, Program

class TVProgram:
    def __init__(self):
        self._zip_file = XML_URL.split("/")[-1]
        self._time_format = "%Y%m%d%H%M%S %z"
        self._db = MongoClient(DB_URL).get_database(DB_NAME).get_collection(COLLECTION_NAME)
        self.__parser = None
        self._tv = None
      
    def install_xml(self):
        req = requests.get(XML_URL)
        with open(self._zip_file, "wb") as f:
          f.write(req.content)
        
    def load_xml(self): 
        with gzip.open(self._zip_file, 'rb') as f:
          xml = f.read()
        return xml
      
    def load_parser(self, xml):
        self.__parser = BeautifulSoup(xml, "xml")
        self._tv = self.__parser.find("tv")

    def load_data(self):
        channels = {}
        for channel in self._tv.findAll("channel"):
          tv_channel = Channel(
            id=channel.attrs.get("id"),
            name=channel.find("display-name").text,
            icon=channel.find("icon").attrs.get("src")
          )
          channels= {**channels, **{channel.attrs.get("id"): tv_channel}}   
        for program in self._tv.findAll("programme"):
          ch_program = Program(
            channel=program.attrs.get("channel"), 
            title=program.find("title").text, 
            description=program.find("desc").text if program.find("desc") is not None else None, 
            category=program.find("category").text if program.find("category") is not None else None,
            start_time=datetime.strptime(program.attrs.get("start"), time_format),
            stop_time=datetime.strptime(program.attrs.get("stop"), time_format)
          )
          channels[program.attrs.get("channel")].programs.append(ch_program)
        return list(channels.values())
    
    def upload_to_db(self, channels):
        self._db.insert_many(channel.dict() for channel in channels)