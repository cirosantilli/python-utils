header = ''
body = ''

strExpandTerminator = ';'
runTerminator = '\\'

curOptions = ['*','o']

hstr('gnm;','Ciro')

#NoEnv
SendMode Input  
SetWorkingDir %A_ScriptDir%
;Autohotkey

;-- global switches ------------------------------------------------------------;
oneletters = 0		#- one letter button -#
html = 1		#- html on off -#

#- paths factoring -#
root = 'C:'

ciro = os.path.join(root,'Users','Ciro')
htdocs = os.path.join(root,'xampp','htdocs')
programFilesX86 = os.path.join(root,'Program Files (x86)')

documents = os.path.join(ciro,'Documents')
desktop = os.path.join(ciro,'Desktop')

backup = os.path.join(ciro,'backup')
downloads = os.path.join(ciro,'Downloads')
rapidshare = os.path.join(ciro,'Rapidshare')

share = os.path.join(ciro,'share')
noshare = os.path.join(ciro,'noshare')

music = os.path.join(ciro,'Music')
films = os.path.join(ciro,'Videos','Films')
games = os.path.join(ciro,'Games')
images = os.path.join(ciro,'Images')
texts = os.path.join(ciro,'Texts')
chinese_learning = os.path.join(ciro,'Chinese Learning')

threeA = os.path.join(noshare,'x','3A')
programs = os.path.join(noshare,'programs')
certificates = os.path.join(noshare,'certificates')

python = os.path.join(programs,'python')
latex = os.path.join(programs,'latex')
autohotkeys = os.path.join(programs,'autohotkeys')

notepadppf = os.path.join(programFilesX86,'Notepad++')

notepadpp = os.path.join(notepadppf,'notepad++.')

elearning = os.path.join(htdocs,'elearning')

mathematics = os.path.join(texts,'Mathematics')
physics = os.path.join(texts,'Physics')

#- caps lock initialization -#
SetCapsLockState, AlwaysOff

#-- global functions ------------------------------------------------------------#
header += """
asdf
asdf
"""
OpenFolder(dir)
{
	
	;Run %dir%
	;Run C:\Program Files (x86)\muCommander\muCommander.exe "%dir%" "%dir%"
	
	Run C:\Program Files (x86)\FreeCommander\FreeCommander.exe  /C "%dir%"
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
Send,{Enter}^v
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
hstr('','gnm`;','Ciro')					#- Given NaMe -#
hstr('','lnm`;','Santilli')				#- Last name -#
hstr('','fnm`;','Duran Santilli')			#- Family name -#
hstr('','cnm`;','Ciro Duran Santilli')		#- Complete name -#
hstr('','cnmf`;','Ciro DURAN SANTILLI')		#- French capital last name standard -#
hstr('','cnma`;','Ciro D. Santilli')		#- Abbreviated (or American) dot middle name-#
hstr('','fgnm`;','Duran Santilli{Tab}Ciro{Tab}')	#- family then given name for internet input-#

hstr('','bdt`;','14/05/1989')
hstr('','bct`;','Rio Claro')

#- address -#
hstr('','adr`;','10, boulevard des Maréchaux')			#- address -#
hstr('','adrc`;','Bâtiment FOCH, Appartement 10.20.39')	#- address complement -#
hstr('','pcd`;','91120')						#- Postal CoDe -#
hstr('','city`;','Palaiseau')					#- city -#
hstr('','cpc`;','Palaiseau, 91120')						#- City Postal CoDe -#
hstr('','fadr`;','10, boulevard des Maréchaux{Tab}Bâtiment FOCH, Appartement{Tab}91120{Tab}Palaiseau')	#- Full address for internet input-#

#- EP address -#

hstr('','epf`;','École Polytechnique')	#- Ãƒâ€°cole Polytechnique (France) -#
hstr('','epadr`;','ECOLE POLYTECHNIQUE')	#- address -#
hstr('','epadrc`;','Route de Saclay')	#- address complement line 2 -#
hstr('','eppcd`;','91128')			#- Postal CoDe -#
hstr('','epcity`;','PALAISEAU Cedex')	#- city -#
hstr('','epfadr`;','ECOLE POLYTECHNIQUE{Tab}Route de Saclay{Tab}91128{Tab}PALAISEAU Cedex')	    #- Full address for internet input-#

#- contact -#
hstr('','mail`;','ciro.santilli@gmail.com')	#- email -#
hstr('','tel`;','0169591651')			#- fixed telephone -#

hstr('','cell`;','0658851651')			#- cell phone -#
hstr('','tcell`;','ciro.santilli@gmail.com')	#- cell phone -#
hstr('','ncs`;','Ciro D. Santilli`ncel: {+}33658851651`nskype: ciro.santilli')		#- Name, Cell, Skype -#

#- social security France -#
hstr('','smerep`;','139205899')			#- SMEREP number -#
hstr('','nss`;','1890599416120')			#- numero de securite sociale -#
hstr('','ass`;','16 Bd. du General Leclerc - 92115 Clichy CEDEX')		#- adress ss -#
hstr('','ssc`;','Vitale`rOrganisme: 99911061`rAdresse: 16 Bd. du General Leclerc - 92115 Clichy CEDEX`rNuméro de securité sociale: 189059941612087') #- Complete ss -#

#- user pass -#
hstr('','unm`;','cirosantilli')				#- standard User Name -#
hstr('','pwd`;','fgb4669201')					#- cheap password -#
hstr('','pwdu`;','Fgb4669201')				#- cheap password Upper case-#
hstr('','upwd`;','cirosantilli{Tab}fgb4669201{Enter}')	#- user + password for quick internet input-#
hstr('','oid`;','https://plus.google.com/106598607405640635523/posts')	#- Open ID-#

#-- Time stamps ---------------------------------------------#
::dmy`;::	#- dd/mm/yyyy -#
	Send,%A_DD%/%A_MM%/%A_YYYY% #- day month year, most standard form  -#
return

::dmys`;::	#- dd-mm-yyyy -#
	Send,%A_DD%-%A_MM%-%A_YYYY% #- day month year, most standard form  -#
return

::ymds`;::	#- Year Month Day with Slashes. For backuping. -#
	Send,%A_YYYY%-%A_MM%-%A_DD% #- day month year, most standard form  -#
return

::dmyw`;::
	Send,%A_DD%/%A_MM%/%A_YYYY% %A_DDD% #-  %A_Hour%:%A_Min%:%A_Sec%  day month year, most standard form  -#
return

::tms`;::	#- TiMeStamp, specially for file versionning -#
	Send, %A_YYYY%-%A_MM%-%A_DD% %A_Hour%-%A_Min%-%A_Sec%
return

#-- quick and dirty text processing ------------------------------------------------------------#

::dts\::	    #- dot to space -#
StringReplace, clipboard, clipboard, ., %A_SPACE%, All
return

::uts\::	    #- underline to space -#
StringReplace, clipboard, clipboard, _, %A_SPACE%, All
return

::stu\::	    #- space to underline -#
StringReplace, clipboard, clipboard, %A_SPACE%, _, All
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

hstr('*o','hstr`;','{:}{:}{:}{:}{Left 2}')	    #- Ahk hotstring -#
hstr('*o','avar`;','{%}{%}{Left 1}')		    #- Ahk variable value -#
hstr('*o','acm`;','{;}-  -{;}{Left 3}')		    #- Ahk comment -#
hstr('*o','aln`;','#--  {- 60};{Home}{Right 4}')	    #- ahk line -#
hstr('*o','ahln`;','#--  {- 30};{Home}{Right 4}')	    #- ahk half line -#

#-- Windows Explorer ------------------------------------------------------------#

^F2::		    #- Rename Underline To Space -#
Send,{F2}^c
;StringReplace, clipboard, clipboard, _, %A_SPACE%, All;
Send,^v
return

#IfWinActive ahk_class CabinetWClass

#-- new window operations. prefixed by ^ ------------------------------#
#- create new text file -#
^+m:: ; analogy to ^+n which creates a new folder. French. Depends on installed programs...
Send {Alt Down}f{Alt Up}e{Up 5}{Enter}
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
Send {Shift Down}{F10}{Shift Up}7aa{Enter}
return

#- decompress .zip here -#
!+u:: ; French.
Send {Shift Down}{F10}{Shift Up}7{Down 2}{Enter}
return

#- decompress .zip to folder -#
!+y:: ; French.
Send {Shift Down}{F10}{Shift Up}7{Down 3}{Enter}
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
::cb\:: #- codeblocks -#
    RunFocusMinTitle("Code::Blocks 10.05","C:\Program Files (x86)\CodeBlocks\codeblocks.exe")
return

::ch\:: #- Chrome -#
    RunFocusMin("Chrome_WidgetWin_0","C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
return

::ec\:: #- Eclipse -#
    RunFocusMin("SWT_Window0","C:\Program Files (x86)\Eclipse\eclipse.exe")
return

::ff\:: #- firefox -#
    RunFocusMin("MozillaWindowClass","C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
return

::mp\:: #- Media Player -#
    RunFocusMin("WMPlayerApp","C:\Program Files (x86)\Windows Media Player\wmplayer.exe")
return

::nb\:: #- netbeans -#
    RunFocusMin("SunAwtFrame","C:\Program Files (x86)\NetBeans 7.0.1\bin\netbeans.exe")
return

::np\:: #- notepad++ -#
    RunFocusMin("Notepad++",notepadpp)
return

::npf;:: #- notepad++ folder-#
    SendRaw,%notepadppf%	#- must use Raw because of the + signs which mean Shift -#
return

::npf\:: #- notepad++ folder-#
    Run %notepadppf%	#- must use Raw because of the + signs which mean Shift -#
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


::twp\:: #- major mouse workaround to get Netbeans Current file path and then do wordpress conversion. uglyy -#
IfWinActive,ahk_class SunAwtFrame 	#- demi check we are in netbeans -#
{
    CurNbFilePathToClipboard()
    run python %elearning%/site-core/wp_markup_conversion.py %clipboard%
}
return

::ttt\:: #- To TesT. Do Test Markup Conversion. Put a dummy id on page and go to it. =) Uglyy, and works! -#
IfWinActive,ahk_class SunAwtFrame 	#- demi check we are in netbeans -#
{
    Send,<span id="HERETESTID"/> 	#- put the test id to go to -#
    Sleep, 500
    CurNbFilePathToClipboard()	 	#- put current path on clipboard -#
    Sleep, 500
    run python %elearning%/site-core/test_markup_conversion.py %clipboard%	#- let python do the conversion -#
    Sleep, 1000
    Send,!{Tab}		#- remove fake id from source and shift between browser and NB -#
    Sleep, 500    
    Send,{BacSleep, 500
    Send,!{Tab}
}
return

::npd\:: #- note pad -#
    RunFocusMin("Notepad","C:\Windows\system32\notepad.exe")
return

#- foxit reader -#
::pd\:: #- pdf -#
    RunFocusMin("classFoxitReader","C:\Program Files (x86)\Foxit Software\Foxit Reader\Foxit Reader.exe")
return

!z::	#- change colors. todo doesnt work -#
IfWinActive,ahk_class classFoxitReader
{
    Send,{Control Down}k{Control Up}{Alt Down}r{Alt Up}{Enter}
}
return 


::rs\:: #- R Statistics -#
    RunFocusMinTitle("RGui","C:\Program Files\R\R-2.14.0\bin\i386\Rgui.exe")
return

::sk\:: #- Skype -#
    RunFocusMin("tSkMainForm","C:\Program Files (x86)\Skype\Phone\Skype.exe")
return

::wd\:: #- word -#
    RunFocusMin("OpusApp","C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Word 2007.lnk")
return

#--- /folders --------------------------#
::ro\:: #- Root -#
    OpenFolder("C:")
return

::dt;:: #- Trash -#
    SendRaw,%desktop%
return

::trs\:: #- Trash -#
    Run C:\Trash
return

::doc\:: #- documents -#
    Run ciro + 
return

#w:: #- Downloads Folder. I use this so often, I put an easier shortcut... -#
	OpenFolder(downloads)
return

::dw;:: #- Downloads -#
    SendRaw,%downloads%
return

::pfx\:: #- Program Files x86 -#
    OpenFolder(programFilesX86)
return

::pfx;:: #- Program Files x86 -#
    SendRaw, %programFilesX86%
return

#--- share --------------------------#
::shr\:: #- share -#
    OpenFolder(share)
return

::nsh\:: #- no share -#
    OpenFolder(noshare)
return

::flm\:: #- Films -#
    OpenFolder(films)
return

::game\:: #- Games -#
    OpenFolder(games)
return

::img\:: #- Images -#
    OpenFolder(images)
return

#--- music --------------------------#
::msc\:: #- Music -#
    OpenFolder(music)
return

::ctm\:: #- Chinese traditional music -#
    Run %music%\Chinese Traditional Music.wpl
return

::cmpg\:: #- Chinese traditional music Guqin-#
    Run %music%\Chinese Traditional Music\An Anthology of Chinese Traditional and Folk Music - A Collection of Music Played on the Guqin (note=93)\All.wpl
return

::jpv\:: #- Joe Pass Virtuoso -#
    Run %music%\Playlists\Joe Pass Virtuoso.wpl
return

#--- texts --------------------------#
::txt\:: #- Texts -#
    OpenFolder(texts)
return

::mth\:: #- Mathematics -#
    OpenFolder(mathematics)
return

::phy\:: #- Physics -#
    OpenFolder(physics) 
return

#- noshare -#
::nsh\:: #- noshare -#
    OpenFolder(noshare)
return

::3a\:: #- 3A -#
    OpenFolder(threeA)
return

::3a;::
	SendRaw,%threeA%
return

::ctf\:: #- Certificates -#
    OpenFolder(certificates)
return

#-- Programs ------------------------------#
::prg\:: #- Programs folder -#
    OpenFolder(programs)
return

::prg;::
	Send,%programs%
return

::ltx\:: #- latex -#
    OpenFolder(latex)
return

#-- Python ------------------------------#

::py\:: #- python interpreter -#
    Run python
return

::pyf\:: #- Python Folder -#
    OpenFolder(python)
return

::pym\:: #- Python Main -#
    Run notepad++ %python%\main.py
return

::dia\:: #- dia -#
    Run %autohotkeys%\output.txt
return

::rsh\:: #- RapidShare folder -#
    OpenFolder(rapidshare)
return

#--- Chinese Learning ----------------------------#
::cns\:: #- chinese learning -#
    Run %chinese_learning%
return

::cnts\:: #- chinese notes -#
    Run notepad++ noshare\chinese notes\Chinese notes.txt
return

::lic\:: #- Latest Interactive Chinese -#
    Run %chinese_learning%\Interactive Chinese\Text 6\Text 6.exe
return

::cnsl\:: #- Chinese Learning -#
    OpenFolder(chinese_learning)
return

::heisig\:: #- Chinese character learning -#
    Run %chinese_learning%\Heisig; Richardson - 2009 - Remembering Simplified Hanzi (UHP, 0824833236) note=93.pdf
return

::itm\:: #- Indian traditional music -#
    Run ciro + \Music\Indian Traditional Music.wpl
return

#n:: #- notes. I use this so often I will give it a shorter shortcut.n -#
    Run noshare\notes.txt
return

#-- site dev ------------------------------#

::xamp\::
Run,C:\xampp\xampp-control.exe
Run,C:\xampp\apache_start.bat
Run,C:\xampp\mysql_start.bat
return

::htd\:: #- htdocs -#
    OpenFolder(htdocs)
return

::sde\:: #- Site Dev Elearning -#
    OpenFolder(elearning)
return

::sde;:: #- Site Dev Elearning -#
    SendRaw,%elearning%
return

::sdrsc\:: #- Site Dev ReSourCes -#
    Run,%elearning%\site-dev\resources.ods
return

#--- scripts ----------------------------#
::sic\:: #- set ip Ciro -#
    Run noshare\programs\bat\set ip ciro.bat
return

::six\:: #- set ip Xiaohua -#
     Run noshare\programs\bat\set ip Xiaohua.bat
return

#--- web sites --------------------------#
::mail\::   #- run email -#
    Run https://mail.google.com/mail/?hl=fr&shva=1#inbox
return

::ftb\::   #- filestube -#
    Run http://www.filestube.com/
return

#Hotstring *0 o0

#--------- Code: c, java, html, etc. ------------------------#
;
; Indentation is complicated because of automatic indententaion which varies from program to program to program.
; I'll mostly put only line breaks and hope for Netbeans automatic indentation
;
#Hotstring * O

#-- general ------------------------------------------------------------#
hstr('','op;','(,){Left 2}')  #- ordered pair -#
hstr('','ot;','(,,){Left 3}')  #- ordered triplet -#
hstr('','bp;','[,]{Left 2}')  #- bracket pair -#

#-- Java ------------------------------------------------------------#
hstr('','jpr`;','System.out.println()`;{Left 2}')  #- Java Pring -#
hstr('','jfi`;','for(int i=0; i<; i{+}{+}){{}`n`n{}}{Up 2}{End}{Left 7}')  #- Java For i -#
hstr('','jfij`;','for(int i=0; i<; i{+}{+}){{}`nfor(int j=0; j<; j{+}{+}){{}`n`n{}}`n{}}{Up 4}{End}{Left 7}')  #- Java For i -#

#-- Html ----------------------------------------------------------------------#
:*:\html::		#- toogle html on off -#
if html = 1
    html = 0
else
    html = 1
return

::html;::<html>{Enter}{Enter}</html>{Up}
::head;::<head>{Enter}{Enter}</head>{Up}
::body;::<body>{Enter}{Enter}</body>{Up}
::div;::<div class=""></div>{Left 8}
::span;::<span class=""></span>{Left 9}

::h1;::<h1></h1>{Left 5}
::h2;::<h2></h2>{Left 5}
::h3;::<h3></h3>{Left 5}
::h4;::<h4></h4>{Left 5}
::h5;::<h5></h5>{Left 5}
::h6;::<h6></h6>{Left 5}
::h7;::<h7></h7>{Left 5}
::h8;::<h8></h8>{Left 5}
::h9;::<h9></h9>{Left 5}

::ul;::<ul>`r    <li></li>`r    <li></li>`r</ul>{Up 2}{End}{Left 5}
::ulanc;::<ul>`r    <li><a href="^v"></a></li>`r    <li><a href=""></a></li>`r</ul>{Up 2}{Right 3}
::ol;::<ol>`r    <li></li>`r    <li></li>`r</ol>{Up 2}{Right 3}
::li;::<li></li>{Left 5}

::dl;::<dl>`r    <dt></dt>`r    <dd></dd>`r    <dt></dt>`r    <dd></dd>`r</dl>{Up 4}{Right 3}
::dt;::<dt></dt>{Left 5}
::dd;::<dd></dd>{Left 5}
::dtdd;::<dt></dt>`r    <dd></dd>{Up}{Left 5}

::p;::<p></p>{Left 4}
::pars;::<p class="par-summary"></p>{Left 4}
::rap;::</p>{Enter}<p>{Left 3}

hstr('','prea;','<pre class="ahk"></pre>{Left 6}') #- to display autohotkey code -#

::a;::<a href="^v"></a>{Left 4}
::aid;::<a href="{#}^v"></a>{Left 4}

::bq;::<blockquote></blockquote>
::img;::<div class="image">`r    <img src="^v" />`r    <div class="img-subtitle"></div>`r</div>
::em;::<em></em>{Left 5}
::str`;::<strong></strong>{Left 9}

::br;::<br />
::hr;::<hr />

::tab;::<div class="table">{Enter}<table class="vertical">{Enter}<tr>{Enter}<td></td>{Enter}<td></td>{Enter}</tr>{Enter}<tr>{Enter}<td></td>{Enter}<td></td>{Enter}</tr>{Enter}</table>{Enter}<div class="table-subtitle"></div>{Enter}</div>{Up 9}{Right 8}
::tr;::<tr>{Enter}<td></td>{Enter}<td></td>{Enter}</tr>{Up 2}{Right 3}
::td;::<td></td>{Left 5}

;comments
hstr('','hcm;','<{!}--  -->{Left 4}')	#- Html CoMment -#
::habc;::<{!}--  -->{Left 4}<!--added by ciro --><!--/added by ciro -->
::todo;::<{!}--todo  -->{Left 4}
hstr('','todoe;','<{!}--todo type="example"  -->{Left 4}')    #- missing example -#
hstr('','todol;','<{!}--todo type="link"  -->')	    #- missing link -#
hstr('','todoi;','<{!}--todo type="incomplete"  -->') #- missing information -#
hstr('','todos;','<{!}--todo type="stub"  -->')	    #-  -#

::mail;::<a href="mailto:^v"></a>{Left 4}

::hpp\::	    #- Html Header Plus Plus. Select, copy, modify! quick and dirty and useful. -#
StringReplace, clipboard, clipboard, <h2>, <h1>, All
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

::hmm\::	    #- Html Header Moins Moins -#
StringReplace, clipboard, clipboard, <h5>, <h6>, All
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
::eq`;::			#- EQuation. turns off one letter shortcuts -#
Send,<eq></eq>{Left 5}	#-  -#
oneletters = 0
return

::iq`;::	
Send,<iq></iq>{Space}{Left 6} #- Internal EQuation. Space so that you write inside then press Home to get out and continue the phrase. -#
oneletters=0
return

hstr('','qi`;','\)  \({Left 3}') #- iq reversed. To cut up an eq. -#

#- math only: no document parts, identical in javascript mathematics with mathjax -#

#- Subscripts, superscripts -#
hstr('','sbs`;','{Backspace}{_}{{}{}}{Left 1}') #- SuBScript. Usage: first do a space, then und\. Otherwise cannot separate from last word. -#

;logic
::imp`;::\implies{Space}
::ex`;::\exists{Space}
::fa`;::\forall{Space}
::sst`;::\subset{Space}
::qin`;::\(\in\){Space} ;internal iq version when alone

;functions
;;new functions
::fdef`;::\begin{{}align{}}`n\funcDef{{}{}}{{}{}}{{}{}}{{}{}}{{}{}}`n\end{{}align{}}{Up}{End}{Left 9}
::fdom`;::\funcDom{{}{}}{{}{}}{{}{}}{Left 5}
hstr('','comp`;','\comp \comp')	#- composition of functions -#
::argmax`;::\argmax_{{}{}}{Left 1}
::argmin`;::\argmin_{}{}}{Left 1}
::dom`;::Dom(){Left 1}

::blt`;::\bullet

;;elementary functions
::frc`;::\frac{{}{}}{{}{}}{Left 3}
::frco`;::\frac{{}1{}}{{}{}}{Left 1}
::sqrt`;::\sqrt{{}{}}{Left 1}
::pw`;::{Backspace}{^}{{}{}}{Left 1} ;usage: first do a space, then pow\. Otherwise cannot separate from last word.
::pwmo`;::{Backspace}{^}{{}-1{}}
::pwt`;::{Backspace}{^}{{}2{}}

;analysis
;;limits
::lim`;::\lim_{{} \to {}}{Left 6}
::limni`;::\lim_{{}n \to \infty{}}
::inf`;::\infty

::der`;::\der{{}{}}{{}{}}{Left 3}
::ddt`;::\der{{}{}}{{}t{}}{Left 4}
::ddtatt`;::\derAt{{}{}}{{}t{}}{{}{}}{Left 6}
hstr('','ddtattz`;','\derAt{{}{}}{{}t{}}{{}0{}}{Left 7}')   #- ddt at t equals -#
::ddtatto`;::\derAt{{}{}}{{}t{}}{{}1{}}{Left 7}
::ddx`;::\der{{}{}}{{}x{}}{Left 4}
::ddxatx`;::\derAt{{}{}}{{}x{}}{{}{}}{Left 6}
hstr('','ddxatxz`;','\derAt{{}{}}{{}x{}}{{}0{}}{Left 7}')   #- ddx at x equals -#
::ddxatxo`;::\derAt{{}{}}{{}x{}}{{}1{}}{Left 7}
::parder`;::\parDer{{}{}}{{}{}}{Left 3}

::nrm`;::\norm{{}{}}{Left 1}
::nrmpt`;::\norm{{}{}}{^}2{Left 3} ;norm Pow Two

:R:epx`;::e^x
:R:ep`;::e^
::exp`;::\exp(){Left 1}
::explr`;::\exp \left(\right){Left 7}
::log`;::\log(){Left 1}

;matrix matrices
;;sets of matrices
hstr('','mn`;','\Mn') #-- define \Mn in latex to fix standard. for example, we could have either M(n) or M_n. A mixture of both would be intractable... --#
::gln`;::\GLn
::glnr`;::\GLn(\r)
::symn`;::\Symn
::spdn`;::\SPDn

;; matrix functions
::det`;::\det(){Left 1}
hstr('','trp`;','{Backspace}{^}{{}T{}}') #- SuBScript. Usage: first do a space, then und\. Otherwise cannot separate from last word. -#
hstr('','otrp`;','O{^}{{}T{}}') #- O transpose -#
::trc`;::\Tr(){Left 1}
::trclr`;::\Tr\left(\right){Left 7}
::pmtx;::\begin{{}pmatrix{}}`r`r\end{{}pmatrix{}}{Up}

;; other common notation
hstr('','lami`;','\lambda_i') #- eigen values -#
hstr('R','bmodb`;','B^{-1}DB') #- diagonalization -#
hstr('R','otr`;','O^{T}') #- traspose of an orthogonal matrix = to its inverse -#
hstr('R','otdo`;','O^{T}DO') #- diagonalization of a symmetric matrix -#

;;set theory
:R:rq`;::\(\r\)
:R:ro`;::\r^1
:R:rt`;::\r^2
:R:rtq`;::\(\r^2\) 
:R:rn`;::\mathbb{R}^n
:R:rnq`;::\(\r^n\) 
:R:cone`;::\c^1
:R:cn`;::\c^n

:R:tms`;::\times

;parenthesis, brackets, etc
::lrp`;::\left(\right){Left 7} ;Left Right Parenthesis
::lrb`;::\left[\right]{Left 7} ;Brackets
::lrc`;::\left{\right}{Left 7} ;braCes (conflict with brackets) 

;contextless
:R:fx`;::f(x)
:R:fxy`;::f(x,y)
hstr('R','foz`;','f(z)')	#- f Of z -#
:R:fz`;::f_0
:R:fo`;::f_1
:R:ft`;::f_2
:R:gx`;::g(x)
:R:hx`;::h(x)
:R:fxz`;::f(x_0)

:R:gxy`;::G(x,y)

#- x shortcuts. SO useful -#
:R:xz`;::x_0
:R:qxz`;::<iq>x_0</iq> 
hstr('R','xoz`;','x(0)')	#- x Of Zero -#
:R:xo`;::x_1
:R:qxo`;::<iq>x_1</iq> 
hstr('R','xoo`;','x(1)')	#- x Of One -#
:R:xt`;::x_2
:R:qxt`;::<iq>x_2</iq> `
:R:xh`;::x_3
:R:qxh`;::<iq>x_3</iq> 
:R:xf`;::x_4
:R:qxf`;::<iq>x_4</iq> 
hstr('R','xof`;','x(f)')	#- X Of T -#
hstr('R','xi`;','x_i')	#- X Of T -#
hstr('R','xpt`;','x^2')	#- X Pow Two -#
:R:xdot`;::\mathop{x}^{.}
:R:xi`;::x_i
:R:qxi`;::<iq>x_i</iq> `
hstr('R','xot`;','x(t)')	#- X Of T -#

:R:yz`;::y_0
hstr('R','yoz`;','y(0)')	#- Y Of Zero -#
:R:yo`;::y_1
:R:qyo`;::<iq>y_1</iq> `
hstr('R','yoo`;','y(1)')	#- y Of One -#
:R:yt`;::y_2
:R:qyt`;::<iq>y_2</iq> `
:R:yh`;::y_3
:R:qyh`;::<iq>y_3</iq> `
:R:yf`;::y_4
:R:qyf`;::<iq>y_4</iq> `
:R:yi`;::y_i
:R:qyi`;::<iq>y_i</iq> `

hstr('R','yot`;','y(t)')	#- Y Of T -#
:R:ypt`;::y^2
:R:yx`;::y(x)

:R:ymax`;::y_{max}
:R:yre`;::y_{\mathbb{R}}

:R:tz`;::t_0

hstr('','bul`;','\bullet')			#- bullet -#
hstr('','bar`;','\bar{{}{}}{Left 1}')		#- horizontal bar over -#
hstr('','oln`;','\overline{{}{}}{Left 1}')	#- overline -#
hstr('','vec`;','\vec{{}{}}{Left 1}')		#- vector sign -#
hstr('','top`;','\mathtop{{}{}}{{}{}}{Left 3}')	#- mathTOP -#
hstr('','vecz`;','\vec{{}0{}}')			#- vector Zero -#
hstr('','smns`;','\setminus')			#- set minus -#
hstr('','cases`;','\begin{{}cases{}}`n &  \\`n &`n\end{{}cases{}}{Up 2}{Home}') 		#- cases-#


hstr('','oi`;','],[{Left 2}')	#- open interval -#
hstr('','ci`;','[,]{Left 2}')	#- closed interval -#
hstr('','coi`;','[,[{Left 2}')	#- closed open interval -#
hstr('','oci`;','],]{Left 2}')	#- open closed interval -#

;s=sum z=zero, o=one, i=inf, nu=nuppercase. cryptic, but used SO often...
::sum`;::\sum_{{}{}}{^}{{}{}}{Left 4}
:R:sizn`;::\sum_{i=0}^{n}
:R:sizi`;::\sum_{i=0}^{\infty}
:R:sion`;::\sum_{i=1}^{n}
:R:sionu`;::\sum_{i=1}^{N}
:R:sioi`;::\sum_{i=1}^{\infty}
:R:skoi`;::\sum_{k=1}^{\infty}
:R:ai`;::a_i

#- logic, set theory -#
::cprod`;::\cartProd

#- greek letters -#
#Hotstring c
::alp`;::\alpha
::lam`;::\lambda
::eps`;::\epsilon
::vphi`;::\varphi
::lam`;::\lambda
::gam`;::\gamma
::ome`;::\omega
::omeo`;::\omega_1
hstr('R','omeopt`;','\omega_1^2') 	#- Pow Two -#
::omet`;::\omega_2
hstr('R','ometpt`;','\omega_2^2')	#- Pow Two -#
::Ome`;::\Omega
#Hotstring c0

::part`;::\partial

#- ams no library. compatible with ams without any defines. works well on internet for collaborative content -#
hstr('R','re`;','\mathbb{R}')		#- REal numbers -#
hstr('R','ren`;','\mathbb{R}^n')		#- REal numbers -#
hstr('R','res`;','\mathbb{R}')		#- REal Star -#
hstr('R','rep`;','\mathbb{R}_+')		#- REal Plus -#
hstr('R','remns`;','\mathbb{R}_-')		#- REal Minus -#
:R:ire`;::\(\mathbb{R}\) 
:R:co`;::\mathbb{C}

#- comments -#
::lcm`;::{%}-  -{%}{Left 3}
hstr('','lln`;','{%}------------------------------------------------------------------------------{%}') #- latex line -#
hstr('','lhln`;','{%}---------------------------------------{%}') #- latex half line -#

#- for typesetting addicts -#
:R:loremipsum::Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

#- ;latex only, mostly document parts not for latex on javascript web pages. -#
;;document parts (good html constructus exist) + 

::sec`;::\section{{}{}}{Left 1}
::seca`;::\section{*}{{}{}}{Left 1} ; a for Asterisc
::ssec`;::\subsection{{}{}}{Left 1}
::sseca`;::\subsection{*}{{}{}}{Left 1}

::enum`;::\begin{{}enumerate{}}`r\item `r\item `r\end{{}enumerate{}}{Up 2}{End}
hstr('','itmm`;','\begin{{}itemize{}}`r\item `r\item `r\end{{}itemize{}}{Up 2}{End}')		#- ITeMMize -#
::desc`;::\begin{{}description{}}`r\item[]`r\item[]`r\end{{}description{}}{Up 2}{End}{Left}
hstr('R','ali`;','\begin{align}`r`r\end{align}')	    #- equation align -#

;;references (hard in javascrpit html...)
::lbl`;::\label{{}{}}{Left 1}
::eqrf`;::\eqRef{{}{}}{Left 1}
::ref`;::\ref{{}{}}{Left 1}
::cite`;::\cite{{}{}}{Left 1}

#-- mathematics. html or latex ------------------------------------------------------------#
::def`;::
if html = 1
    Send,<div class="definition">`r<div class="def-title"></div>`r<div class="def-body">`r`r</div>`r</div>{Up 4}{End}{Left 6}
else
    Send,\begin{{}definition{}}`r`r\end{{}definition{}}{Up 1}
return

::xpl`;::
if html = 1
    Send,<div class="example">`r<div class="exp-title"></div>`r<div class="exp-body">`r`r</div>`r</div>{Up 4}{End}{Left 6}
else
    Send,\begin{{}example{}}`r`r\end{{}example{}}{Up 1}
return

hstr('','cexp`;','<div class="counter-example">`r<div class="cexp-title"></div>`r<div class="cexp-body">`r`r</div>`r</div>{Up 4}{End}{Left 6}')	#- counter example -#
hstr('','rem`;','<div class="remark">`r<span class="rem-title"></span>`r<div class="rem-body">`r`r</div>`r</div>{Up 4}{End}{Left 6}')		#- remark -#

::theo`;::
if html = 1
    Send,<div class="theorem">`r<div class="theo-title"></div>`r<div class="theo-body">`r<div class="theo-hypothesis">`r`r</div>`r<div class="theo-conclusions">`r</div>`r`r</div>`r<div class="theo-proof"></div>`r</div>{Up 10}{End}{Left 6}
else
    Send,\begin{{}theorem{}}`r`r\end{{}theorem{}}{Up 1}
return

::algo`;::<div class="algorithm">`r<div class="algo-title"></div>`r<div class="algo-body">`r</div>`r</div>{Up 10}{End}{Left 6}

#-- wikipedia markup -----------------------------------------------------------#

hstr('','wexp`;','<blockquote><strong>Example</strong>`n</blockquote>{Up}{End}')	#- example -#

hstr('','mth`;','<math></math>{Left 7}')			#- equations -#

hstr('R','wcn`;','{{Citation needed}}')			#- citation needed -#
hstr('','wbf`;',"''''{Left 2}")				#- Bold Face -#

::htw\::	#- html to wikipedia markup. simple substitutions. -#
	StringReplace, clipboard, clipboard, \(, <math>, All
	StringReplace, clipboard, clipboard, \[, <math>, All
	StringReplace, clipboard, clipboard, \), </math>, All
	StringReplace, clipboard, clipboard, \], </math>, All
return

#-- c and cpp ------------------------------------------------------------------
::i`;::int `
::i`;::int[]{Left 1}
::f`;::float `
::f[`;::float[]{Left 1}
::d`;::double `
::d[`;::double[]{Left 1}

::if`;::if(){{}`n`n{}}{Up 2}{End}{Left 2}
::ifel`;::if(){{}`n`n{}} else {{}`n`n{}}{Up 4}{End}{Left 2}

hstr('','pt`;','{Backspace}->')	#- Dereference press then pt`; -#
hstr('','tsp;','this->')		#- this with dereference -#

:R:class`;::class className {`r    privateFields;`r  public:`r    publicFields;}`r}`;`r`r

::printf`;::printf("%%%",)`;{Left 6}
::cout`;::std{:}{:}cout << `

hstr('','ccm`;','// `')			#- c Line Coment -#
hstr('','cbcm`;','/*  */{Left 3}')	#- c block comment -#
hstr('','cln`;','//--  {- 60}//{Home}{Right 5}')	    #- ahk line -#
hstr('','chln`;','//--  {- 30}//{Home}{Right 5}')	    #- ahk half line -#

#-- python ------------------------------------------------------------#
:*:fori`;::for i=1:1000`r    `rend`r
:*:forj`;::for j=1:1000`r    `rend`r
::pcm`;::{#}-  -{#}{Left 3}
::phln`;::{#}-  {- 30}{#}{Home}{Right 3}
::pln`;::{#}-  {- 60}{#}{Home}{Right 3}
::pabc`;::{#}- added by ciro -{#}`n`n{#}-/ added by ciro -{#}{Up}

#------------------------------------------------------------------------------
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
		Send,{Enter}
    else
		Send,{Enter}{Up}
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

CapsLock & `;::
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
' & s::Send,^+{Tab}	#- left tab -#
' & d::Send,^{Tab}	#- right tab -#
' & f::Send,^t		#- new tab -#
' & g::Send,{F5}

#- bottom row -#
' & z::Send,^{Tab}	#- right tab -#
' & x::Send,^{Tab}	#- right tab -#
' & c::Send,^{Tab}	#- right tab -#
' & v::Send,^{Down}	#- Change engine down -#
' & b::Send,^{Up}	#- Change engine up -#

#-- right hand ------------------------#
#- windows -#

#- upper row -#
' & u::Send,^w		
' & i::Send,!{Tab 3}	#- up folder -#
' & o::Send,!{Tab 2}	#- before last page. tap to cycle three latest pages -#
' & p::Send,!{Tab}	#- last page -#

#- middle row -#
' & h::Send,^+{Tab 3}
' & j::Send,!{Left}	#- last folder -#
' & k::Send,!{Up}	#- up folder -#
' & l::Send,l		#- dummy-#
' & `;::Send,!{F4}	#- close window -#

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
StringReplace, Hotstring, Hotstring, `r`n, ``r, All  ; Using `r works better than `n in MS Word, etc.
StringReplace, Hotstring, Hotstring, `n, ``r, All
StringReplace, Hotstring, Hotstring, %A_Tab%, ``t, All
StringReplace, Hotstring, Hotstring, `;, ```;, All
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

:*:ol\::		#- toogle one letter words on off -#
if oneletters = 1
    oneletters = 0
else
    oneletters = 1
return

#IfWinNotActive ahk_class CabinetWClass ;Unbearable for Windows Explorer keyboard navigation

#-------------------------------------------------------------------------------#
#- straight scapes. even if not used, so you  dont have to remember which ones are used or not. -#
::a``::a
::b``::b
::c``::c
::d``::d 
::e``::e
::f``::f 
::g``::g 
::h``::h
::i``::i
::j``::j
::k``::k
::l``::l
::m``::m
::n``::n
::o``::o
::p``::p
::q``::q
::r``::r
::s``::s
::t``::t
::u``::u
::v``::v
::x``::x
::y``::y 
::z``::z 
::w``::w 

#Hotstring *0 o0 c	#- capitalization counts -#

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

:R:ab::about
:R:af::after 
:R:ag::again
:R:im::I'm
:R:ag::again
:R:alo::along
:R:al::also 
:R:ano::another
:R:ar::around
:R:aw::away 
:R:ba::back
:R:bc::because 
:R:bn::been
:R:bf::before 
:R:bl::below 
:R:bt::between
:R:bo::both
:R:ca::came
:R:cm::come
:R:cd::could
:R:dy::day
:R:dd::did
:R:df::different
:R:ds::does
:R:dt::don't
:R:dw::down 
:R:ea::each
:R:en::even
:R:ev::every
:R:fi::find
:R:ft::first
:R:fd::found
:R:fr::from
:R:dst::doesn't
:R:gv::give
:R:gd::good
:R:gr::great
:R:hv::have
:R:hp::help
:R:hr::here
::hv::have
::hl::help
::hr::here
::hm::home
::hou::house
::ju::just
::kn::know
::lr::large
::ls::last
::lf::left
::lk::like
::ln::line
::lt::little
::lg::long
::lo::look
::md::made
::mk::make
::mn::many
::mg::might
::mr::more
::ms::most
::mr.::Mr.	    
::mu::must
::nm::name
::nv::never
::nx::next
::nt::note
::nw::now
::nm::number
::oy::only
::ot::other
::ou::our
::ot::out
::ov::over
::ow::own
::pp::people
::pl::place
::rd::read
::rg::right
::sd::said
::sa::same ;avoid conflict with some (so exists already)
::sy::say
::se::seen so 
::sh::should
::sw::show
::sl::small
::sm::some
::smt::something
::snd::sound
::st::still
::su::such
::tk::take
::tl::tell
::th::than
::tt::that
::tm::them
::tn::then
::tr::there
::ths::these
::ty::they
::tg::thing
::tk::think
::ts::this
::ths::those
::thg::thought
::thr::three
::thg::through
::tm::time
::tg::together
::tw::two
::un::under
::vr::very
::wt::want
::wtr::water
::wy::way
::wel::well
::wa::what
::wn::when
::wr::where
::whc::which
::whl::while
::wl::will
::wi::with
::wk::work
::wd::word
::wrl::world
::wu::would
::wrt::write
::ye::year
::yo::your
::ws::was
:R:typ::type
:R:fr::fr
:R:from::from
:R:jq::jquery
:R:mj::MathJax
:R:rdm::README
:R:xtns::extensions
:R:thm::themes
:R:cntt::content
:R:lch::localhost
:R:mth::mathematics
:R:cls::class
:R:sty::style
:R:blg::blog
:R:dft::default
:R:btf::beautiful
:R:cmm::common
:R:func::function
:R:cntn::continuous
:R:prtl::partial
:R:interv::interval
:R:interpr::interpretation
:R:intui::intuitive
:R:vsl::visual
:R:symboy::symbolically
:R:cont::continuous
:R:ltt::little
:R:aro::around
:R:tn::then
:R:symbc::symbolic
:R:sml::small
:R:eno::enough
:R:pnt::point
:R:stl::still
:R:bcms::becomes
:R:clr::clear
:R:nd::need
:R:hyp::hypothesis
:R:kp::keep
:R:crs::course
:R:adjus::adjustment
:R:whc::which
:R:kps::keeps
:R:vl::value
:R:mgt::might
:R:xpc::expect
:R:varn::variation
:R:hypothesis::hypothesis
:R:hd::hard
:R:eff::effect
:R:cnn::cannot
:R:lrg::large
:R:hwv::however
:R:corre::correction
:R:wkg::working
:R:visu::visualize
:R:ins::inside
:R:rly::really
:R:spl::simple
:R:splr::simpler
:R:effv::effective
:R:rsn::reason
:R:hap::happy
:R:tch::teach
:R:ots::others
:R:evt::everything
:R:cmpl::complete
:R:cmply::completely
:R:ao::anyone
:R:knl::knowledge
:R:shld::should
:R:fl::feel
:R:pls::please
:R:tchg::teaching
:R:expsv::expensive
:R:tog::together
:R:thrf::Therefore
:R:alr::already
:R:src::source
:R:rth::rather
:R:si::site
:R:cmplxy::complexities
:R:blv::believe
:R:au::author
:R:fc::focus
:R:phy::physics
:R:shd::should
:R:lrn::learn
:R:mat::material
:R:cp::cope
:R:ct::cost
:R:tchg::teaching
:R:cms::comes
:R:smw::somewhat
:R:oft::often
:R:wio::without
:R:coop::cooperation
:R:abv::above
:R:tgs::things
:R:cent::centuries
:R:yrs::years
:R:mks::makes
:R:hs::has
:R:spc::space
:R:ltr::letter
:R:thrg::through
:R:inet::internet
:R:thgt::thought
:R:thgts::thoughts
:R:pnts::points
:R:spey::specially
:R:mc::much
:R:moti::motivation
:R:lrng::learning
:R:bcms::becomes
:R:dfc::difficult
:R:motid::motivated
:R:oblid::obliged
:R:fcs::focus
:R:srcs::sources
:R:prb::problem
:R:dgt::digital
:R:mtd::method
:R:tms::times
:R:aml::almost
:R:zr::zero
:R:cmpts::Computers
:R:emph::emphasis
:R:comp::computer
:R:xp::example
:R:tchrs::teachers
:R:btr::better
:R:fls::flash
:R:wc::which
:R:manip::manipulate
:R:distrd::distributed
:R:possibs::possibilities
:R:eit::either
:R:smpy::simply
:R:refs::references
:R:explic::explication
:R:td::to do
:R:comps::computers
:R:qsts::questions
:R:math::mathematics
:R:adv::advanced
:R:mt::most
:R:cs::case
:R:spcf::specify
:R:spcfc::specific
:R:def::define
:R:dervs::derivatives
:R:ans::answer
:R:trf::therefore
:R:cnt::center
:R:img::image
:R:parab::parabolic
:R:prbc::parabolic
:R:exps::examples
:R:mtrs::matters
:R:cncr::concrete
:R:sps::suppose
:R:pln::plane
:R:eqs::equals
:R:alw::always
:R:gxy::G(x,y)
:R:adj::adjustment
:R:nc::nice
:R:frtm::furthermore
:R:crr::correct
:R:crrn::correction
:R:lts::let's
:R:crc::circle
:R:otoh::on the other hand
:R:sv::save
:R:xpl::explicit
:R:qst::question
:R:mjry::majority
:R:funcs::functions
:R:tho::those
:R:usf::useful
:R:xsts::exists
:R:xstc::existence
:R:ppts::properties
:R:cld::called
:R:impl::implicit
:R:xcty::exactly
:R:polyn::polynomial
:R:sc::since
:R:slv::solve
:R:dsr::desire
:R:ptcly::Particularly
:R:vrat::variation
:R:sol::solution
:R:shl::shall
:R:mtvtn::Motivation
:R:tft::the fact that
:R:iltts::illustrates
:R:gvs::gives
:R:rglry::regularity
:R:rt::rather
:R:res::result
:R:wv::we've
:R:enj::enjoy
:R:kng::knowing
:R:hstt::hesitate
:R:sggn::suggestion
:R:prt::print
:R:psb::possible
:R:correction::correction
:R:intv::interval
:R:rst::result
:R:ocs::of course
:R:xmn::examine
:R:hpns::happens
:R:pg::page
:R:lcp::landscape
:R:cds::Ciro Duran Santilli
:R:ttrl::tutorial
:R:clsn::collision
:R:tkn::taken
:R:gpcs::graphics
:R:spd::speed
:R:evrm::environment
:R:fx::for example
:R:inp::input
:R:ahk::autohotkey
:R:cmr::camera
:R:pt::part
:R:rbt::robot
:R:opt::output
:R:sta::start
:R:scs::showcase
:R:fdtns::foundations
:R:fdmt::fundamental 
:R:fie::field
:R:qs::questions
:R:isf::itself
:R:ress::results
:R:incl::include
:R:sua::such as
:R:perh::Perhaps
:R:abrn::abbreviation
:R:ld::lead
:R:bcm::become
:R:abrd::abbreviated
:R:o::one
:R:dmnt::dominate
:R:dmntg::dominating
:R:stag::starting
:R:tx::text
:R:col::color
:R:ei::either
:R:ddn::did not
:R:ppsn::proposition
:R:diff::difficult
:R:dif::difficult
:R:prv::prove
:R:intun::intuition
:R:oc::once
:R:ey::easy
:R:esl::easily
:R:sci::science
:R:ftr::future
:R:dn::done
:R:lang::language
:R:mthl::mathematical
:R:args::arguments
:R:che::check
:R:fml::formal
:R:prcsy::precisely
:R:ambig::ambiguity
:R:gtr::guitar
:R:sys::system
:R:mathematical::mathematical
:R:op::open
:R:uni::university
:R:ta::than
:R:wo::without
:R:csfctn::classification
:R:clod::closed
:R:sfcs::surfaces
:R:ed::edit
:R:scr::script
:R:scrs::scripts
:R:hstr::hotstring
:R:prog::program
:R:wdw::windows
:R:xplo::explorer
:R:xplrr::explore
:R:applis::applications
:R:flw::follow
:R:flwg::following
:R:prop::property
:R:props::properties
:R:desp::despite
:R:spcy::simplicity
:R:gros::groups
:R:mtvn::motivation
:R:cond::condition
:R:guars::guarantees
:R:check::check
:R:difeq::differential equation
:R:eqn::equation
:R:symms::symmetries
:R:cpx::complex
:R:strc::structure
:R:strcs::structures
:R:cofsg::classification of finite simple groups
:R:obj::object
:R:multn::multiplication
:R:mult::multiply
:R:ti::their
:R:thrm::theorem
:R:thry::theory
:R:eb::ebooks
:R:exer::exercises
:R:unt::until
:R:tod::today
:R:defn::definition
:R:hpn::happen
:R:happens::happens
:R:grp::group
:R:grps::groups
:R:intro::introduction
:R:satisg::satisfying
:R:imdy::immediately
:R:imd::immediate
:R:rtns::rationals
:R:tgl::toggle
:R:seld::selected
:R:satis::satisfy
:R:clasn::classification
:R:cofabg::classification of finite abelian groups
:R:gnr::general
:R:invs::inverses
:R:comuy::commutativity
:R:comuv::commutative
:R:cgrp::commutative group
:R:agrp::abelian group
:R:pia::piano
:R:ndd::needed
:R:reqd::required
:R:alge::algebra
:R:algec::algebraic
:R:proby::probably
:R:alea::at least
:R:inft::infinite
:R:infy::infinitely
:R:pstn::position
:R:elems::elements
:R:cntr::counter
:R:cexp::counter example
:R:addn::addition
:R:rl::real
:R:nbs::numbers
:R:fm::form
:R:wrest::with respect to
:R:cho::choose
:R:vrf::verify
:R:jscr::javascript
:R:ccpt::concept
:R:ccpts::concepts
:R:xec::execution
:R:ord::order
:R:otw::otherwise
:R:bsc::basic
:R:sax::saxophone
:R:ltx::latex
:R:fdr::folder
:R:general::general
:R:philo::philosophy
:R:descrs::describres
:R:cnstrn::Construction
:R:msrb::measurable
:R:trnsf::transform
:R:frr::fourrier
:R:ftrns::fourrier transform
:R:topol::topololgy
:R:dtl::detail
:R:trum::trumpet
:R:iot:in order to
:R:prcs::precise
:R:sound::seen
:R:prfs::proofs
:R:flg::feeling
:R:wrtn::written
:R:dfn::define
:R:sn::soon
:R:mathematical::mathematical
:R:sttm::statement
:R:illus::illustrate
:R:achi::achieve
:R:re::real
:R:flang::formal language
:R:sttms::statements
:R:alts::alternatives
:R:sns::sense
:R:udt::understand
:R:fst::first
:R:ho::hope
:R:conv::convince
:R:theos::theorems
:R:os::ones
:R:trg::trying
:R:consi::consider
:R:equiv::equivalent
:R:fvrt::favorite
:R:sttd::started
:R:devm::development
:R:bss::basis
:R:fdts::foundations
:R:mysto::mysterious
:R:objs::objects
:R:dict::dictionary
:R:oril::original
:R:prf::proof
:R:extl::external
:R:xtnl::External
:R:rscs::resources
:R:arti::article
:R:natu::natural
:R:general::general
:R:comm::comment
:R:asap::as soon as possible
:R:dp::deep
:R:axm::axiom
:R:ansg::answering
:R:specific::specific
:R:cheg::checking
:R:qt::quite
:R:chars::characters
:R:calc::calculus
:R:bk::book
:R:syss::systems
:R:frml::formal
:R:proofs::proofs
:R:gm::game
:R:sha::shall
:R:ltrs::letters
:R:alpb::alphabet
:R:reg::regular
:R:bhvs::behaves
:R:seqs::sequences
:R:seq::sequence
:R:phr::phrase
:R:vals::values
:R:eao::each one
:R:tfmt::transformation
:R:rls::rules
:R:phrs::phrases
:R:xprs::express
:R:afirms::affirmations
:R:afirm::affirmation
:R:dbl::double
:R:sns::sense
:R:philol::philosophical
:R:discun::discussion
:R:fundl::fundamental
:R:oprtn::operation
:R:sk::skip
:R:descrn::description
:R:dcptn::description
:R:ys::yourself
:R:yrsf::yourself
:R:jtfns::justifications
:R:chr::character
:R:consts::constants
:R:nbrs::numbers
:R:nnbrs::natural numbers
:R:unq::unique
:R:emp::empty
:R:clry::clearly
:R:unqy::uniquely
:R:frt::further
:R:bty::beauty
:R:ops::opens
:R:cpctd::complicated
:R:vrb::variable
:R:acty::actually
:R:xcp::except
:R:prvg::proving
:R:prvd::proved
:R:mns::means
:R:prj::project
:R:inst::instead
:R:trsl::translate
:R:gnrlz::generalize
:R:cte::constant
:R:dfns::defines
:R:trsld::translated
:R:ho::hope
:R:cmp::computer
:R:ae::able
:R:rea::reach
:R:anss::answers
:R:cnv::convince
:R:rpr::represent
:R:flws::follows
:R:knn::known
:R:fsys::formal system
:R:itrtg::interesting
:R:stts::states
:R:powf::powerful
:R:techq::technique
:R:cphs::comprehensive
:R:fncs::functions
:R:elems::elements
:R:sym::symbol
:R:cvgc::convergence
:R:xpnl::exponential
:R:defns::definitions
:R:intu::intuition
:R:tls::tells
:R:ntg::nothing
:R:lbl::little by little
:R:atg::anything
:R:atc::article
:R:opn::opinion
:R:mthcs::mathematicians
:R:prgms::programs
:R:dife::different
:R:aum::automatic
:R:stri::string
:R:ctr::center
:R:tbl::table
:R:ru::rule
:R:oprtns::operations
:R:oprtn::operation
:R:sec::second
:R:pos::position
:R:wei::weight
:R:gs::goes
:R:oprtn::operation
:R:oprtns::operations
:R:jtf::justify
:R:nb::number
:R:chrs::characters
:R:pts::points
:R:hg::high
:R:thi::think
:R:afmtn::affirmation
:R:tu::true
:R:prvn::proven
:R:afmtns::affirmations
:R:xpln::explain
:R:ccs::conclusion
:R:pcs::precise
:R:htks::hotkeys
:R:htk::hotkey
:R:cvcd::convinced
:R:cpr::compare
:R:smo::someone
:R:cptr::computer
:R:sla::so long as
:R:agr::agree
:R:dfrc::difference
:R:wds::words
:R:ud::used
:R:eng::English
:R:tmn::too many
:R:mtp::multiple
:R:wld::world
:R:bsd::based
:R:mthns::mathematicians
:R:sr::sure
:R:er::error
:R:oao::over and over
:R:tmsv::themselves
:R:itrtg::interesting
:R:smrzs::summarizes
:R:ctx::context
:R:plc::place
:R:bnf::benefit
:R:sstv::sensitive
:R:fdtns::foundations
:R:ntcd::noticed
:R:ss::sense
:R:eqv::equivalent
:R:pfd::profound
:R:ifec::influence
:R:ppsd::proposed
:R:chc::choice
:R:dvlp::develop
:R:pplr::popular
:R:gnrly::generally
:R:cls::close
:R:atck::attack
:R:dvsn::division
:R:stro::strong
:R:pow::power
:R:srs::series
:R:pwr::power
:R:psrs::power series
:R:evw::everywhere
:R:hlmp::holomorphic
:R:yr::your
:R:eqtn::equation
:R:tms\::\times
:R:dfntn::definition
:R:sltn::solution
:R:difeqs::differential equations
:R:psrs::power series
:R:itscs::in this case
:*:pr\::()
:R:invs::inverse
:R:lkg::looking
:R:mtx::matrix
:R:eucln::Euclidean
:R:cvgc::convergence
:R:trc::trace
:R:ifnt::infinite
:R:fnt::finite
:R:jrdn::Jordan
:R:dcpsn::decomposition
:R:tdtnl::traditional
:R:msc::music
:R:kbd::keyboard
:R:hf::half
:R:itfp::in the first place
:R:cns::chinese
:R:fftft::follows from the fact that
:R:taglr::triangular
:R:sgrp::subgroup
:R:ivtb::invertible
:R:dagn::diagonal
:R:mtxs::matrices
:R:pstv::positive
:R:coefs::coefficients
:R:diag::diagonal
:R:dmtx::diagonal matrix
:R:egvl::eigenvalue
:R:egvls::eigenvalues
:R:bij::bijection
:R:oto::one-to-one
:R:eqvln::equivalent
:R:wdfnd::well defined
:R:aotf::are of the form
:R:dfnd::defined
:R:ovoy::obviously
:R:rst::reset
:R:qt::quite
:R:mnfd::manifold
:R:btm::bottom
:R:bfr::beforer
:R:lgrp::Lie group
:R:exp::exponential
:R:xpnt::exponential
:R:opsgrps::one-parameter subgroups
:R:opsgrp::one-parameter subgroup
:R:agb::algebra
:R:lagb::Lie algebra
:R:lgrps::Lie groups
:R:dmnfd::differentiable manifold
:R:stt::such that
:R:vspc::vector space
:R:eqrel::equivalence relation
:R:lgexp::Lie group exponential
:R:assocd::associated
:R:neig::neighborhood
:R:amth::applied mathematics
:R:rtt::rather than
