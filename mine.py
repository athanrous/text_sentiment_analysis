#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 	
#	mod_sentiment_analysis
#
#       Copyright 2013 Athanasios - Ilias Rousinopoulos <athanrous@gmail.com>,
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#      
#       Attribution
#       
#       Israel Herraiz <herraiz@gsyc.escet.urjc.es>
#	@organization: Libresoft Research Group, Universidad Rey Juan Carlos
#	@copyright: Universidad Rey Juan Carlos (Madrid, Spain)
#	@license: GNU GPL version 2 or any later version
#	@contact: libresoft-tools-devel@lists.morfeo-project.org 
#       
#
#	


import MySQLdb
import operator, time, string

class ExtractData :
    
    
    def connect_extract(self,query,filepath):
                 
        db = MySQLdb.connect("localhost"," "," "," " ) #Add your database credentials
        cursor = db.cursor()
        cursor.execute(query)
        output = cursor.fetchall() 
        results = ""
        data = ""
        input_file = open(filepath, "w")
        for record in output:
            for entry in record:
                data = data + "\n" + str(entry)
            data= data + "\n"
        results = results + data + "\n"
        input_file.writelines(results)
        input_file.close()
        db.close()
 
