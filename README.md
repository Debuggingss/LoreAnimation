# LoreAnimation

**This is for 1.8.9, requires ffmpeg and ChatTriggers 1.3.2 version**

- ChatTriggers: https://chattriggers.com
- ffmpeg: http://www.ffmpeg.org/

NOTE: *The code is really bad and the entire thing is very non-user friendly. Might make it more usable in the future. The only reason I decided to share this script in it's current state is because I was requested to, otherwise I wouldn't have considered it yet.*

## Generating the video data:
1) Resize your video to the lore size you want (I use 40 * 30 with Normal GUI scale). For this step I used this tool: https://ezgif.com/resize-video
2) Open the script in any text editor and go to line 51. Change the `width` and `height` variables to the same dimensions used in the first step.
3) Place your resized video into the script's directory.
4) Create a folder named 'frames' in the same directory as the script.
5) Open a Command Promt in the script directory.
6) Type in this command: `ffmpeg -i <yourvideo>.mp4 -vf "fps=fps=10" frames/%07d.raw`, this *should* create a bunch of .raw files in the 'frames' directory.
7) Now you have to determine if you want black/white video or colored. (The colors looks very ugly because of the 16 chat color limit in 1.8.9)
  By default the script will use black and white. If you want colors you have to go into the script file and comment out line 11-24. (Note that colored videos are not only ugly, but they take a very long time to generate because of the bad algorithm.)
8) Run the script in the Command Promt using `python converter.py`
9) Once the script is done you will be left with a file called 'output.json'.

## Displaying the video in the game:
**You need to be in Creative Mode (preferably Singleplayer)**
1) Type in chat `/ct console js`, this will open the ChatTriggers JavaScript console.
2) Copy paste the code from `script.js` into the text area.
3) Change the PATH variable to your output.json path.
4) Press CTRL+ENTER to run the code.
5) Now you have to wait 3 seconds and the animation should start playing in your first hotbar slot.


