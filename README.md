# geospatial repo
PostGIS 2.1.5 for GreenPlum 5.x+

## Licence
This project is developed under GPL v2, because PostGIS is GPL v2.

## How to compile it
To compile geospatial form source code, please install the follow third-party
libraries first by following README.libs.
For normal use without raster, please install json-c, geos and proj.4
To enbale raster function, plese install gdal and expat. The minimum version
requirments are listed in Makefile.version.

Before setup the geospatial, please make sure the GPDB is installed correctly.
To compile and install geospatial, use following command:

```
./configure --with-pgconfig="Your gpdb location"/bin/pg_config --with-raster --without-topology --prefix=$GPHOME
make
make install	
```

If you build from
the extended PostGIS-2.x directory, you may compile with the following command:

```
make USE_PGXS=1 clean all install
```

Here USE_PGXS will specify the correct install path to gpdb.

## How to use it
After installing geospatial extention, run the following commands to enable it:

```
psql -d mydatabase -f ${GPHOME}/share/postgresql/contrib/postgis-2.1/postgis.sql
psql -d mydatabase -f ${GPHOME}/share/postgresql/contrib/postgis-2.1/postgis_comments.sql
psql -d mydatabase -f ${GPHOME}/share/postgresql/contrib/postgis-2.1/rtpostgis.sql
psql -d mydatabase -f ${GPHOME}/share/postgresql/contrib/postgis-2.1/raster_comments.sql
```

Besides, to configure raster utilities, please set following variables into env of both master and segments. A suggested way to do this is to add those variable settings into your `$GPHOME/greenplum_path.sh` file to ensure they get set in all the segments. After setting them, restart the database.

```
export GDAL_DATA=$GPHOME/share/gdal
export POSTGIS_ENABLE_OUTDB_RASTERS=0
export POSTGIS_GDAL_ENABLED_DRIVERS=DISABLE_ALL
```

Note: by default, all the gdal drivers are disabled. To enable specific types of gdal driver, please refer to this [postgis manual](http://postgis.net/docs/manual-2.1/postgis_installation.html#install_short_version). An example can be like this:

```
POSTGIS_GDAL_ENABLED_DRIVERS="GTiff PNG JPEG GIF XYZ"
```

In near future we plan to move them in GUCs after we backport necessary features onto gpdb repo.

## Sub-directories under planing
1. postgis
  * geometry
  * raster
2. trajectory
3. utilities

## Last update date
Jingyi Mei, Nov 27th, 2017	
Kuien Liu, Haozhou Wawng, 26 May 2016
