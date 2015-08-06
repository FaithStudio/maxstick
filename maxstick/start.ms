(
    local thisdir = getFilenamePath (getThisScriptFilename())
    local pyscript = pathConfig.appendPath thisdir "__init__.py"
    python.executeFile pyscript
)