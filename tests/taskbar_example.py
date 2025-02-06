import comtypes.client as cc
import win32api
import win32gui
import time
import tqdm

cc.GetModule('tl.tlb')
import comtypes.gen.TaskbarLib as tbl
taskbar = cc.CreateObject('{56FDF344-FD6D-11d0-958A-006097C9A090}', interface=tbl.ITaskbarList3)
taskbar.HrInit()

# find hWnd of the console
title = win32api.GetConsoleTitle()
tag = title + '___'
win32api.SetConsoleTitle(tag)
time.sleep(0.05)
hWnd = win32gui.FindWindow(None, tag)
win32api.SetConsoleTitle(title)
assert hWnd

# demo loop
for t in tqdm.trange(50):
    time.sleep(0.1)
    # this should be inside tqdm module:
    taskbar.SetProgressValue(hWnd, t, 50)
    taskbar.SetProgressState(hWnd, 0x2)