# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 09:44:58 2013

@author: Artur_Herczeg
"""
from sqlalchemy import Column, Integer, String
import database as db


class Capability(db.Base):
    __tablename__ = 'capabilities'

    id = Column(Integer, primary_key=True)
    category = Column(String)
    subcategory = Column(String)
    level = Column(Integer)
    description = Column(String)

    def __repr__(self):
        return "<Capability(id={id}, category={category}, subcategory={subcat}, level={level}, desc={desc})>".format(id=self.id, category=self.category, subcat=self.subcategory, level=self.level, desc=self.description.encode('utf8')).decode("utf-8")
