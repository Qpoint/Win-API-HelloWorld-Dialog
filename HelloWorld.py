# Referance Link https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxa.
# Import the required module to handle Windows API Calls
import ctypes

# Grab a handle to User32.dll & kernel32.dll
dll_handle = ctypes.WinDLL("User32.dll")
k_handle = ctypes.WinDLL("Kernel32.dll")

# Win API Call
# int MessageBoxA(
# HWND hWnd,
# LPCTSTR lpText,
# LPCTSTR lpCaption,
# UINT, uType
# );

# Setting Up The Params
hWnd = None
lpText = 'Hello World'
lpCaption = 'Hello Students!'
uType = 0x00000002 # switch utype to change output dialog.


# Calling the Windows API Call
response = dll_handle.MessageBoxW(hWnd, lpText, lpCaption, uType)

# Check For Errors
error = k_handle.GetLastError()
if error != 0:
	print("Error Code: {0}".format(error))
	exit(1)

# Check What The User Clicked
if response == 3:
	print("Clicked Abort!")
elif response == 4:
	print("User Retry!")
elif response == 5:
    print("Clicked Ignore!")

