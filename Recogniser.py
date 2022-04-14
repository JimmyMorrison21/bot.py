import speech_recognition as sr


sample_audio = sr.AudioFile('C:\\Users\\yourh\\PycharmProjects\\botProject\\voice.ogg')
with sample_audio as audio_file:
    audio_content = recog.record(audio_file)
recog.recognize_google(audio_content)