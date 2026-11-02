# Hace que Texto a Voz arranque solo al iniciar sesión en Windows
# y crea un acceso directo "Texto a Voz" en el escritorio.
# Para deshacerlo: borra "Texto a Voz.lnk" de la carpeta shell:startup.
$d = $PSScriptRoot
$sh = New-Object -ComObject WScript.Shell
$lnk = $sh.CreateShortcut("$([Environment]::GetFolderPath('Startup'))\Texto a Voz.lnk")
$lnk.TargetPath = "wscript.exe"
$lnk.Arguments = "`"$d\iniciar.vbs`""
$lnk.WorkingDirectory = $d
$lnk.Save()
Set-Content -Path "$([Environment]::GetFolderPath('Desktop'))\Texto a Voz.url" -Value "[InternetShortcut]`r`nURL=http://localhost:5050/"
Write-Host "Listo: Texto a Voz arrancará solo y tienes el acceso directo en el escritorio."
