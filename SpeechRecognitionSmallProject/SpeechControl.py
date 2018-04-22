#语音控制
from win32com.client import constants
import os
import win32com.client
import pythoncom
class SpeechRecognition:
    def __init__(self, wordsToAdd):
        self.speaker = win32com.client.Dispatch("SAPI.SpVoice")
        self.listener = win32com.client.Dispatch("SAPI.SpSharedRecognizer")
        self.context = self.listener.CreateRecoContext()
        self.grammar = self.context.CreateGrammar()
        self.grammar.DictationSetState(0)
        self.wordsRule = self.grammar.Rules.Add("wordsRule", constants.SRATopLevel + constants.SRADynamic, 0)
        self.wordsRule.Clear()
        [self.wordsRule.InitialState.AddWordTransition(None, word) for word in wordsToAdd]
        self.grammar.Rules.Commit()
        self.grammar.CmdSetRuleState("wordsRule", 1)
        self.grammar.Rules.Commit()
        self.eventHandler = ContextEvents(self.context)
        self.say("Started successfully")
    def say(self, phrase):
        self.speaker.Speak(phrase)
class ContextEvents(win32com.client.getevents("SAPI.SpSharedRecoContext")):
    def OnRecognition(self, StreamNumber, StreamPosition, RecognitionType, Result):
        newResult = win32com.client.Dispatch(Result)
        print("You are talking to ", newResult.PhraseInfo.GetText())
        speechstr=newResult.PhraseInfo.GetText()#识别的文本
        if  speechstr=="Shutdown":
            os.system("shutdown -s -t 300")
        elif  speechstr=="Cancle Shutdown":
            os.system("shutdown -a")
        elif speechstr=="Notepad":
            os.system("notepad")
        elif speechstr=="Wordpad":
            os.system("write")
        elif speechstr=="Paint":
            os.system("mspaint")
        elif speechstr=="Close Notepad":
            os.system("taskkill /f   /im  notepad.exe")
        elif  speechstr=="Seting":
            os.system("msconfig")
        else:
            print("I'm not understand!")


if __name__ == '__main__':
    wordsToAdd = ["Shutdown", "Cancle Shutdown", "Notepad", "Paint","Wordpad","Seting","Close Notepad"]
    speechReco = SpeechRecognition(wordsToAdd)
    while True:
        pythoncom.PumpWaitingMessages()
