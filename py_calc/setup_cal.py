from cx_Freeze import setup, Executable
setup(
    name = "Py Calculator",
    version = "1.0.0",
    options = {"build_exe": {
        'packages': ["wx"],
        'include_msvcr': True,
    }},
    executables = [Executable("calculator.py",base="Win32GUI")]
    )