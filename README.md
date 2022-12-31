## Description
The Echo VR API breaks when Quest Pro controllers are connected as a result of an additional network interface that is created for the controllers. The API is bound to that IP instead, which isn't network accessible. This is a workaround for joining [Spark](https://www.ignitevr.gg/spark) links or session IDs via a website loaded on the Quest's browser.

## Usage
### Installation
Python and ADB must both be installed and added to path. The python version shouldn't be too sensitive as long as it is Python 3.
####[Python 3.9.2 Windows 64-bit Installer](https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe)
####[Android Studio](https://developer.android.com/studio)

Then, clone/download the source from Github

### Running the program
First, run `FIRST_TIME_SETUP.bat`
The headset must be plugged in to the computer with the headset awake and controllers connected. This will generate `staticIP.txt`, which is used to find the IP that the API is bound to. This only needs to be run once unless something changes about the headset or controllers. Any USB connection with data is sufficient, but make sure to allow access to files from within the headset after plugging in.

Next, run `RUN_ME.bat`
The window will prompt for a session ID or Spark Link. Paste it and hit enter. It should return a link.

Finally, launch Echo Arena and load up the link from `run_me` in the Meta Quest Browser while in a lobby or game. Select your team (Currently bugged) and then click join. After a few seconds, you should be loaded into the session.

## Known Issues
* Player always joins as spectator, regardless of what team option is selected

## Support
DM Zzenith#4822 on Discord with any issues. This was hacked together very quickly as a proof-of-concept, so there will likely be issues.