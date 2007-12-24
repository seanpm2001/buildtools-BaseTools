## @file
# This file is used to create/update/query/erase table for pcds
#
# Copyright (c) 2007, Intel Corporation
# All rights reserved. This program and the accompanying materials
# are licensed and made available under the terms and conditions of the BSD License
# which accompanies this distribution.  The full text of the license may be found at
# http://opensource.org/licenses/bsd-license.php
#
# THE PROGRAM IS DISTRIBUTED UNDER THE BSD LICENSE ON AN "AS IS" BASIS,
# WITHOUT WARRANTIES OR REPRESENTATIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED.
#

##
# Import Modules
#
import Common.EdkLogger as EdkLogger

## TablePcd
#
# This class defined a table used for pcds
# 
# @param object:       Inherited from object class
#
#
class TablePcd(object):
    def __init__(self, Cursor):
        self.Cur = Cursor
    
    ## Create table
    #
    # Create table Pcd
    #
    # @param ID:                   ID of a Pcd
    # @param CName:                CName of a Pcd
    # @param TokenSpaceGuidCName:  TokenSpaceGuidCName of a Pcd
    # @param Token:                Token of a Pcd
    # @param DatumType:            DatumType of a Pcd
    # @param Model:                Model of a Pcd
    # @param BelongsToFile:        The Pcd belongs to which file
    # @param BelongsToFunction:    The Pcd belongs to which function
    # @param StartLine:            StartLine of a Pcd
    # @param StartColumn:          StartColumn of a Pcd
    # @param EndLine:              EndLine of a Pcd
    # @param EndColumn:            EndColumn of a Pcd
    #
    def Create(self):
        SqlCommand = """create table IF NOT EXISTS Pcd(ID SINGLE PRIMARY KEY,
                                                       CName VARCHAR NOT NULL,
                                                       TokenSpaceGuidCName VARCHAR NOT NULL,
                                                       Token INTEGER,
                                                       DatumType VARCHAR,
                                                       Model INTEGER NOT NULL,
                                                       BelongsToFile SINGLE NOT NULL,
                                                       BelongsToFunction SINGLE DEFAULT -1,
                                                       StartLine INTEGER NOT NULL,
                                                       StartColumn INTEGER NOT NULL,
                                                       EndLine INTEGER NOT NULL,
                                                       EndColumn INTEGER NOT NULL
                                                      )"""
        self.Cur.execute(SqlCommand)
        EdkLogger.verbose("Create table Pcd ... DONE!")

    ## Insert table
    #
    # Insert a record into table Pcd
    #
    # @param ID:                   ID of a Pcd
    # @param CName:                CName of a Pcd
    # @param TokenSpaceGuidCName:  TokenSpaceGuidCName of a Pcd
    # @param Token:                Token of a Pcd
    # @param DatumType:            DatumType of a Pcd
    # @param Model:                Model of a Pcd
    # @param BelongsToFile:        The Pcd belongs to which file
    # @param BelongsToFunction:    The Pcd belongs to which function
    # @param StartLine:            StartLine of a Pcd
    # @param StartColumn:          StartColumn of a Pcd
    # @param EndLine:              EndLine of a Pcd
    # @param EndColumn:            EndColumn of a Pcd
    #
    def Insert(self, ID, CName, TokenSpaceGuidCName, Token, DatumType, Model, BelongsToFile, BelongsToFunction, StartLine, StartColumn, EndLine, EndColumn):
        SqlCommand = """insert into Pcd values(%s, '%s', '%s', %s, '%s', %s, %s, %s, %s, %s, %s, %s)""" \
                                            % (ID, CName, TokenSpaceGuidCName, Token, DatumType, Model, BelongsToFile, BelongsToFunction, StartLine, StartColumn, EndLine, EndColumn)
        self.Cur.execute(SqlCommand)
        EdkLogger.verbose(SqlCommand + " ... DONE!")
    
    ## Query table
    #
    # Query all records of table Pcd
    #  
    def Query(self):
        EdkLogger.verbose("\nQuery tabel Pcd started ...")
        SqlCommand = """select * from Pcd"""
        self.Cur.execute(SqlCommand)
        for Rs in self.Cur:
            EdkLogger.verbose(Rs)
        SqlCommand = """select count(*) as Count from Pcd"""
        self.Cur.execute(SqlCommand)
        for Item in self.Cur:
            EdkLogger.verbose("***Total %s records in table Pcd***" % Item)
        EdkLogger.verbose("Query tabel Pcd DONE!")

    ## Drop a table
    #
    # Drop the table Pcd
    #
    def Drop(self):
        SqlCommand = """drop table IF EXISTS Pcd"""
        self.Cur.execute(SqlCommand)
        EdkLogger.verbose("Drop tabel Pcd ... DONE!")

