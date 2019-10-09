from cx_Freeze import setup, Executable
setup(
    name = "Pandas For Peopel",
    version = "1.0.0",
    options = {"build_exe": {
        'packages': ["wx","pandas"],
        'include_msvcr': True,
    }},
    executables = [Executable("p4p.py",base="Win32GUI")]
    )