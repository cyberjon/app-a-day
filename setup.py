from cx_Freeze import setup, Executable
setup(
    name = "Address Book",
    version = "1.0.0",
    options = {"build_exe": {
        'packages': ["wx","sqlite3"],
        'include_files': ['address_book.db'],
        'include_msvcr': True,
    }},
    executables = [Executable("address_book.py",base="Win32GUI")]
    )