import os
from pydub import AudioSegment
import pandas as pd
from gtts import gTTS

def textToSpeach(text,filename):
    mytext = str(text)
    language = 'en'
    myobj = gTTS(text=mytext, lang=language,slow=False)
    myobj.save(filename)

def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
        return combined

def generateSkelton():
    audio = AudioSegment.from_mp3("flight.mp3")

    #passengers for flight
    start = 0 *1000
    finish =   4.7 *1000
    audioProceed = audio[start:finish]
    audioProceed.export('1English.mp3',format="mp3")


    #to
    start = 6.5 * 1000
    finish = 6.7 * 1000
    audioProceed = audio[start:finish]
    audioProceed.export('2English.mp3', format="mp3")

    #Please go to gate
    start = 7 * 1000
    finish = 8.2 * 1000
    audioProceed = audio[start:finish]
    audioProceed.export('3English.mp3', format="mp3")

def generateAnnoucment(filename):
    df = pd.read_csv(filename)
    print(df)
    for index, items in df.iterrows():
        #flight no
        textToSpeach(items['flight_no'],'1English.mp3')

        textToSpeach(items['country'], '2English.mp3')

        textToSpeach(items['gate_no'], '3English.mp3')

        audios = [f"{i}English.mp3" for i in range(1,3)]
        annoucement= mergeAudios(audios)
        annoucement.export(f"annoucement{items['country']}{index+1}.mp3",format="mp3")



if __name__=="__main__":
    print("Generating Skeliting....")
    generateSkelton()
    print("Now generating Skelton")
    generateAnnoucment("file.csv")
    print("Now generating Annoucments")

