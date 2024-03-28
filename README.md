# ADB_PIN_RECOVERY: Unlocking Android Devices
The ADB PIN Recovery tool is designed for unlocking Android devices through a brute force approach, specifically when ADB (Android Debug Bridge) is enabled and the computer is authorized. It's important to note that this tool has been tested exclusively on Android 8.1.0 and is not compatible with newer Android versions.

Utilizing the deprecated 'locksettings verify' command, this tool attempts to determine the correct PIN. To circumvent the automatic lockout triggered after multiple incorrect attempts, the tool restarts the phone after every five attempts.

While there may be faster methods for PIN recovery, the current implementation of this tool is capable of processing all possible four-digit combinations in approximately 18 hours.
