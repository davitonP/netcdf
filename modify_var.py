import netCDF4 as nc
import numpy as np
toexclude = []


with nc.Dataset("files_test/copy.nc","r+",format="NETCDF4") as src:
    for name, variable in src.variables.items():
        if name not in toexclude:
            if name == "time":
                src.variables[name][:] = 12
