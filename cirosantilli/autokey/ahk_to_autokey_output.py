#NoEnv
SendMode Input  
SetWorkingDir %A_ScriptDir%
;Autohotkey

#-- global switches ------------------------------------------------------------#
oneletters = 0		#- one letter button -#
html = 1		#- html on off -#

#- paths -#
root = C:

ciro = %root%\Users\Ciro
htdocs = %root%\xampp\htdocs
programFilesX86 = %root%\Program Files (x86)

documents = %ciro%\Documents
desktop = %ciro%\Desktop

backup = %documents%\backup
downloads = %documents%\Downloads
rapidshare = %documents%\Rapidshare

share = %backup%\share
noshare = %backup%\noshare

music = %share%\Music
films = %share%\Videos\Films
games = %share%\Games
images = %share%\Images
texts = %share%\Texts
chinese_learning = %share%\Chinese Learning

threeA = %noshare%\x\3A
programs = %noshare%\programs
certificates = %noshare%\certificates

python = %programs%\python
latex = %programs%\latex
autohotkeys = %programs%\autohotkeys

notepadppf = %programFilesX86%\Notepad++

notepadpp = %notepadppf%\notepad++.

elearning = %htdocs%\elearning

mathematics = %texts%\Mathematics
physics = %texts%\Physics

#- caps lock initialization -#
SetCapsLockState, AlwaysOff

#-- global functions ------------------------------------------------------------#
OpenFolder(dir)
{
	;Run %dir%
	;Run C:\Program Files (x86)\muCommander\muCommander.exe "%dir%" "%dir%"
	;Run C:\Program Files (x86)\FreeCommander\FreeCommander.exe  "%dir%"
	Run C:\Program Files (x86)\CubicExplorer\CubicExplorer.exe	"%dir%"
}

DirPathToClipboard()
{
MouseGetPos, xpos, ypos 
click 525, 45
Send,^c
Send,{Tab 4}
MouseMove, xpos, ypos
}

FilePathToClipboard()
{
Send,{F2}
CopyLine()
Sleep,200
fileName = %clipboard%
DirPathToClipboard()
Sleep,200
clipboard = %clipboard%\%fileName%
}

CopyLine()
{
Send,{Home}{Shift Down}{End}{Shift Up}{Control Down}c{Control Up}{End}			    #- copy line -#
}

DoubleLine()				#- double line. TODO, still destroys clipboard -#
{
old_clipboard = %clipboard%
CopyLine()
Sleep,100
Send,<enter>^v
Sleep,100
clipboard = %old_clipboard%									    
}

CutLine()
{
Send,{Home}{Shift Down}{End}{Shift Up}{Control Down}x{Control Up}		    #- cut line -#
}

ClearLine()
{
Send,{Home}{Shift Down}{End}{Shift Up}{Del}					    #- Clear Line -#
}

#Hotstring EndChars :,.?!`n `t #- affects all script, even what comes before... -#

#-- Personal data for quick input ---------------------------------------------#
#Hotstring * o
engine.create_abbreviation(folder,"gnm;","gnm;",r"Ciro") #- Given NaMe -#
engine.create_abbreviation(folder,"lnm;","lnm;",r"Santilli") #- Last name -#
engine.create_abbreviation(folder,"fnm;","fnm;",r"Duran Santilli") #- Family name -#
engine.create_abbreviation(folder,"cnm;","cnm;",r"Ciro Duran Santilli") #- Complete name -#
engine.create_abbreviation(folder,"cnmf;","cnmf;",r"Ciro DURAN SANTILLI") #- French capital last name standard -#
engine.create_abbreviation(folder,"cnma;","cnma;",r"Ciro D. Santilli") #- Abbreviated (or American) dot middle name-#
engine.create_abbreviation(folder,"fgnm;","fgnm;",r"Duran Santilli<tab>Ciro<tab>") #- family then given name for internet input-#

engine.create_abbreviation(folder,"bdt;","bdt;",r"14/05/1989")engine.create_abbreviation(folder,"bct;","bct;",r"Rio Claro") #- address -#
engine.create_abbreviation(folder,"adr;","adr;",r"10, boulevard des Maréchaux") #- address -#
engine.create_abbreviation(folder,"adrc;","adrc;",r"Bâtiment FOCH, Appartement 10.20.39") #- address complement -#
engine.create_abbreviation(folder,"pcd;","pcd;",r"91120") #- Postal CoDe -#
engine.create_abbreviation(folder,"city;","city;",r"Palaiseau") #- city -#
engine.create_abbreviation(folder,"cpc;","cpc;",r"Palaiseau, 91120") #- City Postal CoDe -#
engine.create_abbreviation(folder,"fadr;","fadr;",r"10, boulevard des Maréchaux<tab>Bâtiment FOCH, Appartement<tab>91120<tab>Palaiseau	#- Full address for internet input-#") #- EP address -#

engine.create_abbreviation(folder,"epf;","epf;",r"École Polytechnique") #- Ãƒâ€°cole Polytechnique (France) -#
engine.create_abbreviation(folder,"epadr;","epadr;",r"ECOLE POLYTECHNIQUE") #- address -#
engine.create_abbreviation(folder,"epadrc;","epadrc;",r"Route de Saclay") #- address complement line 2 -#
engine.create_abbreviation(folder,"eppcd;","eppcd;",r"91128") #- Postal CoDe -#
engine.create_abbreviation(folder,"epcity;","epcity;",r"PALAISEAU Cedex") #- city -#
engine.create_abbreviation(folder,"epfadr;","epfadr;",r"ECOLE POLYTECHNIQUE<tab>Route de Saclay<tab>91128<tab>PALAISEAU Cedex	    #- Full address for internet input-#") #- contact -#
engine.create_abbreviation(folder,"mail;","mail;",r"ciro.santilli@gmail.com") #- email -#
engine.create_abbreviation(folder,"tel;","tel;",r"0169591651") #- fixed telephone -#

engine.create_abbreviation(folder,"cell;","cell;",r"0658851651") #- cell phone -#
engine.create_abbreviation(folder,"tcell;","tcell;",r"ciro.santilli@gmail.com") #- cell phone -#
engine.create_abbreviation(folder,"ncs;","ncs;",r"Ciro D. Santilli`ncel: {+}33658851651`nskype: ciro.santilli		#- Name, Cell, Skype -#") #- social security France -#
engine.create_abbreviation(folder,"smerep;","smerep;",r"139205899") #- SMEREP number -#
engine.create_abbreviation(folder,"nss;","nss;",r"1890599416120") #- numero de securite sociale -#
engine.create_abbreviation(folder,"ass;","ass;",r"16 Bd. du General Leclerc - 92115 Clichy CEDEX") #- adress ss -#
engine.create_abbreviation(folder,"ssc;","ssc;",r"Vitale<enter>Organisme: 99911061<enter>Adresse: 16 Bd. du General Leclerc - 92115 Clichy CEDEX<enter>Numéro de securité sociale: 189059941612087 #- Complete ss -#") #- user pass -#
engine.create_abbreviation(folder,"unm;","unm;",r"cirosantilli") #- standard User Name -#
engine.create_abbreviation(folder,"pwd;","pwd;",r"fgb4669201") #- cheap password -#
engine.create_abbreviation(folder,"pwdu;","pwdu;",r"Fgb4669201") #- cheap password Upper case-#
engine.create_abbreviation(folder,"upwd;","upwd;",r"cirosantilli<tab>fgb4669201<enter>") #- user + password for quick internet input-#
engine.create_abbreviation(folder,"oid;","oid;",r"https://plus.google.com/106598607405640635523/posts	#- Open ID-#") #-- Time stamps ---------------------------------------------#
engine.create_abbreviation(folder,"dmy;","dmy;",r"	#- dd/mm/yyyy -#")Send,%A_DD%/%A_MM%/%A_YYYY% #- day month year, most standard form  -#
return

engine.create_abbreviation(folder,"dmys;","dmys;",r"	#- dd-mm-yyyy -#")Send,%A_DD%-%A_MM%-%A_YYYY% #- day month year, most standard form  -#
return

engine.create_abbreviation(folder,"ymds;","ymds;",r"	#- Year Month Day with Slashes. For backuping. -#")Send,%A_YYYY%-%A_MM%-%A_DD% #- day month year, most standard form  -#
return

::dmyw;::
	Send,%A_DD%/%A_MM%/%A_YYYY% %A_DDD% #-  %A_Hour%:%A_Min%:%A_Sec%  day month year, most standard form  -#
return

engine.create_abbreviation(folder,"tms;","tms;",r"	#- TiMeStamp, specially for file versionning -#")Send, %A_YYYY%-%A_MM%-%A_DD% %A_Hour%-%A_Min%-%A_Sec%
return

#-- quick and dirty text processing ------------------------------------------------------------#

engine.create_abbreviation(folder,"dts\","dts\",r"	    #- dot to space -#")StringReplace, clipboard, clipboard, ., %A_SPACE%, All
return

engine.create_abbreviation(folder,"uts\","uts\",r"	    #- underline to space -#")StringReplace, clipboard, clipboard, _, %A_SPACE%, All
return

engine.create_abbreviation(folder,"stu\","stu\",r"	    #- space to underline -#")StringReplace, clipboard, clipboard, %A_SPACE%, _, All
return

return

#Hotstring *0 o0

#-- Autohotkeys ------------------------------------------------------------#

;reload current script
#a::
Send,^s
Reload
return

;edit current script. 
#i::
    Run notepad++ %A_ScriptFullPath%
return

;suspend current script
#s::
Suspend
return

#- autohotkey script -#

engine.create_abbreviation(folder,"hstr;","hstr;",r"{:}{:}{:}{:}{Left 2}") #- Ahk hotstring -#
engine.create_abbreviation(folder,"avar;","avar;",r"{%}{%}{Left 1}") #- Ahk variable value -#
engine.create_abbreviation(folder,"acm;","acm;",r"{;}-  -{;}{Left 3}") #- Ahk comment -#
engine.create_abbreviation(folder,"aln;","aln;",r"#--  {- 60};{Home}{Right 4}") #- ahk line -#
engine.create_abbreviation(folder,"ahln;","ahln;",r"#--  {- 30};{Home}{Right 4}	    #- ahk half line -#") #-- Windows Explorer ------------------------------------------------------------#

^F2::		    #- Rename Underline To Space -#
Send,{F2}^c
;StringReplace, clipboard, clipboard, _, %A_SPACE%, All;
Send,^v
return

#IfWinActive ahk_class CabinetWClass

#-- new window operations. prefixed by ^ ------------------------------#
#- create new text file -#
^+m:: ; analogy to ^+n which creates a new folder. French. Depends on installed programs...
Send {Alt Down}f{Alt Up}e{Up 5}<enter>
return

#- current directory path to clipboard -#
^l:: ; analogy to firefox address bar
DirPathToClipboard()
return

#- current file path to clipboard -#
^+l:: ; analogy to firefox address bar
FilePathToClipboard()
return	

#-- open with a program. prefixed by !+ ------------------------------#

!+n:: #- open with Netbeans -#
FilePathToClipboard()
Run,netbeans %clipboard%
return

!+p:: #- open with NotepadPP. (Mainly for scrpits/executables that run by default, since NotepadPP should be your default applicatiot lightweight eddit application.) -#
FilePathToClipboard()
Run,notepad++ %clipboard%
return

;Compress file to .zip
!+z:: ; French.
Send {Shift Down}{F10}{Shift Up}7aa<enter>
return

#- decompress .zip here -#
!+u:: ; French.
Send {Shift Down}{F10}{Shift Up}7{Down 2}<enter>
return

#- decompress .zip to folder -#
!+y:: ; French.
Send {Shift Down}{F10}{Shift Up}7{Down 3}<enter>
return

#IfWinActive

#-- Files, directories, programs ----------------------------------------------#
;
; all end with '\' backslash
;

ToggleWinMinimize(TheWindowTitle)
{
SetTitleMatchMode,2
DetectHiddenWindows, Off
IfWinActive, %TheWindowTitle%
{
   WinMinimize, %TheWindowTitle%
}
Else
{
   IfWinExist, %TheWindowTitle%
   {
     WinGet, winid, ID, %TheWindowTitle%
     DllCall("SwitchToThisWindow", "UInt", winid, "UInt", 1)
   }
}
Return
}

#- If not running, run from path. If running and not focused, give focus. If focused, minimize. -#
#- watch out for windows that change titles, such as text editors. Sometimes a window only has a different title when focused. -#
RunFocusMinTitle(windowTitle,path)
{
SetTitleMatchMode,2
DetectHiddenWindows, Off
IfWinActive,ahk_class %windowTitle%	#- if active, minimize -#
{
   WinMinimize %windowTitle%
}
Else
{
   IfWinExist %windowTitle%	#- if exists, put it on top -#
   {
     WinActivate %windowTitle%
   }
    Else				#- if not running, run it -#
    {
	 Run %path%
    }
}
Return
}

RunFocusMin(AHKClass,path)
{
SetTitleMatchMode,2
DetectHiddenWindows, Off
IfWinActive,ahk_class %AHKClass%	#- if active, minimize -#
{
   WinMinimize,ahk_class %AHKClass%
}
Else
{
   IfWinExist,ahk_class %AHKClass%	#- if exists, put it on top -#
   {
     WinActivate,ahk_class %AHKClass%
   }
    Else				#- if not running, run it -#
    {
	 Run %path%
    }
}
Return

}

#Hotstring * O

#--- run programs --------------------------#
engine.create_abbreviation(folder,"cb\","cb\",r" #- codeblocks -#")RunFocusMinTitle("Code::Blocks 10.05","C:\Program Files (x86)\CodeBlocks\codeblocks.exe")
return

engine.create_abbreviation(folder,"ch\","ch\",r" #- Chrome -#")RunFocusMin("Chrome_WidgetWin_0","C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
return

engine.create_abbreviation(folder,"ec\","ec\",r" #- Eclipse -#")RunFocusMin("SWT_Window0","C:\Program Files (x86)\Eclipse\eclipse.exe")
return

#-- firefox ------------------------------------------------------------#
engine.create_abbreviation(folder,"ff\","ff\",r" #- firefox -#")RunFocusMin("MozillaWindowClass","C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
return

#IfWinActive ahk_class MozillaWindowClass
	
+Rbutton::
	Sleep 1000
	MouseClick, right
	Sleep 1000
	Send, k<enter>
	Sleep 1000
	MouseClick, left
#IfWinActive

engine.create_abbreviation(folder,"mp\","mp\",r" #- Media Player -#")RunFocusMin("WMPlayerApp","C:\Program Files (x86)\Windows Media Player\wmplayer.exe")
return

engine.create_abbreviation(folder,"nb\","nb\",r" #- netbeans -#")RunFocusMin("SunAwtFrame","C:\Program Files (x86)\NetBeans 7.0.1\bin\netbeans.exe")
return

engine.create_abbreviation(folder,"np\","np\",r" #- notepad++ -#")RunFocusMin("Notepad++",notepadpp)
return

engine.create_abbreviation(folder,"npf;","npf;",r" #- notepad++ folder-#")SendRaw,%notepadppf%	#- must use Raw because of the + signs which mean Shift -#
return

engine.create_abbreviation(folder,"npf\","npf\",r" #- notepad++ folder-#")Run %notepadppf%	#- must use Raw because of the + signs which mean Shift -#
return

CurNbFilePathToClipboard()
{
    Send,^s+{F4}
    Sleep, 100
    Click 200, 330
    Sleep, 100
    Send,^a
    Send,^c
    Sleep, 100
    Send,!{F4}
    Return
}

engine.create_abbreviation(folder,"twp\","twp\",r" #- major mouse workaround to get Netbeans Current file path and then do wordpress conversion. uglyy -#")IfWinActive,ahk_class SunAwtFrame 	#- demi check we are in netbeans -#
{
    CurNbFilePathToClipboard()
    run python %elearning%/site-core/wp_markup_conversion.py %clipboard%
}
return

engine.create_abbreviation(folder,"ttt\","ttt\",r" #- To TesT. Do Test Markup Conversion. Put a dummy id on page and go to it. =) Uglyy, and works! -#")IfWinActive,ahk_class SunAwtFrame 	#- demi check we are in netbeans -#
{
    Send,<span id="HERETESTID"/> 	#- put the test id to go to -#
    Sleep, 500
    CurNbFilePathToClipboard()	 	#- put current path on clipboard -#
    Sleep, 500
    run python %elearning%/site-core/test_markup_conversion.py %clipboard%	#- let python do the conversion -#
    Sleep, 1000
    Send,!<tab>		#- remove fake id from source and shift between browser and NB -#
    Sleep, 500    
    Send,{BacSleep, 500
    Send,!<tab>
}
return

engine.create_abbreviation(folder,"npd\","npd\",r" #- note pad -#")RunFocusMin("Notepad","C:\Windows\system32\notepad.exe")
return

#- foxit reader -#
engine.create_abbreviation(folder,"pd\","pd\",r" #- pdf -#")RunFocusMin("classFoxitReader","C:\Program Files (x86)\Foxit Software\Foxit Reader\Foxit Reader.exe")
return

!z::	#- change colors. todo doesnt work -#
IfWinActive,ahk_class classFoxitReader
{
    Send,{Control Down}k{Control Up}{Alt Down}r{Alt Up}<enter>
}
return 


engine.create_abbreviation(folder,"rs\","rs\",r" #- R Statistics -#")RunFocusMinTitle("RGui","C:\Program Files\R\R-2.14.0\bin\i386\Rgui.exe")
return

engine.create_abbreviation(folder,"sk\","sk\",r" #- Skype -#")RunFocusMin("tSkMainForm","C:\Program Files (x86)\Skype\Phone\Skype.exe")
return

engine.create_abbreviation(folder,"wd\","wd\",r" #- word -#")RunFocusMin("OpusApp","C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Word 2007.lnk")
return

#--- /folders --------------------------#
#e:: #- rename Win e -#
    OpenFolder("C:")
return

#+e:: #- drive F -#
    OpenFolder("F:")
return

#d:: #- Desktop -#
    OpenFolder(desktop)
return

engine.create_abbreviation(folder,"dt;","dt;",r" #- Trash -#")SendRaw,%desktop%
return

engine.create_abbreviation(folder,"trs\","trs\",r" #- Trash -#")Run C:\Trash
return

engine.create_abbreviation(folder,"doc\","doc\",r" #- documents -#")Run %documents%
return

#w:: #- Downloads Folder. I use this so often, I put an easier shortcut... -#
	OpenFolder(downloads)
return

engine.create_abbreviation(folder,"dw;","dw;",r" #- Downloads -#")SendRaw,%downloads%
return

engine.create_abbreviation(folder,"pfx\","pfx\",r" #- Program Files x86 -#")OpenFolder(programFilesX86)
return

engine.create_abbreviation(folder,"pfx;","pfx;",r" #- Program Files x86 -#")SendRaw, %programFilesX86%
return

#--- share --------------------------#
engine.create_abbreviation(folder,"shr\","shr\",r" #- share -#")OpenFolder(share)
return

engine.create_abbreviation(folder,"nsh\","nsh\",r" #- no share -#")OpenFolder(noshare)
return

engine.create_abbreviation(folder,"flm\","flm\",r" #- Films -#")OpenFolder(films)
return

engine.create_abbreviation(folder,"game\","game\",r" #- Games -#")OpenFolder(games)
return

engine.create_abbreviation(folder,"img\","img\",r" #- Images -#")OpenFolder(images)
return

#--- music --------------------------#
engine.create_abbreviation(folder,"msc\","msc\",r" #- Music -#")OpenFolder(music)
return

engine.create_abbreviation(folder,"ctm\","ctm\",r" #- Chinese traditional music -#")Run %music%\Chinese Traditional Music.wpl
return

engine.create_abbreviation(folder,"cmpg\","cmpg\",r" #- Chinese traditional music Guqin-#")Run %music%\Chinese Traditional Music\An Anthology of Chinese Traditional and Folk Music - A Collection of Music Played on the Guqin (note=93)\All.wpl
return

engine.create_abbreviation(folder,"jpv\","jpv\",r" #- Joe Pass Virtuoso -#")Run %music%\Playlists\Joe Pass Virtuoso.wpl
return

#--- texts --------------------------#
engine.create_abbreviation(folder,"txt\","txt\",r" #- Texts -#")OpenFolder(texts)
return

engine.create_abbreviation(folder,"mth\","mth\",r" #- Mathematics -#")OpenFolder(mathematics)
return

engine.create_abbreviation(folder,"phy\","phy\",r" #- Physics -#")OpenFolder(physics) 
return

#- noshare -#
engine.create_abbreviation(folder,"nsh\","nsh\",r" #- noshare -#")OpenFolder(noshare)
return

engine.create_abbreviation(folder,"3a\","3a\",r" #- 3A -#")OpenFolder(threeA)
return

::3a;::
	SendRaw,%threeA%
return

engine.create_abbreviation(folder,"ctf\","ctf\",r" #- Certificates -#")OpenFolder(certificates)
return

#-- Programs ------------------------------#
engine.create_abbreviation(folder,"prg\","prg\",r" #- Programs folder -#")OpenFolder(programs)
return

::prg;::
	Send,%programs%
return

engine.create_abbreviation(folder,"ltx\","ltx\",r" #- latex -#")OpenFolder(latex)
return

#-- Python ------------------------------#

engine.create_abbreviation(folder,"py\","py\",r" #- python interpreter -#")Run python
return

engine.create_abbreviation(folder,"pyf\","pyf\",r" #- Python Folder -#")OpenFolder(python)
return

engine.create_abbreviation(folder,"pym\","pym\",r" #- Python Main -#")Run notepad++ %python%\main.py
return

engine.create_abbreviation(folder,"pyrht\","pyrht\",r" #- python interpreter -#")Run %python%\docs\Regex HOW TO.html
return

#--  ------------------------------#
engine.create_abbreviation(folder,"dia\","dia\",r" #- dia -#")Run %autohotkeys%\output.txt
return

engine.create_abbreviation(folder,"dia\","dia\",r" #- dia -#")Run %autohotkeys%\output.txt
return

engine.create_abbreviation(folder,"rsh\","rsh\",r" #- RapidShare folder -#")OpenFolder(rapidshare)
return

#--- Chinese Learning ----------------------------#
engine.create_abbreviation(folder,"cns\","cns\",r" #- chinese learning -#")Run %chinese_learning%
return

engine.create_abbreviation(folder,"cnts\","cnts\",r" #- chinese notes -#")Run notepad++ %noshare%\chinese notes\Chinese notes.txt
return

engine.create_abbreviation(folder,"lic\","lic\",r" #- Latest Interactive Chinese -#")Run %chinese_learning%\Interactive Chinese\Text 6\Text 6.exe
return

engine.create_abbreviation(folder,"cnsl\","cnsl\",r" #- Chinese Learning -#")OpenFolder(chinese_learning)
return

engine.create_abbreviation(folder,"heisig\","heisig\",r" #- Chinese character learning -#")Run %chinese_learning%\Heisig; Richardson - 2009 - Remembering Simplified Hanzi (UHP, 0824833236) note=93.pdf
return

engine.create_abbreviation(folder,"itm\","itm\",r" #- Indian traditional music -#")Run %share%\Music\Indian Traditional Music.wpl
return

#n:: #- notes. I use this so often I will give it a shorter shortcut.n -#
    Run %noshare%\notes.txt
return

#-- site dev ------------------------------#

::xamp\::
Run,C:\xampp\xampp-control.exe
Run,C:\xampp\apache_start.bat
Run,C:\xampp\mysql_start.bat
return

engine.create_abbreviation(folder,"htd\","htd\",r" #- htdocs -#")OpenFolder(htdocs)
return

engine.create_abbreviation(folder,"sde\","sde\",r" #- Site Dev Elearning -#")OpenFolder(elearning)
return

engine.create_abbreviation(folder,"sde;","sde;",r" #- Site Dev Elearning -#")SendRaw,%elearning%
return

engine.create_abbreviation(folder,"sdrsc\","sdrsc\",r" #- Site Dev ReSourCes -#")Run,%elearning%\site-dev\resources.ods
return

#--- scripts ----------------------------#
engine.create_abbreviation(folder,"sic\","sic\",r" #- set ip Ciro -#")Run %noshare%\programs\bat\set ip ciro.bat
return

engine.create_abbreviation(folder,"six\","six\",r" #- set ip Xiaohua -#")Run %noshare%\programs\bat\set ip Xiaohua.bat
return

#--- web sites --------------------------#
engine.create_abbreviation(folder,"mail\","mail\",r"   #- run email -#")Run https://mail.google.com/mail/?hl=fr&shva=1#inbox
return

engine.create_abbreviation(folder,"ftb\","ftb\",r"   #- filestube -#")Run http://www.filestube.com/
return

#Hotstring *0 o0

#--------- Code: c, java, html, etc. ------------------------#
;
; Indentation is complicated because of automatic indententaion which varies from program to program to program.
; I'll mostly put only line breaks and hope for Netbeans automatic indentation
;
#Hotstring * O

#-- general ------------------------------------------------------------#
engine.create_abbreviation(folder,"op;","op;",r"(,){Left 2}") #- ordered pair -#
engine.create_abbreviation(folder,"ot;","ot;",r"(,,){Left 3}") #- ordered triplet -#
engine.create_abbreviation(folder,"bp;","bp;",r"[,]{Left 2}  #- bracket pair -#") #-- Java ------------------------------------------------------------#
engine.create_abbreviation(folder,"jpr;","jpr;",r"System.out.println();{Left 2}") #- Java Pring -#
engine.create_abbreviation(folder,"jfi;","jfi;",r"for(int i=0; i<; i{+}{+}){{}`n`n{}}{Up 2}{End}{Left 7}") #- Java For i -#
engine.create_abbreviation(folder,"jfij;","jfij;",r"for(int i=0; i<; i{+}{+}){{}`nfor(int j=0; j<; j{+}{+}){{}`n`n{}}`n{}}{Up 4}{End}{Left 7}  #- Java For i -#") #-- html/ ----------------------------------------------------------------------#
engine.create_abbreviation(folder,"\html","\html",r"		#- toogle html on off -#")if html = 1
    html = 0
else
    html = 1
return

engine.create_abbreviation(folder,"html;","html;",r"<html><enter><enter></html>{Up}")engine.create_abbreviation(folder,"head;","head;",r"<head><enter><enter></head>{Up}")engine.create_abbreviation(folder,"body;","body;",r"<body><enter><enter></body>{Up}")engine.create_abbreviation(folder,"div;","div;",r"<div class=""></div>{Left 8}")engine.create_abbreviation(folder,"span;","span;",r"<span class=""></span>{Left 9}")engine.create_abbreviation(folder,"h1;","h1;",r"<h1></h1>{Left 5}")engine.create_abbreviation(folder,"h2;","h2;",r"<h2></h2>{Left 5}")engine.create_abbreviation(folder,"h3;","h3;",r"<h3></h3>{Left 5}")engine.create_abbreviation(folder,"h4;","h4;",r"<h4></h4>{Left 5}")engine.create_abbreviation(folder,"h5;","h5;",r"<h5></h5>{Left 5}")engine.create_abbreviation(folder,"h6;","h6;",r"<h6></h6>{Left 5}")engine.create_abbreviation(folder,"h7;","h7;",r"<h7></h7>{Left 5}")engine.create_abbreviation(folder,"h8;","h8;",r"<h8></h8>{Left 5}")engine.create_abbreviation(folder,"h9;","h9;",r"<h9></h9>{Left 5}")engine.create_abbreviation(folder,"ul;","ul;",r"<ul><enter><li></li><enter><li></li><enter></ul>{Up 2}{End}{Left 5}")engine.create_abbreviation(folder,"ulanc;","ulanc;",r"<ul><enter><li><a href="^v"></a></li><enter><li><a href=""></a></li><enter></ul>{Up 2}{Right 3}")engine.create_abbreviation(folder,"ol;","ol;",r"<ol><enter><li></li><enter><li></li><enter></ol>{Up 2}{Right 3}")engine.create_abbreviation(folder,"li;","li;",r"<li></li>{Left 5}")engine.create_abbreviation(folder,"dl;","dl;",r"<dl><enter>    <dt></dt><enter>    <dd></dd><enter>    <dt></dt><enter>    <dd></dd><enter></dl>{Up 4}{Right 3}")engine.create_abbreviation(folder,"dt;","dt;",r"<dt></dt>{Left 5}")engine.create_abbreviation(folder,"dd;","dd;",r"<dd></dd>{Left 5}")engine.create_abbreviation(folder,"dtdd;","dtdd;",r"<dt></dt><enter>    <dd></dd>{Up}{Left 5}")engine.create_abbreviation(folder,"p;","p;",r"<p></p>{Left 4}")engine.create_abbreviation(folder,"pars;","pars;",r"<p class="par-summary"></p>{Left 4}")engine.create_abbreviation(folder,"rap;","rap;",r"</p><enter><p>{Left 3}")engine.create_abbreviation(folder,"prea;","prea;",r"<pre class="ahk"></pre>{Left 6}") #- to display autohotkey code -#

engine.create_abbreviation(folder,"a;","a;",r"<a href="^v"></a>{Left 4}")engine.create_abbreviation(folder,"aid;","aid;",r"<a href="{#}^v"></a>{Left 4}")engine.create_abbreviation(folder,"bq;","bq;",r"<blockquote></blockquote>")engine.create_abbreviation(folder,"img;","img;",r"<div class="image"><enter>    <img src="^v" /><enter>    <div class="img-subtitle"></div><enter></div>")engine.create_abbreviation(folder,"em;","em;",r"<em></em>{Left 5}")engine.create_abbreviation(folder,"str;","str;",r"<strong></strong>{Left 9}")engine.create_abbreviation(folder,"br;","br;",r"<br />")engine.create_abbreviation(folder,"hr;","hr;",r"<hr />")engine.create_abbreviation(folder,"tab;","tab;",r"<div class="table"><enter><table class="vertical"><enter><tr><enter><td></td><enter><td></td><enter></tr><enter><tr><enter><td></td><enter><td></td><enter></tr><enter></table><enter><div class="table-subtitle"></div><enter></div>{Up 9}{Right 8}")engine.create_abbreviation(folder,"tr;","tr;",r"<tr><enter><td></td><enter><td></td><enter></tr>{Up 2}{Right 3}")engine.create_abbreviation(folder,"td;","td;",r"<td></td>{Left 5}");comments
engine.create_abbreviation(folder,"hcm;","hcm;",r"<{!}--  -->{Left 4}") #- Html CoMment -#
engine.create_abbreviation(folder,"habc;","habc;",r"<{!}--  -->{Left 4}<!--added by ciro --><!--/added by ciro -->")engine.create_abbreviation(folder,"todo;","todo;",r"<{!}--todo  -->{Left 4}")engine.create_abbreviation(folder,"todoe;","todoe;",r"<{!}--todo type="example"  -->{Left 4}") #- missing example -#
engine.create_abbreviation(folder,"todol;","todol;",r"<{!}--todo type="link"  -->") #- missing link -#
engine.create_abbreviation(folder,"todoi;","todoi;",r"<{!}--todo type="incomplete"  -->") #- missing information -#
engine.create_abbreviation(folder,"todos;","todos;",r"<{!}--todo type="stub"  -->") #-  -#

engine.create_abbreviation(folder,"mail;","mail;",r"<a href="mailto:^v"></a>{Left 4}")engine.create_abbreviation(folder,"hpp\","hpp\",r"	    #- Html Header Plus Plus. Select, copy, modify! quick and dirty and useful. -#")StringReplace, clipboard, clipboard, <h2>, <h1>, All
StringReplace, clipboard, clipboard, <h3>, <h2>, All
StringReplace, clipboard, clipboard, <h4>, <h3>, All
StringReplace, clipboard, clipboard, <h5>, <h4>, All
StringReplace, clipboard, clipboard, <h6>, <h5>, All

StringReplace, clipboard, clipboard, </h2>, </h1>, All
StringReplace, clipboard, clipboard, </h3>, </h2>, All
StringReplace, clipboard, clipboard, </h4>, </h3>, All
StringReplace, clipboard, clipboard, </h5>, </h4>, All
StringReplace, clipboard, clipboard, </h6>, </h5>, All
return

engine.create_abbreviation(folder,"hmm\","hmm\",r"	    #- Html Header Moins Moins -#")StringReplace, clipboard, clipboard, <h5>, <h6>, All
StringReplace, clipboard, clipboard, <h4>, <h5>, All
StringReplace, clipboard, clipboard, <h3>, <h4>, All
StringReplace, clipboard, clipboard, <h2>, <h3>, All
StringReplace, clipboard, clipboard, <h1>, <h2>, All

StringReplace, clipboard, clipboard, </h5>, </h6>, All
StringReplace, clipboard, clipboard, </h4>, </h5>, All
StringReplace, clipboard, clipboard, </h3>, </h4>, All
StringReplace, clipboard, clipboard, </h2>, </h3>, All
StringReplace, clipboard, clipboard, </h1>, </h2>, All
return

#-- latex and mathematics -----------------------------------------------------#

#-- left alt alternatives ------------------------#

#- right hand -#


<!1::Send,""{Left 1}
<!2::Send,''{Left 1}
<!3::Send,""{Left 1}
<!4::
<!5::

<!q::Send,*
<!w::Send,-
<!e::Send,{+}
<!r::Send,=
<!t::
<!y::

<!a::
<!s::Send,{Space}- `
<!d::Send,{Space}{+} `
<!f::Send,{Space}= `

;<!z::Send,{+}
<!x::Send,''{Left 1}
<!c::Send,""{Left 1}
<!v::Send,""{Left 1}
<!b::Send,=

#- right hand -#

<!u::
<!i::Send,{(}{)}{Left 1}
<!o::Send,{[}{]}{Left 1}
<!p::Send,{{}{}}{Left 1}
<![::Send,{^}{{}{}}{Left 1}	#- latex upper script -#
<!]::

<!g::
<!h::Send,0		#- I put them here because usually for maths 01234 are much more imporant than 56789, specially in subscripts -#
<!j::Send,1
<!k::Send,2
<!l::Send,3
<!;::Send,4
<!'::Send,_{{}{}}{Left 1}	#- latex lower script -#

<!n::Send,5
<!m::Send,6
<!,::Send,7
<!.::Send,8
<!/::Send,9

#-- right alt alternatives - <^>! for the AltGr key -----------------------#
>!w::Send,{Space}-{Space}
>!e::Send,{Space}{+}{Space}
>!r::Send,{Space}={Space}
>!t::Send,{_}{{}{}}{Left 1}


>!u::Send,{^}{{}{}}{Left 1}

#- abbreviation conventions conventions -------------------------------#
; in long expressions
;
; hotstrings end with ';'. very easy place on hand.
;
; one letter numbers
;
; i = Infinity
; o = One
; z = Zero
; t = Two
; h = tHree
; f = Four
; nu = N (n Uppercase)
; q at beginning: == iq\. Ex.: qin => \(\in\)
; m = minus mo = minus one 
;

#- equation delimiers -#
engine.create_abbreviation(folder,"eq;","eq;",r"			#- EQuation. turns off one letter shortcuts -#")Send,<eq></eq>{Left 5}	#-  -#
oneletters = 0
return

::iq;::	
Send,<iq></iq>{Space}{Left 6} #- Internal EQuation. Space so that you write inside then press Home to get out and continue the phrase. -#
oneletters=0
return

engine.create_abbreviation(folder,"eq;","eq;",r"\[\]<left>") 
engine.create_abbreviation(folder,"iq;","iq;",r"$$<left>") 
engine.create_abbreviation(folder,"qi;","qi;",r"\)  \({Left 3}") #- iq reversed. To cut up an eq. -#

#- Subscripts, superscripts -#
engine.create_abbreviation(folder,"sbs;","sbs;",r"{Backspace}{_}{{}{}}{Left 1}") #- SuBScript. Usage: first do a space, then und\. Otherwise cannot separate from last word. -#

#logic
engine.create_abbreviation(folder,"imp;","imp;",r"\implies{Space}")engine.create_abbreviation(folder,"ex;","ex;",r"\exists{Space}")engine.create_abbreviation(folder,"fa;","fa;",r"\forall{Space}")engine.create_abbreviation(folder,"sst;","sst;",r"\subset{Space}")engine.create_abbreviation(folder,"qin;","qin;",r"\(\in\){Space} ;internal iq version when alone");functions
##new functions
engine.create_abbreviation(folder,"fdef;","fdef;",r"\begin{{}align{}}`n\funcDef{{}{}}{{}{}}{{}{}}{{}{}}{{}{}}`n\end{{}align{}}{Up}{End}{Left 9}")engine.create_abbreviation(folder,"fdom;","fdom;",r"\funcDom{{}{}}{{}{}}{{}{}}{Left 5}")engine.create_abbreviation(folder,"comp;","comp;",r"\comp \comp") #- composition of functions -#
engine.create_abbreviation(folder,"argmax;","argmax;",r"\argmax_{{}{}}{Left 1}")engine.create_abbreviation(folder,"argmin;","argmin;",r"\argmin_{}{}}{Left 1}")engine.create_abbreviation(folder,"dom;","dom;",r"Dom(){Left 1}")engine.create_abbreviation(folder,"blt;","blt;",r"\bullet");;elementary functions
engine.create_abbreviation(folder,"frc;","frc;",r"\frac{{}{}}{{}{}}{Left 3}")engine.create_abbreviation(folder,"frco;","frco;",r"\frac{{}1{}}{{}{}}{Left 1}")engine.create_abbreviation(folder,"sqrt;","sqrt;",r"\sqrt{{}{}}{Left 1}")engine.create_abbreviation(folder,"pw;","pw;",r"{Backspace}{^}{{}{}}{Left 1} ;usage: first do a space, then pow\. Otherwise cannot separate from last word.")engine.create_abbreviation(folder,"pwmo;","pwmo;",r"{Backspace}{^}{{}-1{}}")engine.create_abbreviation(folder,"pwt;","pwt;",r"{Backspace}{^}{{}2{}}");analysis
##limits
engine.create_abbreviation(folder,"lim;","lim;",r"\lim_{{} \to {}}{Left 6}")engine.create_abbreviation(folder,"limni;","limni;",r"\lim_{{}n \to \infty{}}")engine.create_abbreviation(folder,"inf;","inf;",r"\infty")engine.create_abbreviation(folder,"der;","der;",r"\der{{}{}}{{}{}}{Left 3}")engine.create_abbreviation(folder,"ddt;","ddt;",r"\der{{}{}}{{}t{}}{Left 4}")engine.create_abbreviation(folder,"ddtatt;","ddtatt;",r"\derAt{{}{}}{{}t{}}{{}{}}{Left 6}")engine.create_abbreviation(folder,"ddtattz;","ddtattz;",r"\derAt{{}{}}{{}t{}}{{}0{}}{Left 7}") #- ddt at t equals -#
engine.create_abbreviation(folder,"ddtatto;","ddtatto;",r"\derAt{{}{}}{{}t{}}{{}1{}}{Left 7}")engine.create_abbreviation(folder,"ddx;","ddx;",r"\der{{}{}}{{}x{}}{Left 4}")engine.create_abbreviation(folder,"ddxatx;","ddxatx;",r"\derAt{{}{}}{{}x{}}{{}{}}{Left 6}")engine.create_abbreviation(folder,"ddxatxz;","ddxatxz;",r"\derAt{{}{}}{{}x{}}{{}0{}}{Left 7}") #- ddx at x equals -#
engine.create_abbreviation(folder,"ddxatxo;","ddxatxo;",r"\derAt{{}{}}{{}x{}}{{}1{}}{Left 7}")engine.create_abbreviation(folder,"parder;","parder;",r"\parDer{{}{}}{{}{}}{Left 3}")engine.create_abbreviation(folder,"nrm;","nrm;",r"\norm{{}{}}{Left 1}")engine.create_abbreviation(folder,"nrmpt;","nrmpt;",r"\norm{{}{}}{^}2{Left 3} ;norm Pow Two")engine.create_abbreviation(folder,"epx;","epx;",r"e^x")engine.create_abbreviation(folder,"ep;","ep;",r"e^")engine.create_abbreviation(folder,"exp;","exp;",r"\exp(){Left 1}")engine.create_abbreviation(folder,"explr;","explr;",r"\exp \left(\right){Left 7}")engine.create_abbreviation(folder,"log;","log;",r"\log(){Left 1}");matrix matrices
##sets of matrices
engine.create_abbreviation(folder,"mn;","mn;",r"\Mn") #-- define \Mn in latex to fix standard. for example, we could have either M(n) or M_n. A mixture of both would be intractable... --#
engine.create_abbreviation(folder,"gln;","gln;",r"\GLn")engine.create_abbreviation(folder,"glnr;","glnr;",r"\GLn(\r)")engine.create_abbreviation(folder,"symn;","symn;",r"\Symn")engine.create_abbreviation(folder,"spdn;","spdn;",r"\SPDn");; matrix functions
engine.create_abbreviation(folder,"det;","det;",r"\det(){Left 1}")engine.create_abbreviation(folder,"trp;","trp;",r"{Backspace}{^}{{}T{}}") #- SuBScript. Usage: first do a space, then und\. Otherwise cannot separate from last word. -#
engine.create_abbreviation(folder,"otrp;","otrp;",r"O{^}{{}T{}}") #- O transpose -#
engine.create_abbreviation(folder,"trc;","trc;",r"\Tr(){Left 1}")
engine.create_abbreviation(folder,"trclr;","trclr;",r"\Tr\left(\right){Left 7}")
engine.create_abbreviation(folder,"pmtx;","pmtx;",r"\begin{{}pmatrix{}}<enter><enter>\end{{}pmatrix{}}{Up}")
## other common notation
engine.create_abbreviation(folder,"lami;","lami;",r"\lambda_i") #- eigen values -#
engine.create_abbreviation(folder,"bmodb;","bmodb;",r"B^{-1}DB") #- diagonalization -#
engine.create_abbreviation(folder,"otr;","otr;",r"O^{T}") #- traspose of an orthogonal matrix = to its inverse -#
engine.create_abbreviation(folder,"otdo;","otdo;",r"O^{T}DO") #- diagonalization of a symmetric matrix -#

##set theory
engine.create_abbreviation(folder,"rq;","rq;",r"\(\r\)")engine.create_abbreviation(folder,"ro;","ro;",r"\r^1")engine.create_abbreviation(folder,"rt;","rt;",r"\r^2")engine.create_abbreviation(folder,"rtq;","rtq;",r"\(\r^2\)")engine.create_abbreviation(folder,"rn;","rn;",r"\mathbb{R}^n")engine.create_abbreviation(folder,"rnq;","rnq;",r"\(\r^n\)")engine.create_abbreviation(folder,"cone;","cone;",r"\c^1")engine.create_abbreviation(folder,"cn;","cn;",r"\c^n")engine.create_abbreviation(folder,"tms;","tms;",r"\times");parenthesis, brackets, etc
engine.create_abbreviation(folder,"lrp;","lrp;",r"\left(\right){Left 7} ;Left Right Parenthesis")engine.create_abbreviation(folder,"lrb;","lrb;",r"\left[\right]{Left 7} ;Brackets")engine.create_abbreviation(folder,"lrc;","lrc;",r"\left{\right}{Left 7} ;braCes (conflict with brackets)");contextless
engine.create_abbreviation(folder,"fx;","fx;",r"f(x)")engine.create_abbreviation(folder,"fxy;","fxy;",r"f(x,y)")engine.create_abbreviation(folder,"foz;","foz;",r"f(z)") #- f Of z -#
engine.create_abbreviation(folder,"fz;","fz;",r"f_0")engine.create_abbreviation(folder,"fo;","fo;",r"f_1")engine.create_abbreviation(folder,"ft;","ft;",r"f_2")engine.create_abbreviation(folder,"gx;","gx;",r"g(x)")engine.create_abbreviation(folder,"hx;","hx;",r"h(x)")engine.create_abbreviation(folder,"fxz;","fxz;",r"f(x_0)")engine.create_abbreviation(folder,"gxy;","gxy;",r"G(x,y)") #- x shortcuts. SO useful -#
engine.create_abbreviation(folder,"xz;","xz;",r"x_0")engine.create_abbreviation(folder,"qxz;","qxz;",r"<iq>x_0</iq>")engine.create_abbreviation(folder,"xoz;","xoz;",r"x(0)") #- x Of Zero -#
engine.create_abbreviation(folder,"xo;","xo;",r"x_1")engine.create_abbreviation(folder,"qxo;","qxo;",r"<iq>x_1</iq>")engine.create_abbreviation(folder,"xoo;","xoo;",r"x(1)") #- x Of One -#
engine.create_abbreviation(folder,"xt;","xt;",r"x_2")engine.create_abbreviation(folder,"qxt;","qxt;",r"<iq>x_2</iq> `")engine.create_abbreviation(folder,"xh;","xh;",r"x_3")engine.create_abbreviation(folder,"qxh;","qxh;",r"<iq>x_3</iq>")engine.create_abbreviation(folder,"xf;","xf;",r"x_4")engine.create_abbreviation(folder,"qxf;","qxf;",r"<iq>x_4</iq>")engine.create_abbreviation(folder,"xof;","xof;",r"x(f)") #- X Of T -#
engine.create_abbreviation(folder,"xi;","xi;",r"x_i") #- X Of T -#
engine.create_abbreviation(folder,"xpt;","xpt;",r"x^2") #- X Pow Two -#
engine.create_abbreviation(folder,"xdot;","xdot;",r"\mathop{x}^{.}")engine.create_abbreviation(folder,"xi;","xi;",r"x_i")engine.create_abbreviation(folder,"qxi;","qxi;",r"<iq>x_i</iq> `")engine.create_abbreviation(folder,"xot;","xot;",r"x(t)") #- X Of T -#

engine.create_abbreviation(folder,"yz;","yz;",r"y_0")engine.create_abbreviation(folder,"yoz;","yoz;",r"y(0)") #- Y Of Zero -#
engine.create_abbreviation(folder,"yo;","yo;",r"y_1")engine.create_abbreviation(folder,"qyo;","qyo;",r"<iq>y_1</iq> `")engine.create_abbreviation(folder,"yoo;","yoo;",r"y(1)") #- y Of One -#
engine.create_abbreviation(folder,"yt;","yt;",r"y_2")engine.create_abbreviation(folder,"qyt;","qyt;",r"<iq>y_2</iq> `")engine.create_abbreviation(folder,"yh;","yh;",r"y_3")engine.create_abbreviation(folder,"qyh;","qyh;",r"<iq>y_3</iq> `")engine.create_abbreviation(folder,"yf;","yf;",r"y_4")engine.create_abbreviation(folder,"qyf;","qyf;",r"<iq>y_4</iq> `")engine.create_abbreviation(folder,"yi;","yi;",r"y_i")engine.create_abbreviation(folder,"qyi;","qyi;",r"<iq>y_i</iq> `")engine.create_abbreviation(folder,"yot;","yot;",r"y(t)") #- Y Of T -#
engine.create_abbreviation(folder,"ypt;","ypt;",r"y^2")engine.create_abbreviation(folder,"yx;","yx;",r"y(x)")engine.create_abbreviation(folder,"ymax;","ymax;",r"y_{max}")engine.create_abbreviation(folder,"yre;","yre;",r"y_{\mathbb{R}}")engine.create_abbreviation(folder,"tz;","tz;",r"t_0")engine.create_abbreviation(folder,"bul;","bul;",r"\bullet") #- bullet -#
engine.create_abbreviation(folder,"bar;","bar;",r"\bar{{}{}}{Left 1}") #- horizontal bar over -#
engine.create_abbreviation(folder,"oln;","oln;",r"\overline{{}{}}{Left 1}") #- overline -#
engine.create_abbreviation(folder,"vec;","vec;",r"\vec{{}{}}{Left 1}") #- vector sign -#
engine.create_abbreviation(folder,"top;","top;",r"\mathtop{{}{}}{{}{}}{Left 3}") #- mathTOP -#
engine.create_abbreviation(folder,"vecz;","vecz;",r"\vec{{}0{}}") #- vector Zero -#
engine.create_abbreviation(folder,"smns;","smns;",r"\setminus") #- set minus -#
engine.create_abbreviation(folder,"cases;","cases;",r"\begin{{}cases{}}`n &  \\`n &`n\end{{}cases{}}{Up 2}{Home}") #- cases-#


engine.create_abbreviation(folder,"oi;","oi;",r"],[{Left 2}") #- open interval -#
engine.create_abbreviation(folder,"ci;","ci;",r"[,]{Left 2}") #- closed interval -#
engine.create_abbreviation(folder,"coi;","coi;",r"[,[{Left 2}") #- closed open interval -#
engine.create_abbreviation(folder,"oci;","oci;",r"],]{Left 2}") #- open closed interval -#

#s=sum z=zero, o=one, i=inf, nu=nuppercase. cryptic, but used SO often...
engine.create_abbreviation(folder,"sum;","sum;",r"\sum_{{}{}}{^}{{}{}}{Left 4}")
engine.create_abbreviation(folder,"sizn;","sizn;",r"\sum_{i=0}^{n}")
engine.create_abbreviation(folder,"sizi;","sizi;",r"\sum_{i=0}^{\infty}")
engine.create_abbreviation(folder,"sion;","sion;",r"\sum_{i=1}^{n}")
engine.create_abbreviation(folder,"sionu;","sionu;",r"\sum_{i=1}^{N}")
engine.create_abbreviation(folder,"sioi;","sioi;",r"\sum_{i=1}^{\infty}")
engine.create_abbreviation(folder,"skoi;","skoi;",r"\sum_{k=1}^{\infty}")
engine.create_abbreviation(folder,"ai;","ai;",r"a_i") #- logic, set theory -#
engine.create_abbreviation(folder,"cprod;","cprod;",r"\cartProd") #- greek letters -#
#Hotstring c
engine.create_abbreviation(folder,"alp;","alp;",r"\alpha")engine.create_abbreviation(folder,"lam;","lam;",r"\lambda")engine.create_abbreviation(folder,"eps;","eps;",r"\epsilon")engine.create_abbreviation(folder,"vphi;","vphi;",r"\varphi")engine.create_abbreviation(folder,"lam;","lam;",r"\lambda")engine.create_abbreviation(folder,"gam;","gam;",r"\gamma")engine.create_abbreviation(folder,"ome;","ome;",r"\omega")engine.create_abbreviation(folder,"omeo;","omeo;",r"\omega_1")engine.create_abbreviation(folder,"omeopt;","omeopt;",r"\omega_1^2") #- Pow Two -#
engine.create_abbreviation(folder,"omet;","omet;",r"\omega_2")engine.create_abbreviation(folder,"ometpt;","ometpt;",r"\omega_2^2") #- Pow Two -#
engine.create_abbreviation(folder,"Ome;","Ome;",r"\Omega") #Hotstring c0

engine.create_abbreviation(folder,"part;","part;",r"\partial") #- ams no library. compatible with ams without any defines. works well on internet for collaborative content -#
engine.create_abbreviation(folder,"re;","re;",r"\mathbb{R}") #- REal numbers -#
engine.create_abbreviation(folder,"ren;","ren;",r"\mathbb{R}^n") #- REal numbers -#
engine.create_abbreviation(folder,"res;","res;",r"\mathbb{R}") #- REal Star -#
engine.create_abbreviation(folder,"rep;","rep;",r"\mathbb{R}_+") #- REal Plus -#
engine.create_abbreviation(folder,"remns;","remns;",r"\mathbb{R}_-") #- REal Minus -#
engine.create_abbreviation(folder,"ire;","ire;",r"\(\mathbb{R}\)")
engine.create_abbreviation(folder,"co;","co;",r"\mathbb{C}") #- comments -#
engine.create_abbreviation(folder,"lcm;","lcm;",r"{%}-  -{%}{Left 3}")
engine.create_abbreviation(folder,"lln;","lln;",r"{%}------------------------------------------------------------------------------{%}") #- latex line -#
engine.create_abbreviation(folder,"lhln;","lhln;",r"{%}---------------------------------------{%} #- latex half line -#") #- for typesetting addicts -#
engine.create_abbreviation(folder,"loremipsum","loremipsum",r"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.") #- latex only, mostly document parts not for latex on javascript web pages. -#
##document parts (good html constructus exist) + 

engine.create_abbreviation(folder,"sec;","sec;",r"\section{{}{}}{Left 1}")engine.create_abbreviation(folder,"seca;","seca;",r"\section{*}{{}{}}{Left 1} ; a for Asterisc")engine.create_abbreviation(folder,"ssec;","ssec;",r"\subsection{{}{}}{Left 1}")engine.create_abbreviation(folder,"sseca;","sseca;",r"\subsection{*}{{}{}}{Left 1}")engine.create_abbreviation(folder,"enum;","enum;",r"\begin{{}enumerate{}}<enter>\item <enter>\item <enter>\end{{}enumerate{}}{Up 2}{End}")engine.create_abbreviation(folder,"itmm;","itmm;",r"\begin{{}itemize{}}<enter>\item <enter>\item <enter>\end{{}itemize{}}{Up 2}{End}") #- ITeMMize -#
engine.create_abbreviation(folder,"desc;","desc;",r"\begin{{}description{}}<enter>\item[]<enter>\item[]<enter>\end{{}description{}}{Up 2}{End}{Left}")engine.create_abbreviation(folder,"ali;","ali;",r"\begin{align}<enter><enter>\end{align}") #- equation align -#

##references (hard in javascrpit html...)
engine.create_abbreviation(folder,"lbl;","lbl;",r"\label{{}{}}{Left 1}")
engine.create_abbreviation(folder,"eqrf;","eqrf;",r"\eqRef{{}{}}{Left 1}")
engine.create_abbreviation(folder,"ref;","ref;",r"\ref{{}{}}{Left 1}")
engine.create_abbreviation(folder,"cite;","cite;",r"\cite{{}{}}{Left 1}") #-- mathematics. html or latex ------------------------------------------------------------#

::def;::
if html = 1
    Send,<div class="definition"><enter><div class="def-title"></div><enter><div class="def-body"><enter><enter></div><enter></div>{Up 4}{End}{Left 6}
else
    Send,\begin{{}definition{}}<enter><enter>\end{{}definition{}}{Up 1}
return

::xpl;::
if html = 1
    Send,<div class="example"><enter><div class="exp-title"></div><enter><div class="exp-body"><enter><enter></div><enter></div>{Up 4}{End}{Left 6}
else
    Send,\begin{{}example{}}<enter><enter>\end{{}example{}}{Up 1}
return

engine.create_abbreviation(folder,"cexp;","cexp;",r"<div class="counter-example"><enter><div class="cexp-title"></div><enter><div class="cexp-body"><enter><enter></div><enter></div>{Up 4}{End}{Left 6}") #- counter example -#
engine.create_abbreviation(folder,"rem;","rem;",r"<div class="remark"><enter><span class="rem-title"></span><enter><div class="rem-body"><enter><enter></div><enter></div>{Up 4}{End}{Left 6}") #- remark -#

::theo;::
if html = 1
    Send,<div class="theorem"><enter><div class="theo-title"></div><enter><div class="theo-body"><enter><div class="theo-hypothesis"><enter><enter></div><enter><div class="theo-conclusions"><enter></div><enter><enter></div><enter><div class="theo-proof"></div><enter></div>{Up 10}{End}{Left 6}
else
    Send,\begin{{}theorem{}}<enter><enter>\end{{}theorem{}}{Up 1}
return

engine.create_abbreviation(folder,"algo;","algo;",r"<div class="algorithm"><enter><div class="algo-title"></div><enter><div class="algo-body"><enter></div><enter></div>{Up 10}{End}{Left 6}") #-- wikipedia markup -----------------------------------------------------------#

engine.create_abbreviation(folder,"wexp;","wexp;",r"<blockquote><strong>Example</strong>`n</blockquote>{Up}{End}") #- example -#

engine.create_abbreviation(folder,"mth;","mth;",r"<math></math>{Left 7}") #- equations -#

engine.create_abbreviation(folder,"wcn;","wcn;",r"{{Citation needed}}") #- citation needed -#
engine.create_abbreviation(folder,"wbf;","wbf;",r"''''{Left 2}") #- Bold Face -#

engine.create_abbreviation(folder,"htw\","htw\",r"	#- html to wikipedia markup. simple substitutions. -#")StringReplace, clipboard, clipboard, \(, <math>, All
	StringReplace, clipboard, clipboard, \[, <math>, All
	StringReplace, clipboard, clipboard, \), </math>, All
	StringReplace, clipboard, clipboard, \], </math>, All
return

#-- c and cpp ------------------------------------------------------------------
engine.create_abbreviation(folder,"i;","i;",r"int `")engine.create_abbreviation(folder,"i;","i;",r"int[]{Left 1}")engine.create_abbreviation(folder,"f;","f;",r"float `")engine.create_abbreviation(folder,"f[;","f[;",r"float[]{Left 1}")engine.create_abbreviation(folder,"d;","d;",r"double `")engine.create_abbreviation(folder,"d[;","d[;",r"double[]{Left 1}")engine.create_abbreviation(folder,"if;","if;",r"if(){{}`n`n{}}{Up 2}{End}{Left 2}")engine.create_abbreviation(folder,"ifel;","ifel;",r"if(){{}`n`n{}} else {{}`n`n{}}{Up 4}{End}{Left 2}")engine.create_abbreviation(folder,"pt;","pt;",r"{Backspace}->") #- Dereference press then pt; -#
engine.create_abbreviation(folder,"tsp;","tsp;",r"this->") #- this with dereference -#

engine.create_abbreviation(folder,"class;","class;",r"class className {<enter>    privateFields;<enter>  public:<enter>    publicFields;}<enter>};<enter><enter>")engine.create_abbreviation(folder,"printf;","printf;",r"printf("%%%",);{Left 6}")engine.create_abbreviation(folder,"cout;","cout;",r"std{:}{:}cout << `")engine.create_abbreviation(folder,"ccm;","ccm;",r"// `") #- c Line Coment -#
engine.create_abbreviation(folder,"cbcm;","cbcm;",r"/*  */{Left 3}") #- c block comment -#
engine.create_abbreviation(folder,"cln;","cln;",r"//--  {- 60}//{Home}{Right 5}") #- ahk line -#
engine.create_abbreviation(folder,"chln;","chln;",r"//--  {- 30}//{Home}{Right 5}	    #- ahk half line -#") #-- python ------------------------------------------------------------#
engine.create_abbreviation(folder,"fori;","fori;",r"for i=1:1000<enter>    <enter>end<enter>")engine.create_abbreviation(folder,"forj;","forj;",r"for j=1:1000<enter>    <enter>end<enter>")engine.create_abbreviation(folder,"pcm;","pcm;",r"{#}-  -{#}{Left 3}")engine.create_abbreviation(folder,"phln;","phln;",r"{#}-  {- 30}{#}{Home}{Right 3}")engine.create_abbreviation(folder,"pln;","pln;",r"{#}-  {- 60}{#}{Home}{Right 3}")engine.create_abbreviation(folder,"pabc;","pabc;",r"{#}- added by ciro -{#}`n`n{#}-/ added by ciro -{#}{Up}") #------------------------------------------------------------------------------
#-- Capslock --  make the keyboard be the way it should be if it had been made for the computer.
;
; this means putting Enter, Arrows, Backspace/Del, cc cv cx, PgUp PgDw, under your hand...
;
; Principles
;
; 1. The load on both hands should be balanced.
; 2. Mostly used characters should be arranged according to these rules in the order of priority:
; a) Index finger > Middle finger > Ring finger > Little finger
; b) Middle row of the keyboard > Upper row > Lower row 
;
; - Home and Del on small finger.
; You never do more than one. Small finger is not good at all for repetitions. 
;
; - Synchronism. We never use {Up}{Down}. But for example {Up 5}{Down}
; and {Up 5}{Up} should come up much more often. So I try to put them in places that
; can be done easily in sequence.
; - different hands. Complete decoupling.
; - different fingers on anatomic position. Index is a great sequence starter.
; 
; 
; 
; - Mnemonics
; The faster you learn the better.
;  - order: aeiou, abcde, 12345.
;  - positional 2D: iklp for up left down right
;  - Mirror hand
;  - Functional. All movement keys on left hand.

#- Reset hotstring recognizer. I could not find a command, besides the z option. -#
ResetAHS()
{
    Suspend off
}

#-- left hand -----------------#
#- number row -#
CapsLock & 1::
if getkeystate("alt") = 0
		Send,^s	    ;save
    else
		Send,!{F4}   ;close window
return

CapsLock & 2::
if getkeystate("alt") = 0
		Send,^f	    ;find
    else
		Send,!{F4}   ;close window
return

CapsLock & 3::
if getkeystate("alt") = 0
		Send,{F2}
    else
		Send,!{F4}   ;close window
return

CapsLock & 4::
if getkeystate("alt") = 0
		Send,^s	    ;save
    else
		Send,!{F4}   ;close window
return

#- upper row -#
CapsLock & q::
if getkeystate("alt") = 0
		Send,^s	    ;save
    else
		Send,!{F4}   ;close window
return

CapsLock & w::
if getkeystate("alt") = 0
		Send ^x
    else
		CutLine()
return

CapsLock & e::
if getkeystate("alt") = 0
		Send ^c
    else
		CopyLine()
return

CapsLock & r::
if getkeystate("alt") = 0
		Send ^v
    else
		DoubleLine()	    #- erase line -#
return	    	

CapsLock & t::		 	   	;eRase

#- middle row -#
CapsLock & a::
if getkeystate("alt") = 0
		DoubleLine()
    else
		ClearLine()	    #- erase line -#
return

CapsLock & s::
    if getkeystate("alt") = 0
		Send,{Del}
    else
		Send,+^{Right}{Del}
return

CapsLock & d::
    if getkeystate("alt") = 0
		Send,{BackSpace}
    else
		ClearLine()
return
    

CapsLock & f::
    if getkeystate("alt") = 0
		Send,<enter>
    else
		Send,<enter>{Up}
return

CapsLock & g::
if getkeystate("alt") = 0
		Send,^f
    else
		Send,^f
return

#- bottom line -#
CapsLock & z::Send ^z
CapsLock & x::Send ^x

CapsLock & c:: 
	if getkeystate("alt") = 0 #- append to clipboard -#
	{
		oldclipboard = %clipboard%
		Send,^c
		Sleep,100
		clipboard = %oldclipboard%%clipboard%
	}
    else	#- clear to clipboard -#
		clipboard := ""
return

CapsLock & v::Send ^v

#-- right hand ------------------
CapsLock & 8::
    Send,{PgUp}
return

CapsLock & 9::
    Send,{PgDn}
return

#- upper row -#
CapsLock & u::
       if getkeystate("alt") = 0
	       Send,^{Right}
       else
	       Send,+^{Right}
return

CapsLock & i::
       if getkeystate("alt") = 0
               Send,{Up}
       else
               Send,+{Up}
return

#- middle row -#
CapsLock & j::
       if getkeystate("alt") = 0
               Send,{Left}
       else
               Send,+{Left}
return

CapsLock & k::
    if getkeystate("alt") = 0
	Send,{Down}
    else
	Send,+{Down}
return

CapsLock & l::
       if getkeystate("alt") = 0
               Send,{Right}
       else
               Send,+{Right}
return

#- bottom row -#
CapsLock & n::			    ;about half a page, slower than Pg
       if getkeystate("alt") = 0
               Send,{Up 15}
       else
               Send,+{Up 15}
return

CapsLock & m::
       if getkeystate("alt") = 0
               Send,{Up 5}
       else
               Send,+{Up 5}	    ;for Netbeans copy line
return

CapsLock & ,::
       if getkeystate("alt") = 0
               Send,{Down 5}   ;I find it more useful to go up with pthe cursor
       else
               Send,+{Down 5}	    ;for Netbeans copy line
return

CapsLock & .::
	if getkeystate("alt") = 0
	    Send,{Down 15}
	else
        Send,+{Down 15}
return

CapsLock & ;::
    if getkeystate("alt") = 0
		Send,{Home}
    else
		Send,^{Home} #- page beginning -#
return

CapsLock & '::
    if getkeystate("alt") = 0
	   Send,{End}
    else
	   Send,^{End} #- page end -#
return

CapsLock & p::
    if getkeystate("alt") = 0
		Send,^{Home}
    else
		Send,^+{Home}
return

CapsLock & [::
    if getkeystate("alt") = 0
	   Send,^{End}
    else
	   Send,^+{End}
return

CapsLock & h::
       if getkeystate("alt") = 0
               Send,^{Left}
       else
               Send,+^{Left}
return

;Prevents CapsState-Shifting
CapsLock & Space::Send,{Space}

#------------------------------------------------------------------------------#
#-- ' (apostrophe) -- just like Capslock, but on the other side.
;

#- escapes -#
'::Send,{'}	    #- make the apostrohpe -#
+'::Send,{"}	    #- make the quotation marks -#

#-- left hand ------------------------#
#- firefox -#

#- upper row -#
' & q::Send,^w	    #- close tab -#
' & w::Send,^l	    #- address bar -#
' & e::Send,^k	    #- google search -#
' & r::Send,^t	    #- new tab -#

#- middle row -#
' & a::Send,^w		#- close tab -#
' & s::Send,^+<tab>	#- left tab -#
' & d::Send,^<tab>	#- right tab -#
' & f::Send,^t		#- new tab -#
' & g::Send,{F5}

#- bottom row -#
' & z::Send,^<tab>	#- right tab -#
' & x::Send,^<tab>	#- right tab -#
' & c::Send,^<tab>	#- right tab -#
' & v::Send,^{Down}	#- Change engine down -#
' & b::Send,^{Up}	#- Change engine up -#

#-- right hand ------------------------#
#- windows -#

#- upper row -#
' & u::Send,^w		
' & i::Send,!{Tab 3}	#- up folder -#
' & o::Send,!{Tab 2}	#- before last page. tap to cycle three latest pages -#
' & p::Send,!<tab>	#- last page -#

#- middle row -#
' & h::Send,^+{Tab 3}
' & j::Send,!{Left}	#- last folder -#
' & k::Send,!{Up}	#- up folder -#
' & l::Send,l		#- dummy-#
' & ;::Send,!{F4}	#- close window -#

#-- Window dragging -----------------------------------------------------------
; Hold alt then click and drag window'
;
; Note: You can optionally release Capslock or the middle mouse button after
; pressing down the mouse button rather than holding it down the whole time.
; This script requires v1.0.25+.

~MButton & LButton::
Alt & LButton::
CoordMode, Mouse  ; Switch to screen/absolute coordinates.
MouseGetPos, EWD_MouseStartX, EWD_MouseStartY, EWD_MouseWin
WinGetPos, EWD_OriginalPosX, EWD_OriginalPosY,,, ahk_id %EWD_MouseWin%
WinGet, EWD_WinState, MinMax, ahk_id %EWD_MouseWin% 
if EWD_WinState = 0  ; Only if the window isn't maximized 
    SetTimer, EWD_WatchMouse, 10 ; Track the mouse as the user drags it.
return

EWD_WatchMouse:
GetKeyState, EWD_LButtonState, LButton, P
if EWD_LButtonState = U  ; Button has been released, so drag is complete.
{
    SetTimer, EWD_WatchMouse, off
    return
}
GetKeyState, EWD_EscapeState, Escape, P
if EWD_EscapeState = D  ; Escape has been pressed, so drag is cancelled.
{
    SetTimer, EWD_WatchMouse, off
    WinMove, ahk_id %EWD_MouseWin%,, %EWD_OriginalPosX%, %EWD_OriginalPosY%
    return
}
; Otherwise, reposition the window to match the change in mouse coordinates
; caused by the user having dragged the mouse:
CoordMode, Mouse
MouseGetPos, EWD_MouseX, EWD_MouseY
WinGetPos, EWD_WinX, EWD_WinY,,, ahk_id %EWD_MouseWin%
SetWinDelay, -1   ; Makes the below move faster/smoother.
WinMove, ahk_id %EWD_MouseWin%,, EWD_WinX + EWD_MouseX - EWD_MouseStartX, EWD_WinY + EWD_MouseY - EWD_MouseStartY
EWD_MouseStartX := EWD_MouseX  ; Update for the next timer-call to this subroutine.
EWD_MouseStartY := EWD_MouseY
return

#-- Easy word adding -----------------------------------------------------------
#h::  ; Win+H hotkey
; Get the text currently selected. The clipboard is used instead of
; "ControlGet Selected" because it works in a greater variety of editors
; (namely word processors).  Save the current clipboard contents to be
; restored later. Although this handles only plain text, it seems better
; than nothing
AutoTrim Off  ; Retain any leading and trailing whitespace on the clipboard.
ClipboardOld = %ClipboardAll%
Clipboard =  ; Must start off blank for detection to work.
Send ^c
ClipWait 1
if ErrorLevel  ; ClipWait timed out.
    return
; Replace CRLF and/or LF with `n for use in a "send-raw" hotstring:
; The same is done for any other characters that might otherwise
; be a problem in raw mode:
StringReplace, Hotstring, Clipboard, ``, ````, All  ; Do this replacement first to avoid interfering with the others below.
StringReplace, Hotstring, Hotstring, <enter>`n, `<enter>, All  ; Using <enter> works better than `n in MS Word, etc.
StringReplace, Hotstring, Hotstring, `n, `<enter>, All
StringReplace, Hotstring, Hotstring, %A_Tab%, ``t, All
StringReplace, Hotstring, Hotstring, ;, ``;, All
Clipboard = %ClipboardOld%  ; Restore previous contents of clipboard.
; This will move the InputBox's caret to a more friendly position:
SetTimer, MoveCaret, 10
; Show the InputBox, providing the default hotstring:
InputBox, Hotstring, New Hotstring, Type your abreviation at the indicated insertion point. You can also edit the replacement text if you wish.`n`nExample entry: :R:btw`::by the way,,,,,,,, :R:`::%Hotstring%
if ErrorLevel  ; The user pressed Cancel.
    return
IfInString, Hotstring, :R`:::
{
    MsgBox You didn't provide an abbreviation. The hotstring has not been added.
    return
}
; Otherwise, add the hotstring and reload the script:
FileAppend, `n%Hotstring%, %A_ScriptFullPath%  ; Put a `n at the beginning in case file lacks a blank line at its end.
Reload
Sleep 200 ; If successful, the reload will close this instance during the Sleep, so the line below will never be reached.
MsgBox, 4,, The hotstring just added appears to be improperly formatted.  Would you like to open the script for editing? Note that the bad hotstring is at the bottom of the script.
IfMsgBox, Yes, Edit
return

MoveCaret:
IfWinNotActive, New Hotstring
    return
; Otherwise, move the InputBox's insertion point to where the user will type the abbreviation.
Send {Home}{Right 3}
SetTimer, MoveCaret, Off
return

#-- English --------------------------------------------------------------------
;
; Hostring Conventions:
; 
; 
;
; 2 letter words are not abbreviated
; 3 letter words -> 1 letter or not
; 4 letter words -> 2 letter, except extremely common ones that are on top of their letters
;
; 3+ syllables:
;
; starting letters - not very maintainable because there are too many conflicts. this is more for magic words that are used very often.
;
; or
;
; first letter of each syllable. less conflicts
;
; or
;
; all consonants. even less conflicts
;
; My philosophy is:
;
; provide a very short potentially conflicting shortcut for the most used words
; provide longer more conflict free shortcuts for less used ones
; provide a longer more standard version for the commonly used ones, in case I forget their punctual cryptic logics
;
;
; 
;
; One of the hotstring plagues of English is that there are too many multiple consonants, which make it difficult to cut by syllable sometimes.
;
; Substitutions
;
; 'qu' always becomes 'q'
; double letters become one letter - aFFirmation -> aFirm
;
;
;
;
; Prefixes
;
; inter	    in
; ex	    x
; trans	    trs	TRANSlate -> trsl
; auto	    au	AUTOmatic
;
;
;
; Suffixes
;
;
;
;
; 
; l	(ajd)	    l	mathematicAL 
; s	(plural)    s	beaches
; s	(he)	    s	he does
; ed	(past)	    d	he planted a tree
; ion	(noun)	    n	coronaiION, visION
; ful	(ajd)	    f	beautiFUL
; ing	()	    g	takING
; ence	(noun)	    c	existENCE 
;

#-------------------------------------------------------------------------------#
#- one letters with toogle button. Better to turn off for equation design, or even latex. -#

engine.create_abbreviation(folder,"ol\","ol\",r"		#- toogle one letter words on off -#")if oneletters = 1
    oneletters = 0
else
    oneletters = 1
return

#IfWinNotActive ahk_class CabinetWClass ;Unbearable for Windows Explorer keyboard navigation

#-------------------------------------------------------------------------------#
#- straight scapes. even if not used, so you  dont have to remember which ones are used or not. -#
engine.create_abbreviation(folder,"a``","a``",r"a")engine.create_abbreviation(folder,"b``","b``",r"b")engine.create_abbreviation(folder,"c``","c``",r"c")engine.create_abbreviation(folder,"d``","d``",r"d")engine.create_abbreviation(folder,"e``","e``",r"e")engine.create_abbreviation(folder,"f``","f``",r"f")engine.create_abbreviation(folder,"g``","g``",r"g")engine.create_abbreviation(folder,"h``","h``",r"h")engine.create_abbreviation(folder,"i``","i``",r"i")engine.create_abbreviation(folder,"j``","j``",r"j")engine.create_abbreviation(folder,"k``","k``",r"k")engine.create_abbreviation(folder,"l``","l``",r"l")engine.create_abbreviation(folder,"m``","m``",r"m")engine.create_abbreviation(folder,"n``","n``",r"n")engine.create_abbreviation(folder,"o``","o``",r"o")engine.create_abbreviation(folder,"p``","p``",r"p")engine.create_abbreviation(folder,"q``","q``",r"q")engine.create_abbreviation(folder,"r``","r``",r"r")engine.create_abbreviation(folder,"s``","s``",r"s")engine.create_abbreviation(folder,"t``","t``",r"t")engine.create_abbreviation(folder,"u``","u``",r"u")engine.create_abbreviation(folder,"v``","v``",r"v")engine.create_abbreviation(folder,"x``","x``",r"x")engine.create_abbreviation(folder,"y``","y``",r"y")engine.create_abbreviation(folder,"z``","z``",r"z")engine.create_abbreviation(folder,"w``","w``",r"w")#Hotstring *0 o0 c	#- capitalization counts -#

#-------------------------------------------------------------------------------#
#- one letter expansions -#
::b::
if oneletters = 1
    Send,but{Space}
else
    Send,b{Space}
return
::B::
if oneletters = 1
    Send,But{Space}
else
    Send,B{Space}
return

::c::
if oneletters = 1
    Send,can{Space}
else
    Send,c{Space}
return
::C::
if oneletters = 1
    Send,Can{Space}
else
    Send,C{Space}
return

::d::
if oneletters = 1
    Send,and{Space}
else
    Send,d{Space}
return
::D::
if oneletters = 1
    Send,And{Space}
else
    Send,D{Space}
return

::f::
if oneletters = 1
    Send,for{Space}
else
    Send,f{Space}
return
::F::
if oneletters = 1
    Send,For{Space}
else
    Send,F{Space}
return

::g::
if oneletters = 1
	Send,get{Space}
else
	Send,g{Space}
return
::G::
if oneletters = 1
	Send,Get{Space}
else
	Send,G{Space}
return

::h::
if oneletters = 1
	Send,has{Space}
else
	Send,h{Space}
return
::H::
if oneletters = 1
	Send,Has{Space}
else
	Send,H{Space}
return

::j::
if oneletters = 1
	Send,just{Space}
else
	Send,j{Space}
return
::J::
if oneletters = 1
	Send,Just{Space}
else
	Send,J{Space}
return

::l::
if oneletters = 1
	Send,let{Space}
else
	Send,l{Space}
return
::L::
if oneletters = 1
	Send,Let{Space}
else
	Send,L{Space}
return

::m::
if oneletters = 1
	Send,make{Space}
else
	Send,m{Space}
return
::M::
if oneletters = 1
	Send,Make{Space}
else
	Send,M{Space}
return

::n::
if oneletters = 1
	Send,not{Space}
else
	Send,n{Space}
return
::N::
if oneletters = 1
	Send,Not{Space}
else
	Send,N{Space}
return

::p::
if oneletters = 1
	Send,put{Space}
else
	Send,p{Space}
return
::P::
if oneletters = 1
	Send,Put{Space}
else
	Send,P{Space}
return

::q::
if oneletters = 1
	Send,question{Space}
else
	Send,q{Space}
return
::Q::
if oneletters = 1
	Send,Question{Space}
else
	Send,Q{Space}
return

::r::
if oneletters = 1
	Send,are{Space}
else
	Send,r{Space}
return
::R::
if oneletters = 1
	Send,Are{Space}
else
	Send,R{Space}
return

::s::
if oneletters = 1
	Send,see{Space}
else
	Send,s{Space}
return
::S::
if oneletters = 1
	Send,See{Space}
else
	Send,S{Space}
return

::t::
if oneletters = 1
	Send,the{Space}
else
	Send,t{Space}
return
::T::
if oneletters = 1
	Send,The{Space}
else
	Send,T{Space}
return

::u::
if oneletters = 1
	Send,use{Space}
else
	Send,u{Space}
return
::U::
if oneletters = 1
	Send,Use{Space}
else
	Send,U{Space}
return

::v::
if oneletters = 1
	Send,very{Space}
else
	Send,v{Space}
return
::V::
if oneletters = 1
	Send,Very{Space}
else
	Send,V{Space}
return

::y::
if oneletters = 1
	Send,you{Space}
else
	Send,y{Space}
return
::Y::
if oneletters = 1
	Send,You{Space}
else
	Send,Y{Space}
return
 
::w::
if oneletters = 1
	Send,with{Space}
else
	Send,w{Space}
return
::W::
if oneletters = 1
	Send,With{Space}
else
	Send,W{Space}
return

#Hotstring c0
#IfWinNotActive

;more than one letter

engine.create_abbreviation(folder,"ab","ab",r"about")engine.create_abbreviation(folder,"af","af",r"after")engine.create_abbreviation(folder,"ag","ag",r"again")engine.create_abbreviation(folder,"im","im",r"I'm")engine.create_abbreviation(folder,"ag","ag",r"again")engine.create_abbreviation(folder,"alo","alo",r"along")engine.create_abbreviation(folder,"al","al",r"also")engine.create_abbreviation(folder,"ano","ano",r"another")engine.create_abbreviation(folder,"ar","ar",r"around")engine.create_abbreviation(folder,"aw","aw",r"away")engine.create_abbreviation(folder,"ba","ba",r"back")engine.create_abbreviation(folder,"bc","bc",r"because")engine.create_abbreviation(folder,"bn","bn",r"been")engine.create_abbreviation(folder,"bf","bf",r"before")engine.create_abbreviation(folder,"bl","bl",r"below")engine.create_abbreviation(folder,"bt","bt",r"between")engine.create_abbreviation(folder,"bo","bo",r"both")engine.create_abbreviation(folder,"ca","ca",r"came")engine.create_abbreviation(folder,"cm","cm",r"come")engine.create_abbreviation(folder,"cd","cd",r"could")engine.create_abbreviation(folder,"dy","dy",r"day")engine.create_abbreviation(folder,"dd","dd",r"did")engine.create_abbreviation(folder,"df","df",r"different")engine.create_abbreviation(folder,"ds","ds",r"does")engine.create_abbreviation(folder,"dt","dt",r"don't")engine.create_abbreviation(folder,"dw","dw",r"down")engine.create_abbreviation(folder,"ea","ea",r"each")engine.create_abbreviation(folder,"en","en",r"even")engine.create_abbreviation(folder,"ev","ev",r"every")engine.create_abbreviation(folder,"fi","fi",r"find")engine.create_abbreviation(folder,"ft","ft",r"first")engine.create_abbreviation(folder,"fd","fd",r"found")engine.create_abbreviation(folder,"fr","fr",r"from")engine.create_abbreviation(folder,"dst","dst",r"doesn't")engine.create_abbreviation(folder,"gv","gv",r"give")engine.create_abbreviation(folder,"gd","gd",r"good")engine.create_abbreviation(folder,"gr","gr",r"great")engine.create_abbreviation(folder,"hv","hv",r"have")engine.create_abbreviation(folder,"hp","hp",r"help")engine.create_abbreviation(folder,"hr","hr",r"here")engine.create_abbreviation(folder,"hv","hv",r"have")engine.create_abbreviation(folder,"hl","hl",r"help")engine.create_abbreviation(folder,"hr","hr",r"here")engine.create_abbreviation(folder,"hm","hm",r"home")engine.create_abbreviation(folder,"hou","hou",r"house")engine.create_abbreviation(folder,"ju","ju",r"just")engine.create_abbreviation(folder,"kn","kn",r"know")engine.create_abbreviation(folder,"lr","lr",r"large")engine.create_abbreviation(folder,"ls","ls",r"last")engine.create_abbreviation(folder,"lf","lf",r"left")engine.create_abbreviation(folder,"lk","lk",r"like")engine.create_abbreviation(folder,"ln","ln",r"line")engine.create_abbreviation(folder,"lt","lt",r"little")engine.create_abbreviation(folder,"lg","lg",r"long")engine.create_abbreviation(folder,"lo","lo",r"look")engine.create_abbreviation(folder,"md","md",r"made")engine.create_abbreviation(folder,"mk","mk",r"make")engine.create_abbreviation(folder,"mn","mn",r"many")engine.create_abbreviation(folder,"mg","mg",r"might")engine.create_abbreviation(folder,"mr","mr",r"more")engine.create_abbreviation(folder,"ms","ms",r"most")engine.create_abbreviation(folder,"mr.","mr.",r"Mr.")engine.create_abbreviation(folder,"mu","mu",r"must")engine.create_abbreviation(folder,"nm","nm",r"name")engine.create_abbreviation(folder,"nv","nv",r"never")engine.create_abbreviation(folder,"nx","nx",r"next")engine.create_abbreviation(folder,"nt","nt",r"note")engine.create_abbreviation(folder,"nw","nw",r"now")engine.create_abbreviation(folder,"nm","nm",r"number")engine.create_abbreviation(folder,"oy","oy",r"only")engine.create_abbreviation(folder,"ot","ot",r"other")engine.create_abbreviation(folder,"ou","ou",r"our")engine.create_abbreviation(folder,"ot","ot",r"out")engine.create_abbreviation(folder,"ov","ov",r"over")engine.create_abbreviation(folder,"ow","ow",r"own")engine.create_abbreviation(folder,"pp","pp",r"people")engine.create_abbreviation(folder,"pl","pl",r"place")engine.create_abbreviation(folder,"rd","rd",r"read")engine.create_abbreviation(folder,"rg","rg",r"right")engine.create_abbreviation(folder,"sd","sd",r"said")engine.create_abbreviation(folder,"sa","sa",r"same ;avoid conflict with some (so exists already)")engine.create_abbreviation(folder,"sy","sy",r"say")engine.create_abbreviation(folder,"se","se",r"seen so")engine.create_abbreviation(folder,"sh","sh",r"should")engine.create_abbreviation(folder,"sw","sw",r"show")engine.create_abbreviation(folder,"sl","sl",r"small")engine.create_abbreviation(folder,"sm","sm",r"some")engine.create_abbreviation(folder,"smt","smt",r"something")engine.create_abbreviation(folder,"snd","snd",r"sound")engine.create_abbreviation(folder,"st","st",r"still")engine.create_abbreviation(folder,"su","su",r"such")engine.create_abbreviation(folder,"tk","tk",r"take")engine.create_abbreviation(folder,"tl","tl",r"tell")engine.create_abbreviation(folder,"th","th",r"than")engine.create_abbreviation(folder,"tt","tt",r"that")engine.create_abbreviation(folder,"tm","tm",r"them")engine.create_abbreviation(folder,"tn","tn",r"then")engine.create_abbreviation(folder,"tr","tr",r"there")engine.create_abbreviation(folder,"ths","ths",r"these")engine.create_abbreviation(folder,"ty","ty",r"they")engine.create_abbreviation(folder,"tg","tg",r"thing")engine.create_abbreviation(folder,"tk","tk",r"think")engine.create_abbreviation(folder,"ts","ts",r"this")engine.create_abbreviation(folder,"ths","ths",r"those")engine.create_abbreviation(folder,"thg","thg",r"thought")engine.create_abbreviation(folder,"thr","thr",r"three")engine.create_abbreviation(folder,"thg","thg",r"through")engine.create_abbreviation(folder,"tm","tm",r"time")engine.create_abbreviation(folder,"tg","tg",r"together")engine.create_abbreviation(folder,"tw","tw",r"two")engine.create_abbreviation(folder,"un","un",r"under")engine.create_abbreviation(folder,"vr","vr",r"very")engine.create_abbreviation(folder,"wt","wt",r"want")engine.create_abbreviation(folder,"wtr","wtr",r"water")engine.create_abbreviation(folder,"wy","wy",r"way")engine.create_abbreviation(folder,"wel","wel",r"well")engine.create_abbreviation(folder,"wa","wa",r"what")engine.create_abbreviation(folder,"wn","wn",r"when")engine.create_abbreviation(folder,"wr","wr",r"where")engine.create_abbreviation(folder,"whc","whc",r"which")engine.create_abbreviation(folder,"whl","whl",r"while")engine.create_abbreviation(folder,"wl","wl",r"will")engine.create_abbreviation(folder,"wi","wi",r"with")engine.create_abbreviation(folder,"wk","wk",r"work")engine.create_abbreviation(folder,"wd","wd",r"word")engine.create_abbreviation(folder,"wrl","wrl",r"world")engine.create_abbreviation(folder,"wu","wu",r"would")engine.create_abbreviation(folder,"wrt","wrt",r"write")engine.create_abbreviation(folder,"ye","ye",r"year")engine.create_abbreviation(folder,"yo","yo",r"your")engine.create_abbreviation(folder,"ws","ws",r"was")engine.create_abbreviation(folder,"typ","typ",r"type")engine.create_abbreviation(folder,"fr","fr",r"fr")engine.create_abbreviation(folder,"from","from",r"from")engine.create_abbreviation(folder,"jq","jq",r"jquery")engine.create_abbreviation(folder,"mj","mj",r"MathJax")engine.create_abbreviation(folder,"rdm","rdm",r"README")engine.create_abbreviation(folder,"xtns","xtns",r"extensions")engine.create_abbreviation(folder,"thm","thm",r"themes")engine.create_abbreviation(folder,"cntt","cntt",r"content")engine.create_abbreviation(folder,"lch","lch",r"localhost")engine.create_abbreviation(folder,"mth","mth",r"mathematics")engine.create_abbreviation(folder,"cls","cls",r"class")engine.create_abbreviation(folder,"sty","sty",r"style")engine.create_abbreviation(folder,"blg","blg",r"blog")engine.create_abbreviation(folder,"dft","dft",r"default")engine.create_abbreviation(folder,"btf","btf",r"beautiful")engine.create_abbreviation(folder,"cmm","cmm",r"common")engine.create_abbreviation(folder,"func","func",r"function")engine.create_abbreviation(folder,"cntn","cntn",r"continuous")engine.create_abbreviation(folder,"prtl","prtl",r"partial")engine.create_abbreviation(folder,"interv","interv",r"interval")engine.create_abbreviation(folder,"interpr","interpr",r"interpretation")engine.create_abbreviation(folder,"intui","intui",r"intuitive")engine.create_abbreviation(folder,"vsl","vsl",r"visual")engine.create_abbreviation(folder,"symboy","symboy",r"symbolically")engine.create_abbreviation(folder,"cont","cont",r"continuous")engine.create_abbreviation(folder,"ltt","ltt",r"little")engine.create_abbreviation(folder,"aro","aro",r"around")engine.create_abbreviation(folder,"tn","tn",r"then")engine.create_abbreviation(folder,"symbc","symbc",r"symbolic")engine.create_abbreviation(folder,"sml","sml",r"small")engine.create_abbreviation(folder,"eno","eno",r"enough")engine.create_abbreviation(folder,"pnt","pnt",r"point")engine.create_abbreviation(folder,"stl","stl",r"still")engine.create_abbreviation(folder,"bcms","bcms",r"becomes")engine.create_abbreviation(folder,"clr","clr",r"clear")engine.create_abbreviation(folder,"nd","nd",r"need")engine.create_abbreviation(folder,"hyp","hyp",r"hypothesis")engine.create_abbreviation(folder,"kp","kp",r"keep")engine.create_abbreviation(folder,"crs","crs",r"course")engine.create_abbreviation(folder,"adjus","adjus",r"adjustment")engine.create_abbreviation(folder,"whc","whc",r"which")engine.create_abbreviation(folder,"kps","kps",r"keeps")engine.create_abbreviation(folder,"vl","vl",r"value")engine.create_abbreviation(folder,"mgt","mgt",r"might")engine.create_abbreviation(folder,"xpc","xpc",r"expect")engine.create_abbreviation(folder,"varn","varn",r"variation")engine.create_abbreviation(folder,"hypothesis","hypothesis",r"hypothesis")engine.create_abbreviation(folder,"hd","hd",r"hard")engine.create_abbreviation(folder,"eff","eff",r"effect")engine.create_abbreviation(folder,"cnn","cnn",r"cannot")engine.create_abbreviation(folder,"lrg","lrg",r"large")engine.create_abbreviation(folder,"hwv","hwv",r"however")engine.create_abbreviation(folder,"corre","corre",r"correction")engine.create_abbreviation(folder,"wkg","wkg",r"working")engine.create_abbreviation(folder,"visu","visu",r"visualize")engine.create_abbreviation(folder,"ins","ins",r"inside")engine.create_abbreviation(folder,"rly","rly",r"really")engine.create_abbreviation(folder,"spl","spl",r"simple")engine.create_abbreviation(folder,"splr","splr",r"simpler")engine.create_abbreviation(folder,"effv","effv",r"effective")engine.create_abbreviation(folder,"rsn","rsn",r"reason")engine.create_abbreviation(folder,"hap","hap",r"happy")engine.create_abbreviation(folder,"tch","tch",r"teach")engine.create_abbreviation(folder,"ots","ots",r"others")engine.create_abbreviation(folder,"evt","evt",r"everything")engine.create_abbreviation(folder,"cmpl","cmpl",r"complete")engine.create_abbreviation(folder,"cmply","cmply",r"completely")engine.create_abbreviation(folder,"ao","ao",r"anyone")engine.create_abbreviation(folder,"knl","knl",r"knowledge")engine.create_abbreviation(folder,"shld","shld",r"should")engine.create_abbreviation(folder,"fl","fl",r"feel")engine.create_abbreviation(folder,"pls","pls",r"please")engine.create_abbreviation(folder,"tchg","tchg",r"teaching")engine.create_abbreviation(folder,"expsv","expsv",r"expensive")engine.create_abbreviation(folder,"tog","tog",r"together")engine.create_abbreviation(folder,"thrf","thrf",r"Therefore")engine.create_abbreviation(folder,"alr","alr",r"already")engine.create_abbreviation(folder,"src","src",r"source")engine.create_abbreviation(folder,"rth","rth",r"rather")engine.create_abbreviation(folder,"si","si",r"site")engine.create_abbreviation(folder,"cmplxy","cmplxy",r"complexities")engine.create_abbreviation(folder,"blv","blv",r"believe")engine.create_abbreviation(folder,"au","au",r"author")engine.create_abbreviation(folder,"fc","fc",r"focus")engine.create_abbreviation(folder,"phy","phy",r"physics")engine.create_abbreviation(folder,"shd","shd",r"should")engine.create_abbreviation(folder,"lrn","lrn",r"learn")engine.create_abbreviation(folder,"mat","mat",r"material")engine.create_abbreviation(folder,"cp","cp",r"cope")engine.create_abbreviation(folder,"ct","ct",r"cost")engine.create_abbreviation(folder,"tchg","tchg",r"teaching")engine.create_abbreviation(folder,"cms","cms",r"comes")engine.create_abbreviation(folder,"smw","smw",r"somewhat")engine.create_abbreviation(folder,"oft","oft",r"often")engine.create_abbreviation(folder,"wio","wio",r"without")engine.create_abbreviation(folder,"coop","coop",r"cooperation")engine.create_abbreviation(folder,"abv","abv",r"above")engine.create_abbreviation(folder,"tgs","tgs",r"things")engine.create_abbreviation(folder,"cent","cent",r"centuries")engine.create_abbreviation(folder,"yrs","yrs",r"years")engine.create_abbreviation(folder,"mks","mks",r"makes")engine.create_abbreviation(folder,"hs","hs",r"has")engine.create_abbreviation(folder,"spc","spc",r"space")engine.create_abbreviation(folder,"ltr","ltr",r"letter")engine.create_abbreviation(folder,"thrg","thrg",r"through")engine.create_abbreviation(folder,"inet","inet",r"internet")engine.create_abbreviation(folder,"thgt","thgt",r"thought")engine.create_abbreviation(folder,"thgts","thgts",r"thoughts")engine.create_abbreviation(folder,"pnts","pnts",r"points")engine.create_abbreviation(folder,"spey","spey",r"specially")engine.create_abbreviation(folder,"mc","mc",r"much")engine.create_abbreviation(folder,"moti","moti",r"motivation")engine.create_abbreviation(folder,"lrng","lrng",r"learning")engine.create_abbreviation(folder,"bcms","bcms",r"becomes")engine.create_abbreviation(folder,"dfc","dfc",r"difficult")engine.create_abbreviation(folder,"motid","motid",r"motivated")engine.create_abbreviation(folder,"oblid","oblid",r"obliged")engine.create_abbreviation(folder,"fcs","fcs",r"focus")engine.create_abbreviation(folder,"srcs","srcs",r"sources")engine.create_abbreviation(folder,"prb","prb",r"problem")engine.create_abbreviation(folder,"dgt","dgt",r"digital")engine.create_abbreviation(folder,"mtd","mtd",r"method")engine.create_abbreviation(folder,"tms","tms",r"times")engine.create_abbreviation(folder,"aml","aml",r"almost")engine.create_abbreviation(folder,"zr","zr",r"zero")engine.create_abbreviation(folder,"cmpts","cmpts",r"Computers")engine.create_abbreviation(folder,"emph","emph",r"emphasis")engine.create_abbreviation(folder,"comp","comp",r"computer")engine.create_abbreviation(folder,"xp","xp",r"example")engine.create_abbreviation(folder,"tchrs","tchrs",r"teachers")engine.create_abbreviation(folder,"btr","btr",r"better")engine.create_abbreviation(folder,"fls","fls",r"flash")engine.create_abbreviation(folder,"wc","wc",r"which")engine.create_abbreviation(folder,"manip","manip",r"manipulate")engine.create_abbreviation(folder,"distrd","distrd",r"distributed")engine.create_abbreviation(folder,"possibs","possibs",r"possibilities")engine.create_abbreviation(folder,"eit","eit",r"either")engine.create_abbreviation(folder,"smpy","smpy",r"simply")engine.create_abbreviation(folder,"refs","refs",r"references")engine.create_abbreviation(folder,"explic","explic",r"explication")engine.create_abbreviation(folder,"td","td",r"to do")engine.create_abbreviation(folder,"comps","comps",r"computers")engine.create_abbreviation(folder,"qsts","qsts",r"questions")engine.create_abbreviation(folder,"math","math",r"mathematics")engine.create_abbreviation(folder,"adv","adv",r"advanced")engine.create_abbreviation(folder,"mt","mt",r"most")engine.create_abbreviation(folder,"cs","cs",r"case")engine.create_abbreviation(folder,"spcf","spcf",r"specify")engine.create_abbreviation(folder,"spcfc","spcfc",r"specific")engine.create_abbreviation(folder,"def","def",r"define")engine.create_abbreviation(folder,"dervs","dervs",r"derivatives")engine.create_abbreviation(folder,"ans","ans",r"answer")engine.create_abbreviation(folder,"trf","trf",r"therefore")engine.create_abbreviation(folder,"cnt","cnt",r"center")engine.create_abbreviation(folder,"img","img",r"image")engine.create_abbreviation(folder,"parab","parab",r"parabolic")engine.create_abbreviation(folder,"prbc","prbc",r"parabolic")engine.create_abbreviation(folder,"exps","exps",r"examples")engine.create_abbreviation(folder,"mtrs","mtrs",r"matters")engine.create_abbreviation(folder,"cncr","cncr",r"concrete")engine.create_abbreviation(folder,"sps","sps",r"suppose")engine.create_abbreviation(folder,"pln","pln",r"plane")engine.create_abbreviation(folder,"eqs","eqs",r"equals")engine.create_abbreviation(folder,"alw","alw",r"always")engine.create_abbreviation(folder,"gxy","gxy",r"G(x,y)")engine.create_abbreviation(folder,"adj","adj",r"adjustment")engine.create_abbreviation(folder,"nc","nc",r"nice")engine.create_abbreviation(folder,"frtm","frtm",r"furthermore")engine.create_abbreviation(folder,"crr","crr",r"correct")engine.create_abbreviation(folder,"crrn","crrn",r"correction")engine.create_abbreviation(folder,"lts","lts",r"let's")engine.create_abbreviation(folder,"crc","crc",r"circle")engine.create_abbreviation(folder,"otoh","otoh",r"on the other hand")engine.create_abbreviation(folder,"sv","sv",r"save")engine.create_abbreviation(folder,"xpl","xpl",r"explicit")engine.create_abbreviation(folder,"qst","qst",r"question")engine.create_abbreviation(folder,"mjry","mjry",r"majority")engine.create_abbreviation(folder,"funcs","funcs",r"functions")engine.create_abbreviation(folder,"tho","tho",r"those")engine.create_abbreviation(folder,"usf","usf",r"useful")engine.create_abbreviation(folder,"xsts","xsts",r"exists")engine.create_abbreviation(folder,"xstc","xstc",r"existence")engine.create_abbreviation(folder,"ppts","ppts",r"properties")engine.create_abbreviation(folder,"cld","cld",r"called")engine.create_abbreviation(folder,"impl","impl",r"implicit")engine.create_abbreviation(folder,"xcty","xcty",r"exactly")engine.create_abbreviation(folder,"polyn","polyn",r"polynomial")engine.create_abbreviation(folder,"sc","sc",r"since")engine.create_abbreviation(folder,"slv","slv",r"solve")engine.create_abbreviation(folder,"dsr","dsr",r"desire")engine.create_abbreviation(folder,"ptcly","ptcly",r"Particularly")engine.create_abbreviation(folder,"vrat","vrat",r"variation")engine.create_abbreviation(folder,"sol","sol",r"solution")engine.create_abbreviation(folder,"shl","shl",r"shall")engine.create_abbreviation(folder,"mtvtn","mtvtn",r"Motivation")engine.create_abbreviation(folder,"tft","tft",r"the fact that")engine.create_abbreviation(folder,"iltts","iltts",r"illustrates")engine.create_abbreviation(folder,"gvs","gvs",r"gives")engine.create_abbreviation(folder,"rglry","rglry",r"regularity")engine.create_abbreviation(folder,"rt","rt",r"rather")engine.create_abbreviation(folder,"res","res",r"result")engine.create_abbreviation(folder,"wv","wv",r"we've")engine.create_abbreviation(folder,"enj","enj",r"enjoy")engine.create_abbreviation(folder,"kng","kng",r"knowing")engine.create_abbreviation(folder,"hstt","hstt",r"hesitate")engine.create_abbreviation(folder,"sggn","sggn",r"suggestion")engine.create_abbreviation(folder,"prt","prt",r"print")engine.create_abbreviation(folder,"psb","psb",r"possible")engine.create_abbreviation(folder,"correction","correction",r"correction")engine.create_abbreviation(folder,"intv","intv",r"interval")engine.create_abbreviation(folder,"rst","rst",r"result")engine.create_abbreviation(folder,"ocs","ocs",r"of course")engine.create_abbreviation(folder,"xmn","xmn",r"examine")engine.create_abbreviation(folder,"hpns","hpns",r"happens")engine.create_abbreviation(folder,"pg","pg",r"page")engine.create_abbreviation(folder,"lcp","lcp",r"landscape")engine.create_abbreviation(folder,"cds","cds",r"Ciro Duran Santilli")engine.create_abbreviation(folder,"ttrl","ttrl",r"tutorial")engine.create_abbreviation(folder,"clsn","clsn",r"collision")engine.create_abbreviation(folder,"tkn","tkn",r"taken")engine.create_abbreviation(folder,"gpcs","gpcs",r"graphics")engine.create_abbreviation(folder,"spd","spd",r"speed")engine.create_abbreviation(folder,"evrm","evrm",r"environment")engine.create_abbreviation(folder,"fx","fx",r"for example")engine.create_abbreviation(folder,"inp","inp",r"input")engine.create_abbreviation(folder,"ahk","ahk",r"autohotkey")engine.create_abbreviation(folder,"cmr","cmr",r"camera")engine.create_abbreviation(folder,"pt","pt",r"part")engine.create_abbreviation(folder,"rbt","rbt",r"robot")engine.create_abbreviation(folder,"opt","opt",r"output")engine.create_abbreviation(folder,"sta","sta",r"start")engine.create_abbreviation(folder,"scs","scs",r"showcase")engine.create_abbreviation(folder,"fdtns","fdtns",r"foundations")engine.create_abbreviation(folder,"fdmt","fdmt",r"fundamental")engine.create_abbreviation(folder,"fie","fie",r"field")engine.create_abbreviation(folder,"qs","qs",r"questions")engine.create_abbreviation(folder,"isf","isf",r"itself")engine.create_abbreviation(folder,"ress","ress",r"results")engine.create_abbreviation(folder,"incl","incl",r"include")engine.create_abbreviation(folder,"sua","sua",r"such as")engine.create_abbreviation(folder,"perh","perh",r"Perhaps")engine.create_abbreviation(folder,"abrn","abrn",r"abbreviation")engine.create_abbreviation(folder,"ld","ld",r"lead")engine.create_abbreviation(folder,"bcm","bcm",r"become")engine.create_abbreviation(folder,"abrd","abrd",r"abbreviated")engine.create_abbreviation(folder,"o","o",r"one")engine.create_abbreviation(folder,"dmnt","dmnt",r"dominate")engine.create_abbreviation(folder,"dmntg","dmntg",r"dominating")engine.create_abbreviation(folder,"stag","stag",r"starting")engine.create_abbreviation(folder,"tx","tx",r"text")engine.create_abbreviation(folder,"col","col",r"color")engine.create_abbreviation(folder,"ei","ei",r"either")engine.create_abbreviation(folder,"ddn","ddn",r"did not")engine.create_abbreviation(folder,"ppsn","ppsn",r"proposition")engine.create_abbreviation(folder,"diff","diff",r"difficult")engine.create_abbreviation(folder,"dif","dif",r"difficult")engine.create_abbreviation(folder,"prv","prv",r"prove")engine.create_abbreviation(folder,"intun","intun",r"intuition")engine.create_abbreviation(folder,"oc","oc",r"once")engine.create_abbreviation(folder,"ey","ey",r"easy")engine.create_abbreviation(folder,"esl","esl",r"easily")engine.create_abbreviation(folder,"sci","sci",r"science")engine.create_abbreviation(folder,"ftr","ftr",r"future")engine.create_abbreviation(folder,"dn","dn",r"done")engine.create_abbreviation(folder,"lang","lang",r"language")engine.create_abbreviation(folder,"mthl","mthl",r"mathematical")engine.create_abbreviation(folder,"args","args",r"arguments")engine.create_abbreviation(folder,"che","che",r"check")engine.create_abbreviation(folder,"fml","fml",r"formal")engine.create_abbreviation(folder,"prcsy","prcsy",r"precisely")engine.create_abbreviation(folder,"ambig","ambig",r"ambiguity")engine.create_abbreviation(folder,"gtr","gtr",r"guitar")engine.create_abbreviation(folder,"sys","sys",r"system")engine.create_abbreviation(folder,"mathematical","mathematical",r"mathematical")engine.create_abbreviation(folder,"op","op",r"open")engine.create_abbreviation(folder,"uni","uni",r"university")engine.create_abbreviation(folder,"ta","ta",r"than")engine.create_abbreviation(folder,"wo","wo",r"without")engine.create_abbreviation(folder,"csfctn","csfctn",r"classification")engine.create_abbreviation(folder,"clod","clod",r"closed")engine.create_abbreviation(folder,"sfcs","sfcs",r"surfaces")engine.create_abbreviation(folder,"ed","ed",r"edit")engine.create_abbreviation(folder,"scr","scr",r"script")engine.create_abbreviation(folder,"scrs","scrs",r"scripts")engine.create_abbreviation(folder,"hstr","hstr",r"hotstring")engine.create_abbreviation(folder,"prog","prog",r"program")engine.create_abbreviation(folder,"wdw","wdw",r"windows")engine.create_abbreviation(folder,"xplo","xplo",r"explorer")engine.create_abbreviation(folder,"xplrr","xplrr",r"explore")engine.create_abbreviation(folder,"applis","applis",r"applications")engine.create_abbreviation(folder,"flw","flw",r"follow")engine.create_abbreviation(folder,"flwg","flwg",r"following")engine.create_abbreviation(folder,"prop","prop",r"property")engine.create_abbreviation(folder,"props","props",r"properties")engine.create_abbreviation(folder,"desp","desp",r"despite")engine.create_abbreviation(folder,"spcy","spcy",r"simplicity")engine.create_abbreviation(folder,"gros","gros",r"groups")engine.create_abbreviation(folder,"mtvn","mtvn",r"motivation")engine.create_abbreviation(folder,"cond","cond",r"condition")engine.create_abbreviation(folder,"guars","guars",r"guarantees")engine.create_abbreviation(folder,"check","check",r"check")engine.create_abbreviation(folder,"difeq","difeq",r"differential equation")engine.create_abbreviation(folder,"eqn","eqn",r"equation")engine.create_abbreviation(folder,"symms","symms",r"symmetries")engine.create_abbreviation(folder,"cpx","cpx",r"complex")engine.create_abbreviation(folder,"strc","strc",r"structure")engine.create_abbreviation(folder,"strcs","strcs",r"structures")engine.create_abbreviation(folder,"cofsg","cofsg",r"classification of finite simple groups")engine.create_abbreviation(folder,"obj","obj",r"object")engine.create_abbreviation(folder,"multn","multn",r"multiplication")engine.create_abbreviation(folder,"mult","mult",r"multiply")engine.create_abbreviation(folder,"ti","ti",r"their")engine.create_abbreviation(folder,"thrm","thrm",r"theorem")engine.create_abbreviation(folder,"thry","thry",r"theory")engine.create_abbreviation(folder,"eb","eb",r"ebooks")engine.create_abbreviation(folder,"exer","exer",r"exercises")engine.create_abbreviation(folder,"unt","unt",r"until")engine.create_abbreviation(folder,"tod","tod",r"today")engine.create_abbreviation(folder,"defn","defn",r"definition")engine.create_abbreviation(folder,"hpn","hpn",r"happen")engine.create_abbreviation(folder,"happens","happens",r"happens")engine.create_abbreviation(folder,"grp","grp",r"group")engine.create_abbreviation(folder,"grps","grps",r"groups")engine.create_abbreviation(folder,"intro","intro",r"introduction")engine.create_abbreviation(folder,"satisg","satisg",r"satisfying")engine.create_abbreviation(folder,"imdy","imdy",r"immediately")engine.create_abbreviation(folder,"imd","imd",r"immediate")engine.create_abbreviation(folder,"rtns","rtns",r"rationals")engine.create_abbreviation(folder,"tgl","tgl",r"toggle")engine.create_abbreviation(folder,"seld","seld",r"selected")engine.create_abbreviation(folder,"satis","satis",r"satisfy")engine.create_abbreviation(folder,"clasn","clasn",r"classification")engine.create_abbreviation(folder,"cofabg","cofabg",r"classification of finite abelian groups")engine.create_abbreviation(folder,"gnr","gnr",r"general")engine.create_abbreviation(folder,"invs","invs",r"inverses")engine.create_abbreviation(folder,"comuy","comuy",r"commutativity")engine.create_abbreviation(folder,"comuv","comuv",r"commutative")engine.create_abbreviation(folder,"cgrp","cgrp",r"commutative group")engine.create_abbreviation(folder,"agrp","agrp",r"abelian group")engine.create_abbreviation(folder,"pia","pia",r"piano")engine.create_abbreviation(folder,"ndd","ndd",r"needed")engine.create_abbreviation(folder,"reqd","reqd",r"required")engine.create_abbreviation(folder,"alge","alge",r"algebra")engine.create_abbreviation(folder,"algec","algec",r"algebraic")engine.create_abbreviation(folder,"proby","proby",r"probably")engine.create_abbreviation(folder,"alea","alea",r"at least")engine.create_abbreviation(folder,"inft","inft",r"infinite")engine.create_abbreviation(folder,"infy","infy",r"infinitely")engine.create_abbreviation(folder,"pstn","pstn",r"position")engine.create_abbreviation(folder,"elems","elems",r"elements")engine.create_abbreviation(folder,"cntr","cntr",r"counter")engine.create_abbreviation(folder,"cexp","cexp",r"counter example")engine.create_abbreviation(folder,"addn","addn",r"addition")engine.create_abbreviation(folder,"rl","rl",r"real")engine.create_abbreviation(folder,"nbs","nbs",r"numbers")engine.create_abbreviation(folder,"fm","fm",r"form")engine.create_abbreviation(folder,"wrest","wrest",r"with respect to")engine.create_abbreviation(folder,"cho","cho",r"choose")engine.create_abbreviation(folder,"vrf","vrf",r"verify")engine.create_abbreviation(folder,"jscr","jscr",r"javascript")engine.create_abbreviation(folder,"ccpt","ccpt",r"concept")engine.create_abbreviation(folder,"ccpts","ccpts",r"concepts")engine.create_abbreviation(folder,"xec","xec",r"execution")engine.create_abbreviation(folder,"ord","ord",r"order")engine.create_abbreviation(folder,"otw","otw",r"otherwise")engine.create_abbreviation(folder,"bsc","bsc",r"basic")engine.create_abbreviation(folder,"sax","sax",r"saxophone")engine.create_abbreviation(folder,"ltx","ltx",r"latex")engine.create_abbreviation(folder,"fdr","fdr",r"folder")engine.create_abbreviation(folder,"general","general",r"general")engine.create_abbreviation(folder,"philo","philo",r"philosophy")engine.create_abbreviation(folder,"descrs","descrs",r"describres")engine.create_abbreviation(folder,"cnstrn","cnstrn",r"Construction")engine.create_abbreviation(folder,"msrb","msrb",r"measurable")engine.create_abbreviation(folder,"trnsf","trnsf",r"transform")engine.create_abbreviation(folder,"frr","frr",r"fourrier")engine.create_abbreviation(folder,"ftrns","ftrns",r"fourrier transform")engine.create_abbreviation(folder,"topol","topol",r"topololgy")engine.create_abbreviation(folder,"dtl","dtl",r"detail")engine.create_abbreviation(folder,"trum","trum",r"trumpet"):R:iot:in order to
engine.create_abbreviation(folder,"prcs","prcs",r"precise")engine.create_abbreviation(folder,"sound","sound",r"seen")engine.create_abbreviation(folder,"prfs","prfs",r"proofs")engine.create_abbreviation(folder,"flg","flg",r"feeling")engine.create_abbreviation(folder,"wrtn","wrtn",r"written")engine.create_abbreviation(folder,"dfn","dfn",r"define")engine.create_abbreviation(folder,"sn","sn",r"soon")engine.create_abbreviation(folder,"mathematical","mathematical",r"mathematical")engine.create_abbreviation(folder,"sttm","sttm",r"statement")engine.create_abbreviation(folder,"illus","illus",r"illustrate")engine.create_abbreviation(folder,"achi","achi",r"achieve")engine.create_abbreviation(folder,"re","re",r"real")engine.create_abbreviation(folder,"flang","flang",r"formal language")engine.create_abbreviation(folder,"sttms","sttms",r"statements")engine.create_abbreviation(folder,"alts","alts",r"alternatives")engine.create_abbreviation(folder,"sns","sns",r"sense")engine.create_abbreviation(folder,"udt","udt",r"understand")engine.create_abbreviation(folder,"fst","fst",r"first")engine.create_abbreviation(folder,"ho","ho",r"hope")engine.create_abbreviation(folder,"conv","conv",r"convince")engine.create_abbreviation(folder,"theos","theos",r"theorems")engine.create_abbreviation(folder,"os","os",r"ones")engine.create_abbreviation(folder,"trg","trg",r"trying")engine.create_abbreviation(folder,"consi","consi",r"consider")engine.create_abbreviation(folder,"equiv","equiv",r"equivalent")engine.create_abbreviation(folder,"fvrt","fvrt",r"favorite")engine.create_abbreviation(folder,"sttd","sttd",r"started")engine.create_abbreviation(folder,"devm","devm",r"development")engine.create_abbreviation(folder,"bss","bss",r"basis")engine.create_abbreviation(folder,"fdts","fdts",r"foundations")engine.create_abbreviation(folder,"mysto","mysto",r"mysterious")engine.create_abbreviation(folder,"objs","objs",r"objects")engine.create_abbreviation(folder,"dict","dict",r"dictionary")engine.create_abbreviation(folder,"oril","oril",r"original")engine.create_abbreviation(folder,"prf","prf",r"proof")engine.create_abbreviation(folder,"extl","extl",r"external")engine.create_abbreviation(folder,"xtnl","xtnl",r"External")engine.create_abbreviation(folder,"rscs","rscs",r"resources")engine.create_abbreviation(folder,"arti","arti",r"article")engine.create_abbreviation(folder,"natu","natu",r"natural")engine.create_abbreviation(folder,"general","general",r"general")engine.create_abbreviation(folder,"comm","comm",r"comment")engine.create_abbreviation(folder,"asap","asap",r"as soon as possible")engine.create_abbreviation(folder,"dp","dp",r"deep")engine.create_abbreviation(folder,"axm","axm",r"axiom")engine.create_abbreviation(folder,"ansg","ansg",r"answering")engine.create_abbreviation(folder,"specific","specific",r"specific")engine.create_abbreviation(folder,"cheg","cheg",r"checking")engine.create_abbreviation(folder,"qt","qt",r"quite")engine.create_abbreviation(folder,"chars","chars",r"characters")engine.create_abbreviation(folder,"calc","calc",r"calculus")engine.create_abbreviation(folder,"bk","bk",r"book")engine.create_abbreviation(folder,"syss","syss",r"systems")engine.create_abbreviation(folder,"frml","frml",r"formal")engine.create_abbreviation(folder,"proofs","proofs",r"proofs")engine.create_abbreviation(folder,"gm","gm",r"game")engine.create_abbreviation(folder,"sha","sha",r"shall")engine.create_abbreviation(folder,"ltrs","ltrs",r"letters")engine.create_abbreviation(folder,"alpb","alpb",r"alphabet")engine.create_abbreviation(folder,"reg","reg",r"regular")engine.create_abbreviation(folder,"bhvs","bhvs",r"behaves")engine.create_abbreviation(folder,"seqs","seqs",r"sequences")engine.create_abbreviation(folder,"seq","seq",r"sequence")engine.create_abbreviation(folder,"phr","phr",r"phrase")engine.create_abbreviation(folder,"vals","vals",r"values")engine.create_abbreviation(folder,"eao","eao",r"each one")engine.create_abbreviation(folder,"tfmt","tfmt",r"transformation")engine.create_abbreviation(folder,"rls","rls",r"rules")engine.create_abbreviation(folder,"phrs","phrs",r"phrases")engine.create_abbreviation(folder,"xprs","xprs",r"express")engine.create_abbreviation(folder,"afirms","afirms",r"affirmations")engine.create_abbreviation(folder,"afirm","afirm",r"affirmation")engine.create_abbreviation(folder,"dbl","dbl",r"double")engine.create_abbreviation(folder,"sns","sns",r"sense")engine.create_abbreviation(folder,"philol","philol",r"philosophical")engine.create_abbreviation(folder,"discun","discun",r"discussion")engine.create_abbreviation(folder,"fundl","fundl",r"fundamental")engine.create_abbreviation(folder,"oprtn","oprtn",r"operation")engine.create_abbreviation(folder,"sk","sk",r"skip")engine.create_abbreviation(folder,"descrn","descrn",r"description")engine.create_abbreviation(folder,"dcptn","dcptn",r"description")engine.create_abbreviation(folder,"ys","ys",r"yourself")engine.create_abbreviation(folder,"yrsf","yrsf",r"yourself")engine.create_abbreviation(folder,"jtfns","jtfns",r"justifications")engine.create_abbreviation(folder,"chr","chr",r"character")engine.create_abbreviation(folder,"consts","consts",r"constants")engine.create_abbreviation(folder,"nbrs","nbrs",r"numbers")engine.create_abbreviation(folder,"nnbrs","nnbrs",r"natural numbers")engine.create_abbreviation(folder,"unq","unq",r"unique")engine.create_abbreviation(folder,"emp","emp",r"empty")engine.create_abbreviation(folder,"clry","clry",r"clearly")engine.create_abbreviation(folder,"unqy","unqy",r"uniquely")engine.create_abbreviation(folder,"frt","frt",r"further")engine.create_abbreviation(folder,"bty","bty",r"beauty")engine.create_abbreviation(folder,"ops","ops",r"opens")engine.create_abbreviation(folder,"cpctd","cpctd",r"complicated")engine.create_abbreviation(folder,"vrb","vrb",r"variable")engine.create_abbreviation(folder,"acty","acty",r"actually")engine.create_abbreviation(folder,"xcp","xcp",r"except")engine.create_abbreviation(folder,"prvg","prvg",r"proving")engine.create_abbreviation(folder,"prvd","prvd",r"proved")engine.create_abbreviation(folder,"mns","mns",r"means")engine.create_abbreviation(folder,"prj","prj",r"project")engine.create_abbreviation(folder,"inst","inst",r"instead")engine.create_abbreviation(folder,"trsl","trsl",r"translate")engine.create_abbreviation(folder,"gnrlz","gnrlz",r"generalize")engine.create_abbreviation(folder,"cte","cte",r"constant")engine.create_abbreviation(folder,"dfns","dfns",r"defines")engine.create_abbreviation(folder,"trsld","trsld",r"translated")engine.create_abbreviation(folder,"ho","ho",r"hope")engine.create_abbreviation(folder,"cmp","cmp",r"computer")engine.create_abbreviation(folder,"ae","ae",r"able")engine.create_abbreviation(folder,"rea","rea",r"reach")engine.create_abbreviation(folder,"anss","anss",r"answers")engine.create_abbreviation(folder,"cnv","cnv",r"convince")engine.create_abbreviation(folder,"rpr","rpr",r"represent")engine.create_abbreviation(folder,"flws","flws",r"follows")engine.create_abbreviation(folder,"knn","knn",r"known")engine.create_abbreviation(folder,"fsys","fsys",r"formal system")engine.create_abbreviation(folder,"itrtg","itrtg",r"interesting")engine.create_abbreviation(folder,"stts","stts",r"states")engine.create_abbreviation(folder,"powf","powf",r"powerful")engine.create_abbreviation(folder,"techq","techq",r"technique")engine.create_abbreviation(folder,"cphs","cphs",r"comprehensive")engine.create_abbreviation(folder,"fncs","fncs",r"functions")engine.create_abbreviation(folder,"elems","elems",r"elements")engine.create_abbreviation(folder,"sym","sym",r"symbol")engine.create_abbreviation(folder,"cvgc","cvgc",r"convergence")engine.create_abbreviation(folder,"xpnl","xpnl",r"exponential")engine.create_abbreviation(folder,"defns","defns",r"definitions")engine.create_abbreviation(folder,"intu","intu",r"intuition")engine.create_abbreviation(folder,"tls","tls",r"tells")engine.create_abbreviation(folder,"ntg","ntg",r"nothing")engine.create_abbreviation(folder,"lbl","lbl",r"little by little")engine.create_abbreviation(folder,"atg","atg",r"anything")engine.create_abbreviation(folder,"atc","atc",r"article")engine.create_abbreviation(folder,"opn","opn",r"opinion")engine.create_abbreviation(folder,"mthcs","mthcs",r"mathematicians")engine.create_abbreviation(folder,"prgms","prgms",r"programs")engine.create_abbreviation(folder,"dife","dife",r"different")engine.create_abbreviation(folder,"aum","aum",r"automatic")engine.create_abbreviation(folder,"stri","stri",r"string")engine.create_abbreviation(folder,"ctr","ctr",r"center")engine.create_abbreviation(folder,"tbl","tbl",r"table")engine.create_abbreviation(folder,"ru","ru",r"rule")engine.create_abbreviation(folder,"oprtns","oprtns",r"operations")engine.create_abbreviation(folder,"oprtn","oprtn",r"operation")engine.create_abbreviation(folder,"sec","sec",r"second")engine.create_abbreviation(folder,"pos","pos",r"position")engine.create_abbreviation(folder,"wei","wei",r"weight")engine.create_abbreviation(folder,"gs","gs",r"goes")engine.create_abbreviation(folder,"oprtn","oprtn",r"operation")engine.create_abbreviation(folder,"oprtns","oprtns",r"operations")engine.create_abbreviation(folder,"jtf","jtf",r"justify")engine.create_abbreviation(folder,"nb","nb",r"number")engine.create_abbreviation(folder,"chrs","chrs",r"characters")engine.create_abbreviation(folder,"pts","pts",r"points")engine.create_abbreviation(folder,"hg","hg",r"high")engine.create_abbreviation(folder,"thi","thi",r"think")engine.create_abbreviation(folder,"afmtn","afmtn",r"affirmation")engine.create_abbreviation(folder,"tu","tu",r"true")engine.create_abbreviation(folder,"prvn","prvn",r"proven")engine.create_abbreviation(folder,"afmtns","afmtns",r"affirmations")engine.create_abbreviation(folder,"xpln","xpln",r"explain")engine.create_abbreviation(folder,"ccs","ccs",r"conclusion")engine.create_abbreviation(folder,"pcs","pcs",r"precise")engine.create_abbreviation(folder,"htks","htks",r"hotkeys")engine.create_abbreviation(folder,"htk","htk",r"hotkey")engine.create_abbreviation(folder,"cvcd","cvcd",r"convinced")engine.create_abbreviation(folder,"cpr","cpr",r"compare")engine.create_abbreviation(folder,"smo","smo",r"someone")engine.create_abbreviation(folder,"cptr","cptr",r"computer")engine.create_abbreviation(folder,"sla","sla",r"so long as")engine.create_abbreviation(folder,"agr","agr",r"agree")engine.create_abbreviation(folder,"dfrc","dfrc",r"difference")engine.create_abbreviation(folder,"wds","wds",r"words")engine.create_abbreviation(folder,"ud","ud",r"used")engine.create_abbreviation(folder,"eng","eng",r"English")engine.create_abbreviation(folder,"tmn","tmn",r"too many")engine.create_abbreviation(folder,"mtp","mtp",r"multiple")engine.create_abbreviation(folder,"wld","wld",r"world")engine.create_abbreviation(folder,"bsd","bsd",r"based")engine.create_abbreviation(folder,"mthns","mthns",r"mathematicians")engine.create_abbreviation(folder,"sr","sr",r"sure")engine.create_abbreviation(folder,"er","er",r"error")engine.create_abbreviation(folder,"oao","oao",r"over and over")engine.create_abbreviation(folder,"tmsv","tmsv",r"themselves")engine.create_abbreviation(folder,"itrtg","itrtg",r"interesting")engine.create_abbreviation(folder,"smrzs","smrzs",r"summarizes")engine.create_abbreviation(folder,"ctx","ctx",r"context")engine.create_abbreviation(folder,"plc","plc",r"place")engine.create_abbreviation(folder,"bnf","bnf",r"benefit")engine.create_abbreviation(folder,"sstv","sstv",r"sensitive")engine.create_abbreviation(folder,"fdtns","fdtns",r"foundations")engine.create_abbreviation(folder,"ntcd","ntcd",r"noticed")engine.create_abbreviation(folder,"ss","ss",r"sense")engine.create_abbreviation(folder,"eqv","eqv",r"equivalent")engine.create_abbreviation(folder,"pfd","pfd",r"profound")engine.create_abbreviation(folder,"ifec","ifec",r"influence")engine.create_abbreviation(folder,"ppsd","ppsd",r"proposed")engine.create_abbreviation(folder,"chc","chc",r"choice")engine.create_abbreviation(folder,"dvlp","dvlp",r"develop")engine.create_abbreviation(folder,"pplr","pplr",r"popular")engine.create_abbreviation(folder,"gnrly","gnrly",r"generally")engine.create_abbreviation(folder,"cls","cls",r"close")engine.create_abbreviation(folder,"atck","atck",r"attack")engine.create_abbreviation(folder,"dvsn","dvsn",r"division")engine.create_abbreviation(folder,"stro","stro",r"strong")engine.create_abbreviation(folder,"pow","pow",r"power")engine.create_abbreviation(folder,"srs","srs",r"series")engine.create_abbreviation(folder,"pwr","pwr",r"power")engine.create_abbreviation(folder,"psrs","psrs",r"power series")engine.create_abbreviation(folder,"evw","evw",r"everywhere")engine.create_abbreviation(folder,"hlmp","hlmp",r"holomorphic")engine.create_abbreviation(folder,"yr","yr",r"your")engine.create_abbreviation(folder,"eqtn","eqtn",r"equation")engine.create_abbreviation(folder,"tms\","tms\",r"\times")engine.create_abbreviation(folder,"dfntn","dfntn",r"definition")engine.create_abbreviation(folder,"sltn","sltn",r"solution")engine.create_abbreviation(folder,"difeqs","difeqs",r"differential equations")engine.create_abbreviation(folder,"psrs","psrs",r"power series")engine.create_abbreviation(folder,"itscs","itscs",r"in this case")engine.create_abbreviation(folder,"pr\","pr\",r"()")engine.create_abbreviation(folder,"invs","invs",r"inverse")engine.create_abbreviation(folder,"lkg","lkg",r"looking")engine.create_abbreviation(folder,"mtx","mtx",r"matrix")engine.create_abbreviation(folder,"eucln","eucln",r"Euclidean")engine.create_abbreviation(folder,"cvgc","cvgc",r"convergence")engine.create_abbreviation(folder,"trc","trc",r"trace")engine.create_abbreviation(folder,"ifnt","ifnt",r"infinite")engine.create_abbreviation(folder,"fnt","fnt",r"finite")engine.create_abbreviation(folder,"jrdn","jrdn",r"Jordan")engine.create_abbreviation(folder,"dcpsn","dcpsn",r"decomposition")engine.create_abbreviation(folder,"tdtnl","tdtnl",r"traditional")engine.create_abbreviation(folder,"msc","msc",r"music")engine.create_abbreviation(folder,"kbd","kbd",r"keyboard")engine.create_abbreviation(folder,"hf","hf",r"half")engine.create_abbreviation(folder,"itfp","itfp",r"in the first place")engine.create_abbreviation(folder,"cns","cns",r"chinese")engine.create_abbreviation(folder,"fftft","fftft",r"follows from the fact that")engine.create_abbreviation(folder,"taglr","taglr",r"triangular")engine.create_abbreviation(folder,"sgrp","sgrp",r"subgroup")engine.create_abbreviation(folder,"ivtb","ivtb",r"invertible")engine.create_abbreviation(folder,"dagn","dagn",r"diagonal")engine.create_abbreviation(folder,"mtxs","mtxs",r"matrices")engine.create_abbreviation(folder,"pstv","pstv",r"positive")engine.create_abbreviation(folder,"coefs","coefs",r"coefficients")engine.create_abbreviation(folder,"diag","diag",r"diagonal")engine.create_abbreviation(folder,"dmtx","dmtx",r"diagonal matrix")engine.create_abbreviation(folder,"egvl","egvl",r"eigenvalue")engine.create_abbreviation(folder,"egvls","egvls",r"eigenvalues")engine.create_abbreviation(folder,"bij","bij",r"bijection")engine.create_abbreviation(folder,"oto","oto",r"one-to-one")engine.create_abbreviation(folder,"eqvln","eqvln",r"equivalent")engine.create_abbreviation(folder,"wdfnd","wdfnd",r"well defined")engine.create_abbreviation(folder,"aotf","aotf",r"are of the form")engine.create_abbreviation(folder,"dfnd","dfnd",r"defined")engine.create_abbreviation(folder,"ovoy","ovoy",r"obviously")engine.create_abbreviation(folder,"rst","rst",r"reset")engine.create_abbreviation(folder,"qt","qt",r"quite")engine.create_abbreviation(folder,"mnfd","mnfd",r"manifold")engine.create_abbreviation(folder,"btm","btm",r"bottom")engine.create_abbreviation(folder,"bfr","bfr",r"beforer")engine.create_abbreviation(folder,"lgrp","lgrp",r"Lie group")engine.create_abbreviation(folder,"exp","exp",r"exponential")engine.create_abbreviation(folder,"xpnt","xpnt",r"exponential")engine.create_abbreviation(folder,"opsgrps","opsgrps",r"one-parameter subgroups")engine.create_abbreviation(folder,"opsgrp","opsgrp",r"one-parameter subgroup")engine.create_abbreviation(folder,"agb","agb",r"algebra")engine.create_abbreviation(folder,"lagb","lagb",r"Lie algebra")engine.create_abbreviation(folder,"lgrps","lgrps",r"Lie groups")engine.create_abbreviation(folder,"dmnfd","dmnfd",r"differentiable manifold")engine.create_abbreviation(folder,"stt","stt",r"such that")engine.create_abbreviation(folder,"vspc","vspc",r"vector space")engine.create_abbreviation(folder,"eqrel","eqrel",r"equivalence relation")engine.create_abbreviation(folder,"lgexp","lgexp",r"Lie group exponential")engine.create_abbreviation(folder,"assocd","assocd",r"associated")engine.create_abbreviation(folder,"neig","neig",r"neighborhood")engine.create_abbreviation(folder,"amth","amth",r"applied mathematics")engine.create_abbreviation(folder,"rtt","rtt",r"rather than")