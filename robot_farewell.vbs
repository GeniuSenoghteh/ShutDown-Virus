Set S = CreateObject("SAPI.SpVoice")
Dim messages
messages = Array("Goodbye human...", "See you in the void...", "Reboot? Maybe.", "Ha ha ha.")
For i = 0 To UBound(messages)
    S.Speak messages(i)
Next
