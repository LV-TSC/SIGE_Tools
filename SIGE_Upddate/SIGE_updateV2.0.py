import os
import time
from tkinter import messagebox

ordcorte = os.path.isfile("start C:\\TSC\\SIGE\\D01OrdCorte.exe")

def update_usercontrol():
    os.system('"regsvr32 /s "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\ACTBUTTO.ocx"')
    os.system('"regsvr32 /s "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\FuncButt.ocx"')
    os.system('"regsvr32 /s "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\FuncButtdotNet.ocx"')
    os.system('"regsvr32 /s "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\MantenimientosDoNet.ocx"')
    os.system('"regsvr32 /s "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\Mantenimientos.ocx"')
    os.system('"regsvr32 /s "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\GridEX20.ocx"')
    os.system('"regsvr32 /s "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\MDIExtender.ocx"')
    os.system('"regsvr32 /s "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\MSDATGRD.ocx"')
    os.system('"regsvr32 /s "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\NumBox.ocx"')
    os.system('"regsvr32 /s "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\msdxm.ocx"')
    os.system('"regsvr32 /s "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\ChamaleonButton.ocx"')
    os.system('"regsvr32 /s "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\FloatButton.ocx"')
    os.system('"regsvr32 /s "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\MSMASK32.OCX"')
    os.system('"regsvr32 /s "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\prjKEXPCheck.ocx"')
    os.system('"regsvr32 /s "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\tabctl32.ocx"')
    os.system('"regsvr32 /s "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\tbarcode5.ocx"')
    os.system('"regsvr32 /s "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\aspsmartmail.dll"')
    os.system('"regsvr32 /s "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\MSDATlst.ocx"')
    os.system('"regsvr32 /s "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\mscomct2.ocx"')
    os.system('"regsvr32 /s "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\labels.ocx"')
    os.system('"regsvr32 /s "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\comdlg32.ocx"')
    os.system('"regsvr32 /s "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\ssdw3b32.ocx"')
    os.system('"regsvr32 /s "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\IGResizer40.ocx"')
    os.system('"regsvr32 /s "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\MSADODC.OCX"')
    os.system('"regsvr32 /s "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\MSCAL.OCX"')
    os.system('"regsvr32 /s "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\LibraryVB.dll"')
    os.system('"regsvr32 /s "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\doNetControls.ocx"')

def update_dll():
    os.system("regsvr32.exe /s FuncButt.ocx")
    os.system("regsvr32.exe /s GridEX20.ocx")
    os.system("regsvr32.exe /s labels.ocx")
    os.system("regsvr32.exe /s LIBRAR~1.DLL")
    os.system("regsvr32.exe /s Mantenimientos.ocx")
    os.system("regsvr32.exe /s MDIExtender.ocx")
    os.system("regsvr32.exe /s MSCOMCT2.OCX")
    os.system("regsvr32.exe /s MSDATGRD.OCX")
    os.system("regsvr32.exe /s MSMASK32.OCX")
    os.system("regsvr32.exe /s MSSTDFMT.DLL")
    os.system("regsvr32.exe /s msvbvm60.dll")
    os.system("regsvr32.exe /s scrrun.dll")

def cerrar_procesos():
    os.system("taskkill /f /im GestionEmpresarial_Produccion.exe")
    os.system("taskkill /f /im D01OrdCorte.exe")
    time.sleep(2)

def abrir_SIGE():
    print("Abrir SIGE")
    os.system("start C:\\TSC\\SIGE\\SIGE.bat")
    time.sleep(2)
    
try:
    cerrar_procesos()
    abrir_SIGE()
    cerrar_procesos()
    update_usercontrol()

    print("ejecutar d01ordcorte")
    os.system("start C:\\TSC\\SIGE\\D01OrdCorte.exe")
    time.sleep(2)

    cerrar_procesos()

    print("Borrar REGEDIT")
    os.system('"REG DELETE "HKEY_CLASSES_ROOT\D01OrdCorte.clsForm\Clsid" /f"')
    os.system('"REG DELETE "HKEY_CLASSES_ROOT\WOW6432Node\CLSID\{9F2B5F37-C713-468E-BF7A-9FAD8FAA8320}" /f"')
    time.sleep(2)

    print("Borrar archivo D01OrdCorte")
    if ordcorte == True:
        os.remove("C:\\TSC\\SIGE\\D01OrdCorte.exe")
        time.sleep(2)
    else:
        print("No existe el archivo")

    print("copiar archhivos como administrador")
    os.system("copy /Y /V C:\\TSC\\SIGE\RegistrarOcxvb6\\*   C:\Windows\\System32\\")
    os.system("copy /Y /V C:\\TSC\\SIGE\RegistrarOcxvb6\\*   C:\Windows\\SysWoW64\\")
    time.sleep(1)

    print("EJECUTAR DLL")
    os.chdir("C:\\Windows\\System32")
    update_dll()
    time.sleep(2)
    os.chdir("C:\\Windows\\SysWOW64")
    update_dll()
    time.sleep(2)

    abrir_SIGE()
    time.sleep(2)
    cerrar_procesos()

    print("ejecutar d01ordcorte")
    os.system("start C:\\TSC\\SIGE\\D01OrdCorte.exe")
    time.sleep(2)

    abrir_SIGE()
    time.sleep(2)

    print("FINAL")
    os.system("taskkill /f /im GestionEmpresarial_Produccion.exe")

    messagebox.showinfo(message="Se realizo la actualización del SIGE", title="Actualizacion del SIGE")

except:
    messagebox.showerror(message="Hubo un problema con la actualización del SIGE", title="Actualizacion del SIGE")


finally:
    print("ejecutar d01ordcorte")
    os.system("start C:\\TSC\\SIGE\\D01OrdCorte.exe")
    time.sleep(2)