## Description
The Echo VR API breaks when Quest Pro controllers are connected as a result of an additional network interface that is created for the controllers. The API is bound to that IP instead, which isn't network accessible. This program is a workaround for joining [Spark](https://www.ignitevr.gg/spark) links or session IDs via a website loaded on the Quest's browser.

## Usage
### Installation
Python must be installed and added to path. The version shouldn't be too sensitive as long as it is Python 3.
* [Python 3.9.2 Windows 64-bit Installer](https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe)

Then, clone/download the source from Github

### Running the program
Run `RUN_ME.bat`
The window will prompt for a session ID or Spark Link. Paste it and hit enter. It should return a link.

Finally, launch Echo Arena and load up the link from `run_me` in the Meta Quest Browser while in a lobby or game. Feel free to bookmark the link for convenience, it should remain static. Select your team and then click join. After a few seconds, you should be loaded into the session.

## Common Problems
* Ensure that you are not running a VPN

## Support
DM `Zzenith#4822` on Discord with any issues. This was hacked together very quickly as a proof-of-concept, so there will likely be issues.
