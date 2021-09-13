import os, shutil
crackroot = "C:/Users/Infinime/Downloads/Football Manager 2021/CrackTest Folders"
root = "C:/Users/Infinime/Downloads/Football Manager 2021"

with open("cracks.txt", "r") as f:
    crackarr = f.read().split(", ")
    crackarr = list(map(lambda x: x[1:-1], crackarr))[:-1]
    crackarr = list(filter(lambda x: 'steam' not in x, crackarr))
print(crackarr)

with open("stopped.txt", "r") as f:
    stopped=int(f.readlines()[-1])

if os.path.exists(root+"/steam_emu.ini"): os.unlink(root+"/steam_emu.ini")
if os.path.exists(root+"/steam"): os.system(f'rmdir /S /Q "{root+"/steam"}"')

shutil.copytree(crackarr[stopped]+"/steam", root+"/steam")
shutil.copy(crackarr[stopped]+"/steam_emu.ini", root)

with open("stopped.txt", "r+") as f:
    f.write("\n"+str(int(f.readlines()[-1])+1))

os.startfile(r"C:/Users/Infinime/Downloads/Football Manager 2021/fm26.exe")

print(f"{stopped} try. Launched the app")
