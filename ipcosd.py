from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist,QMediaContent
import sys
import os
import time
import random

import iposdui
import changeosd


AllSongs=[]
mmplaylist=QMediaPlaylist()
mmplayer=QMediaPlayer()
mmplayer.setPlaylist(mmplaylist)
validMediaFormart=["mp3","wav","m4a","aac","ogg","wma"]

def addLog(level:int,logcontext:str):
    '''
    level:0-info,1-error
    '''
    levellist=["INFO","ERROR"]
    global mwindui
    mwindui.logarea.appendPlainText(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {levellist[level]} "+logcontext)

def initPlayList():
    global AllSongs,mwindui,mmplayer
    mwindui.songlist.clear()
    mmplaylist.clear()
    for persong in AllSongs:
        mmplaylist.addMedia(QMediaContent(QUrl.fromLocalFile(persong)))
        mwindui.songlist.addItem(os.path.split(persong)[1])
    #print(mmplaylist.mediaCount())
    mwindui.songscnt.setText(f"--/{mmplaylist.mediaCount()}")
    mwindui.songlist.setCurrentRow(0)
    mmplaylist.setCurrentIndex(0)
    mmplayer.setMuted(False)
    addLog(0,f"初始化播放列表,共{mmplaylist.mediaCount()}项")

def initPrepare():
    global mwindui
    initPlayList()
    mwindui.logarea.clear()
    addLog(0,"初始化完成")

def removeSong():
    global mwindui,AllSongs,mmplaylist
    if mwindui.songlist.selectedIndexes():
        removeedsong=AllSongs[mwindui.songlist.currentIndex().row()]
        AllSongs.pop(mwindui.songlist.currentIndex().row())
        mmplaylist.removeMedia(mwindui.songlist.currentIndex().row())
        mwindui.songlist.takeItem(mwindui.songlist.currentRow())
        updateCurrentSong()
        addLog(0,f"移除项目 {removeedsong}")

def removeAllSongs():
    global mwindui,AllSongs
    if len(AllSongs):
        mwindui.songlist.clear()
        AllSongs.clear()
        initPlayList()
        addLog(0,"移除所有项")
    else:
        addLog(1,"列表是空的欸")

def addSingleSong():
    Files=QFileDialog.getOpenFileNames()
    #print(Files)
    addedcnt=0
    for file in Files[0]:
        if os.path.exists(file) and (not file in AllSongs) and file.split(".")[-1].lower() in validMediaFormart:
            AllSongs.append(file)
            #print(f"add {file}")
            addedcnt+=1
        else:
            print(f"file {file} is invalid")
    addLog(0,f"添加{len(Files[0])}项,成功:{addedcnt}项")
    initPlayList()
    #print(AllSongs)

def addSongsFromForder():
    global mwindui,AllSongs
    baseForder=QFileDialog.getExistingDirectory()
    #print(baseForder)
    if os.path.isdir(baseForder):
        addedcnt=0
        for froot, fdirs, ffiles in os.walk(baseForder):
        # froot 表示当前正在访问的文件夹路径
        # fdirs 表示该文件夹下的子目录名list
        # ffiles 表示该文件夹下的文件list
            for f in ffiles:
                currentfn=os.path.join(froot, f).replace("\\", "/")
                if os.path.exists(currentfn) and (not currentfn in AllSongs) and currentfn.split(".")[-1].lower() in validMediaFormart:
                    AllSongs.append(currentfn)
                    addedcnt+=1
                    #print(f"add {currentfn}")
        
        addLog(0,f"成功:{addedcnt}项")
        initPlayList()
    else:
        print(f"{baseForder} is not a directory")
        addLog(1,"所选目录无效")

def setipcstatus(status:str):
    global mwindui
    mwindui.ipcstatus.setText(status)
    mwindui.ipcstatus.setStyleSheet(f"color:{'green' if status=='正常' else 'red'};")

def testIP():
    global mwindui
    currip=mwindui.ipcip.text()
    if currip=="":
        addLog(1,"我认为你应该在IP栏写点什么")
    else:
        ips=currip.split(".")
        if len(ips)==4:
            addLog(0,"IP地址格式正确,检查通信情况")
            addLog(0,"应用默认UI...")
            mapp.processEvents()
            testresult=changeosd.testconn(currip)
            if testresult[0]==200:
                addLog(0,f"状态码:{testresult[0]},成功")
                setipcstatus("正常")
            elif testresult[0]=="ERR":
                addLog(1,f"连接错误,{testresult[1]}")
                setipcstatus("错误")
            else:
                addLog(1,f"状态码:{testresult[0]},失败,{testresult[1]}")
                setipcstatus("错误")
        else:
            addLog(1,"IP地址格式错误")

def startplay():
    global mwindui,AllSongs
    if len(AllSongs)!=0:
        mmplayer.play()
        addLog(0,"开始播放")
        #updateCurrentSong()
        #updateProcess()

us_flag_ft=1
def updateCurrentSong():
    global mwindui,us_flag_ft
    if mwindui.orderrand.isChecked():
        us_flag_ft=0
        mmplaylist.setCurrentIndex(random.randint(0,mmplaylist.mediaCount()-1))
    else:
        us_flag_ft=1
    if us_flag_ft==0 or not mwindui.orderrand.isChecked():
        if mmplaylist.currentIndex()==-1:
            mmplayer.stop()
            mwindui.currentsongl.setText("队列结束")
            addLog(0,"队列结束")
        else:
            mwindui.currentsongl.setText(mmplaylist.currentMedia().canonicalUrl().fileName())
            mwindui.songscnt.setText(f"{mmplaylist.currentIndex()+1}/{mmplaylist.mediaCount()}")
            #print(mmplaylist.currentMedia().canonicalUrl().path()[1::])
            addLog(0,f"当前播放: {mmplaylist.currentMedia().canonicalUrl().fileName()}")
        us_flag_ft=1
def updateProcess():
    global mwindui,mmplayer,mmplaylist
    mwindui.songprogress.setMaximum(mmplayer.duration())
    mwindui.songprogress.setValue(mmplayer.position())

mapp=QApplication(sys.argv)
mwind=QMainWindow()
mwindui=iposdui.Ui_ipcosdsongui()
mwindui.setupUi(mwind)

mwindui.removesingleb.clicked.connect(removeSong)
mwindui.loadsongsb.clicked.connect(addSingleSong)
mwindui.removeallb.clicked.connect(removeAllSongs)
#mwindui.testipc.clicked.connect(lambda:threading.Thread(target=testIP,daemon=True).start())
mwindui.testipc.clicked.connect(testIP)
mwindui.loadforder.clicked.connect(addSongsFromForder)

mwindui.startb.clicked.connect(startplay)
mwindui.nextsongb.clicked.connect(mmplaylist.next)
mwindui.prevsongb.clicked.connect(mmplaylist.previous)
mwindui.stopb.clicked.connect(mmplayer.stop)

mmplaylist.currentIndexChanged.connect(lambda:updateCurrentSong())
mmplayer.positionChanged.connect(lambda:updateProcess())


initPrepare()
mwind.show()
sys.exit(mapp.exec_())