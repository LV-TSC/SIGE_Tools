import os, sys

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout
        
with HiddenPrints():
    os.system('"regsvr32 "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\ACTBUTTO.ocx"')
    os.system('"regsvr32 "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\FuncButt.ocx"')
    os.system('"regsvr32 "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\FuncButtdotNet.ocx"')
    os.system('"regsvr32 "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\MantenimientosDoNet.ocx"')
    os.system('"regsvr32 "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\Mantenimientos.ocx"')
    os.system('"regsvr32 "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\GridEX20.ocx"')
    os.system('"regsvr32 "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\MDIExtender.ocx"')
    os.system('"regsvr32 "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\MSDATGRD.ocx"')
    os.system('"regsvr32 "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\NumBox.ocx"')
    os.system('"regsvr32 "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\msdxm.ocx"')
    os.system('"regsvr32 "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\ChamaleonButton.ocx"')
    os.system('"regsvr32 "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\FloatButton.ocx"')
    os.system('"regsvr32 "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\MSMASK32.OCX"')
    os.system('"regsvr32 "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\prjKEXPCheck.ocx"')
    os.system('"regsvr32 "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\tabctl32.ocx"')
    os.system('"regsvr32 "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\tbarcode5.ocx"')
    os.system('"regsvr32 "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\aspsmartmail.dll"')
    os.system('"regsvr32 "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\MSDATlst.ocx"')
    os.system('"regsvr32 "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\mscomct2.ocx"')
    os.system('"regsvr32 "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\labels.ocx"')
    os.system('"regsvr32 "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\comdlg32.ocx"')
    os.system('"regsvr32 "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\ssdw3b32.ocx"')
    os.system('"regsvr32 "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\IGResizer40.ocx"')
    os.system('"regsvr32 "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\MSADODC.OCX"')
    os.system('"regsvr32 "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\MSCAL.OCX"')
    os.system('"regsvr32 "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\LibraryVB.dll"')
    os.system('"regsvr32 "C:\\TSC\\SIGE\\_SIGEUserControlsVB6\\doNetControls.ocx"')
 
print('Will be printed')