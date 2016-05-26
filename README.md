# geospatial repo

## licence

This project is developing under GPL v2, because PostGIS is GPL v2.

## sub-directories under planing
1. postgis
  * geometry
  * raster
2. trajectory
3. utilities

## how to compile it
To compile geospatial form source code, please install the follow third-party
libraries first by following README.libs.
For normal use without raster, please install json-c, geos and proj.4
To enbale raster function, plese install gdal and expat. The minimum version
requirments are listed in Makefile.version.

Before setup the geospatial, please make sure the GPDB is installed correctly. 
To configure the geospatial, please use following command:
```
./configure --with-pgconfig="Your gpdb location"/bin/pg_config --with-raster
--without-topology --prefix=$GPHOME
```

If configuration is successfully, then please run _make_ to compile the geospatial
and run make install to install the geospatial to the GPDB. If you build from
the extended PostGIS-2.x directory, you may compile with following command:
```
make USE_PGXS=1 clean all install 
```
Here USE_PGXS will specify the correct install path to gpdb.


## how to distribute it
The geospatial has bulit-in function to build the geospatial as a gppkg to allow
user to install the geospatial directly into GPDB without compiling. 

To build the gppkg, please make sure the source code of GPDB is downloaded and 
```make sync_tools``` is run correctly. 

After this, go to _package_ folder and run ./build.sh or following command to build the gppkg
automaticly. 
```
make BLD_TARGETS="gppkg" \
	BLD_ARCH="rhel5_x86_64" \
	BLD_TOP="Your_gpdb_source_location/gpAux" \
	INSTLOC="Your_gpdb_installation_location/" \
	gppkg
```

## how to use it
After you installed geospatial extention, run following commands to enable it:
```
psql -d mydatabase -f ${GPHOME}/share/postgresql/contrib/postgis-2.1/*.sql
```

The most commonly used files include:
1. postgis.sql
2. postgis_comments.sql
3. spatial_ref_sys.sql
4. rtpostgis.sql
5. raster_comments.sql

Besides, to configure raster utilities, please set following variables into env of both
master and segments, and restart the databases.
```
export GDAL_DATA=$GPHOME/share/gdal
export POSTGIS_ENABLE_OUTDB_RASTERS=0
export POSTGIS_GDAL_ENABLED_DRIVERS=DISABLE_ALL
```

In near future we plan to move them in GUCs after we backport necessary features
onto gpdb repo.

## last update date
	Kuien Liu, Haozhou Wawng, 26 May 2016
