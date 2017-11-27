import cx_Freeze
import os
executables = [cx_Freeze.Executable("main.py")]


cx_Freeze.setup(
    name = "CachimboBros",
    options = {"build_exe":{"packages":["pygame"],
                            "include_files":["source",
                                             "assets"]}},
    executables = executables,
    version='1.0.0'
    )
