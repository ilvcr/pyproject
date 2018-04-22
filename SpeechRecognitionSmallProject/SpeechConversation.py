#语音对话
from win32com.client import constants
import os
import win32com.client
import pythoncom

speaker = win32com.client.Dispatch("SAPI.SPVOICE")


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
        print("小伙子你在说 ", newResult.PhraseInfo.GetText())
        speechstr=newResult.PhraseInfo.GetText()
        if  speechstr=="赵大":
            speaker.Speak("赵大，我愿意")
        elif  speechstr=="你好":
            speaker.Speak("你好啊")
        elif  speechstr=="国庆快乐":
            speaker.Speak("是的，国庆快乐")
        elif  speechstr=="新年快乐":
            speaker.Speak("新年happy")
        elif  speechstr=="赵二":
            speaker.Speak("来自海边的汉子")
        elif  speechstr=="王五":
            speaker.Speak("波涛涌用")
        elif  speechstr=="彭彭":
            speaker.Speak("彭砰砰")
        elif  speechstr=="马六":
            speaker.Speak("你的马儿去了哪里")
        elif  speechstr=="孟七":
            speaker.Speak("孟七，你好")
        else:
            pass

if __name__ == '__main__':

    speaker.Speak("语音识别开启")
    wordsToAdd = ["赵大",
                  "你好",
                  "国庆快乐",
                  "新年快乐",
                  "王五",
                  "赵二",
                  "彭彭",
                  "马六",
                  "孟七",
                  ]
    speechReco = SpeechRecognition(wordsToAdd)
    while True:
        pythoncom.PumpWaitingMessages()
