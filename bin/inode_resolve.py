#!/usr/bin/env python

from cirosantilli import files
import os
import json

class Item:

    def __init__(self,relpath,inode):
        self.relpath = relpath
        self.inode = inode
        
    def serialize(self):
        return relpath + '\n' + inode
    
    def deserialize(self, serialized):
        splited = serialized.split('\n')
        relpath = splited[0]
        inode = splited[1]
        return File(relpath,inode)
    
class DB:
    
    DB_NAME = '.iresolve'
    
    def __init__(self, items=[]):
        self.items = items
        
    def add_item(self, item):
        self.items.append(item)
        
    def add_items(self, items):
        self.items.extend(items)

    @staticmethod
    def update(dbdir):
        """
        Creates the relative path/inode database in given directory.
        
        If it already exists, erases the old one, and creates the new one.
        """
        
        # create database in memory
        dbpath = os.path.join(dbdir,DBNAME)
        if os.path.exists(dbpath):
            db = DB.deserialize(files.read(dbpath))
        else:
            db = db()
        
        inodes = db.get_inodes()
        relpaths = db.get_relpaths()
        for relpath in relpaths:
            path = os.path.join(dbdir,relpath)
            if( not os.path.exists(path) ):
                db.update_inode_path(inode,path)
        
        # get files under
        exists, file_paths = files.find(r'./',
            type='f',
            fulltree=True,
            
        
        for path in file_paths:
            db.add_item(paths.append(path),files.inode(path))
        
        files.write(dbpath,db.serialize())
    
    def update_inode_path(self,inode,path):
    
    def clear(self):
        self.items = []
        
    def serialize(self,dbpath):
        
        json_items = []
        for item in self.items:
            json_items.append(item.serialize())
        
        json_db = json.dumps(json_items)
        return json_db
    
    @staticmethod
    def deserialize(serialized):
        
        items = []
        json_items = json.loads(serialized)
        for json_item in json_items:
            items.append(object)
    
        splited = serialized.split(SPLIT_SEQ)
        for item in self.items: 
            output = output + item.serialize + '\n'
        return db

if __name__ == '__main__':
    
    DB.update(os.getcwd())




