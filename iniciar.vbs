' Arranca el servidor de Texto a Voz en segundo plano (sin ventana).
Set fso = CreateObject("Scripting.FileSystemObject")
carpeta = fso.GetParentFolderName(WScript.ScriptFullName)
Set shell = CreateObject("WScript.Shell")
shell.CurrentDirectory = carpeta
shell.Run "pythonw """ & carpeta & "\app.py""", 0, False
