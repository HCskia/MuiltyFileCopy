import random
import os
import shutil
import time


def writeLog(context):
    print(context)
    with open("log.txt", 'a', encoding="utf-8")as f:
        f.write(context)
        f.close()

def getFolderPath():
    LOG = "正在获取目标文件夹.....\n"
    with open("folderPath.txt", 'r', encoding="utf-8")as f:
        folderPath = f.read()
        f.close()
    directories = []
    for root, dirs, files in os.walk(folderPath):
        for name in dirs:
            dirPath = os.path.join(root, name)
            LOG += f"添加目标文件夹：{dirPath}\n"
            directories.append(dirPath)
    LOG += f"获取目标文件夹完毕！\n\n"
    writeLog(LOG)
    return directories

def getFiles():
    LOG = "正在获取文件地址.....\n"
    path_list = []
    filenames = os.listdir("files")
    for filename in filenames:
        a = os.path.join("files", filename)
        LOG += f"添加文件地址：{a}\n"
        path_list.append(a)
    LOG += f"获取文件地址完毕！\n\n"
    writeLog(LOG)
    return path_list

def MuiltyFileCopy():
    writeLog("程序运行......\n")
    FileList = getFiles()
    for FolderPath in getFolderPath():
        writeLog(f"正在复制文件到 [{FolderPath}] 文件夹\n")
        for FilePath in FileList:
            writeLog(f"尝试复制文件[{os.path.basename(FilePath)}]\n")
            shutil.copy(FilePath, FolderPath)
            time.sleep(2.5)
        writeLog(f"准备检查 [{FolderPath}] 文件夹内容是否齐全\n")
        for FilePath in FileList:
            FileName = os.path.basename(FilePath)
            tempFilePath = os.path.join(FolderPath, FileName)
            if os.path.getsize(FilePath) != os.path.getsize(tempFilePath):
                writeLog(f"[{FileName}] 疑似复制失败！\n")
            else:
                writeLog(f"[{FileName}] 复制成功！\n")
                continue
        writeLog(f"\n")
    writeLog("程序运行结束......\n")


MuiltyFileCopy()