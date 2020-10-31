from PyQt5 import *
from PyQt5.QtWidgets import *
from mainwindow import *
import sys
import moviepy
from pytube import YouTube
from pytube import Playlist
import time


#status


#FUNCTİON

def checkedConvert():
    if ui.r_playlst.isChecked():
        link=ui.lE_link.text()

        pl=Playlist(link)
        pl.download_all('/home/ilkayus/Downloads')

    elif ui.r_vdeo.isChecked():
        link=ui.lE_link.text()

        yt = YouTube(link)
        ys = yt.streams.get_highest_resolution()
        ys.download('/home/ilkayus/Downloads')
        ui.l_status.setText("Download Successful")

    else: ui.l_status.setText("Type Link...")
        
     


Uygulama=QApplication(sys.argv)
penAna=QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()

#COMMAND
ui.pB_download.clicked.connect(checkedConvert)




sys.exit(Uygulama.exec_())