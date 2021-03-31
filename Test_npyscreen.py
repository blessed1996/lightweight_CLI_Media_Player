import os
import subprocess

import npyscreen


# This class (widget) selects files from the path-List and plays them in order.
# Afterwards the List gets cleared.
class PlayButton(npyscreen.ButtonPress):
    def whenPressed(self):
        for file in SelectButton.path:
            subprocess.run(
                ["mplayer", "-really-quiet", "-vo", "caca", file]
            )
        SelectButton.path.clear()


# This class (widget) lets us select a file and write the path of said file in a list.
class SelectButton(npyscreen.ButtonPress):
    path = []

    def whenPressed(self):
        media = npyscreen.selectFile(must_exist=True)
        SelectButton.path.append(os.path.realpath(media))


# FormTable fills the Form with widgets. SplitForm draws a line at the bottom of th Form (aesthetics).
class FormTable(npyscreen.ActionFormMinimal, npyscreen.SplitForm):
    def create(self):
        self.show_atx = 10
        self.show_aty = 2
        self.select = self.add(SelectButton, name="Select Media")
        self.nextrely += 1
        self.play = self.add(PlayButton, name="Play Media")
        self.nextrely += 1
        self.exit = self.add(npyscreen.TitleFixedText, name="Press OK to exit")

    # ActionFormMinimal gives us an "OK"-Button in the bottom right corner.
    # This method give this Button the purpose of exiting the Form.
    def on_ok(self):
        npyscreen.notify_confirm("Good Bye!", editw=1)
        self.parentApp.setNextForm(None)


# MediaPlayer initializes a Form as an Object and defines the Form.
class MediaPlayer(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', FormTable, name="MediaDevice done simple", lines=20, columns=60, draw_line_at=17)


if __name__ == "__main__":
    app = MediaPlayer().run()
