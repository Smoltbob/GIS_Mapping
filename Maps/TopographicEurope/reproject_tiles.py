import processing
import glob
import os
from qgis.core import QgsCoordinateReferenceSystem, QgsMessageLog

"""
Runs processing commands on iterated files of a folder.
"""

input_path = "DTM Europe 3asec v19 by Sonny"
out_path = os.path.join(input_path, "out")

if not os.path.exists(out_path):
    QgsMessageLog.logMessage(f"Creating {out_file}", 'ReprojectTilesScript')
    os.makedirs(out_path)

input_files = glob.glob(os.path.join(input_path, "*.hgt"))
for input_file in input_files:
    out_file = os.path.join(out_path, os.path.basename(input_file))
    out_file = out_file.rsplit('.', 1)[0] + '.tif' # replace hgt by tif
    out_file_hill = out_file.rsplit('.', 1)[0] + 'hill.tif'

    processing.run(
    "gdal:warpreproject", {
    'INPUT':input_file,
    'SOURCE_CRS':None,
    'TARGET_CRS':QgsCoordinateReferenceSystem('EPSG:3035'), # EU CRS
    'RESAMPLING':0,'NODATA':None,'TARGET_RESOLUTION':None,'OPTIONS':'','DATA_TYPE':0,'TARGET_EXTENT':None,'TARGET_EXTENT_CRS':None,'MULTITHREADING':False,'EXTRA':'',
    'OUTPUT':out_file})


    