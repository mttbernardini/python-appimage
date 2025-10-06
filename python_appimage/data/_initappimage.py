# This is a patch to getpath. It must execute before site.main() is called
def _initappimage():
    """Initialise executable name when running from an AppImage."""
    import os
    import sys

    env = os.environ
    try:
        command = env["APPIMAGE_COMMAND"]
    except KeyError:
        return

    if command and ("APPDIR" in env):
        command = os.path.abspath(command)
        sys.executable = command
        sys._base_executable = command
    
    # unset AppImage variables to ensure transparent environment
    env.pop("APPIMAGE_COMMAND", None)
    env.pop("APPIMAGE", None)
    env.pop("APPDIR", None)

_initappimage()
del _initappimage
