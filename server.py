# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 14:43:36 2013

@author: Artur_Herczeg
"""

from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
import psycopg2
import urlparse


def initDB():
    initdata = [(1, "Computer Science", "Data structures", 0, "Doesn’t know the difference between Array and LinkedList"),
                (2, "Computer Science", "Data structures", 1, "Able to explain and use Arrays, LinkedLists, Dictionaries etc in practical programming tasks"),
                (3, "Computer Science", "Data structures", 2, "Knows space and time tradeoffs of the basic data structures, Arrays vs LinkedLists, Able to explain how hashtables can be implemented and can handle collisions, Priority queues and ways to implement them etc."),
                (4, "Computer Science", "Data structures", 3, "Knowledge of advanced data structures like B-trees, binomial and fibonacci heaps, AVL/Red Black trees, Splay Trees, Skip Lists, tries etc."),
                
                (5, "Computer Science", "Algorithms", 0, "Unable to find the average of numbers in an array (It’s hard to believe but I’ve interviewed such candidates)"),
                (6, "Computer Science", "Algorithms", 1, "Basic sorting, searching and data structure traversal and retrieval algorithms"),
                (7, "Computer Science", "Algorithms", 2, "Tree, Graph, simple greedy and divide and conquer algorithms, is able to understand the relevance of the levels of this matrix."),
                (8, "Computer Science", "Algorithms", 3, "Able to recognize and code dynamic programming solutions, good knowledge of graph algorithms, good knowledge of numerical computation algorithms, able to identify NP problems etc."),
                
                (9, "Computer Science", "systems programming", 0, "Doesn't know what a compiler, linker or interpreter is"),
                (10, "Computer Science", "systems programming", 1, "Basic understanding of compilers, linker and interpreters. Understands what assembly code is and how things work at the hardware level. Some knowledge of virtual memory and paging."),
                (11, "Computer Science", "systems programming", 2, "Understands kernel mode vs. user mode, multi-threading, synchronization primitives and how they’re implemented, able to read assembly code. Understands how networks work, understanding of network protocols and socket level programming."),
                (12, "Computer Science", "systems programming", 3, "Understands the entire programming stack, hardware (CPU + Memory + Cache + Interrupts + microcode), binary code, assembly, static and dynamic linking, compilation, interpretation, JIT compilation, garbage collection, heap, stack, memory addressing…"),

                (13, "Software Engineering", "source code version control", 0, "Folder backups by date"),
                (14, "Software Engineering", "source code version control", 1, "VSS and beginning CVS/SVN user"),
                (15, "Software Engineering", "source code version control", 2, "Proficient in using CVS and SVN features. Knows how to branch and merge, use patches setup repository properties etc."),
                (16, "Software Engineering", "source code version control", 3, "Knowledge of distributed VCS systems. Has tried out Bzr/Mercurial/Darcs/Git"),

                (17, "Software Engineering", "build automation", 0, "Only knows how to build from IDE"),
                (18, "Software Engineering", "build automation", 1, "Knows how to build the system from the command line"),
                (19, "Software Engineering", "build automation", 2, "Can setup a script to build the basic system"),
                (20, "Software Engineering", "build automation", 3, "Can setup a script to build the system and also documentation, installers, generate release notes and tag the code in source control"),

                (21, "Software Engineering", "automated testing", 0, "Thinks that all testing is the job of the tester"),
                (22, "Software Engineering", "automated testing", 1, "Has written automated unit tests and comes up with good unit test cases for the code that is being written"),
                (23, "Software Engineering", "automated testing", 2, "Has written code in TDD manner"),
                (24, "Software Engineering", "automated testing", 3, "Understands and is able to setup automated functional, load/performance and UI tests	"),]
    
    session = Session()
    for d in initdata:
        id, category, subcategory, level, desc = d
        capability = Capability(id=id, category=category, subcategory=subcategory, level=level, description=desc)
        res = session.query(Capability).filter(Capability.id==id).count()
        if res == 0:
            session.add(capability)
        
    
    session.commit()
    
def createDBSession():
    DATABASE_ENVVAR = "HEROKU_POSTGRESQL_RED_URL"    
    
    if DATABASE_ENVVAR in os.environ:
        urlparse.uses_netloc.append("postgres")
        url = urlparse.urlparse(os.environ[DATABASE_ENVVAR])   
        print url
        engine = create_engine(url)
    else:
        engine = create_engine('postgresql://postgres:pass123@localhost:5432/ProgCapMat',
                           echo=True)
    print engine
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session
    
def connectDB():
    return Session()


Base = declarative_base()

class Capability(Base):
    __tablename__ = 'capabilities'

    id = Column(Integer, primary_key=True)
    category = Column(String)
    subcategory = Column(String)
    level = Column(Integer)
    description = Column(String)

    def __repr__(self):
        return "<Capability(id={id}, category={category}, subcategory={subcat}, level={level}, desc={desc})>".format(id=self.id, category=self.category, subcat=self.subcategory, level=self.level, desc=self.description.encode('utf8')).decode("utf-8")




app = Flask(__name__)

Session = createDBSession()
initDB()



@app.route("/")
def index():
    session = Session()
    
    allcap = session.query(Capability)
    categories = session.query(Capability.category).distinct()
    
    
    processed = list()  
    for cat in categories:
        subcats = session.query(Capability.subcategory).distinct()
        print cat
        print [x for x in subcats]
        
        for sub in subcats:
            items = session.query(Capability.level, Capability.description).filter(Capability.category == cat, Capability.subcategory == sub)
            print [x for x in items]
            processed.append((cat, sub, items))
        
        
     
    
    
    return render_template('index.html', categories = categories, items = allcap)

if __name__ == "__main__":   
    
    app.debug = True
    app.run()
