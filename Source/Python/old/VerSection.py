from Ffs import Ffs
import Section
import os
import subprocess
from GenFdsGlobalVariable import GenFdsGlobalVariable
class VerSection (Section.Section):
    def __init__(self):
        self.Alignment = None
        self.BuildNum = None
        self.StringData = None
        self.FileName = None
        
    def GenSection(self,OutputPath, ModuleName, KeyStringList, FfsInf = None):
        #
        # Prepare the parameter of GenSection
        #
        if FfsInf != None:
            self.Alignment = FfsInf.__ExtendMarco__(self.Alignment)
            self.BuildNum = FfsInf.__ExtendMarco__(self.BuildNum)
            self.StringData = FfsInf.__ExtendMarco__(self.StringData)
            self.FileName = FfsInf.__ExtendMarco__(self.FileName)
            
        OutputFile = os.path.join(OutputPath,
                                  ModuleName+Ffs.SectionSuffix.get('VERSION'))
        OutputFile = os.path.normpath(OutputFile)
        
        """Get Build Num """
        BuildNum = ''
        if not (self.BuildNum == None) :
            BuildNum = ' -j ' + '%d' %self.BuildNum;
 
        """Get String Data"""
        StringData = ''
        if self.StringData != None:
             StringData = self.StringData
        elif self.FileName != None:
            f = open (self.FileName, 'r')
            StringData = f.read()
            f.close()
        else:
            StringData = ''
            
        GenSectionCmd = 'GenSec -o '                + \
                         OutputFile                 + \
                         ' -s EFI_SECTION_VERSION ' + \
                         '-n '                      + \
                         '\"'                       + \
                         StringData                 + \
                         '\"'                       + \
                         BuildNum                   
                         
        #
        # Call GenSection
        #
        print GenSectionCmd
        GenFdsGlobalVariable.CallExternalTool(GenSectionCmd, "Gensection Failed!")
        return OutputFile, self.Alignment