# geospatial repo
PostGIS 2.1.5 for GreenPlum 5.x+

## License
This project is developed under GPL v2, because PostGIS is GPL v2.

## How to compile it
Currently, we support building geospatial on rhel/centos. To compile geospatial form source code, please install the following third-party libraries as described in [README.libs](https://github.com/greenplum-db/geospatial/blob/master/postgis/README.libs).
For normal use without raster, please install json-c, geos and proj.4.
To enable raster functionality, please install gdal and expat. The minimum version requirments are listed in [Makefile.version](https://github.com/greenplum-db/geospatial/blob/master/postgis/Makefile.version).

Before setting up geospatial, please make sure GPDB is installed correctly.
To compile and install geospatial, use following command:

```
cd postgis/build/postgis-2.1.5/
./configure --with-pgconfig=$GPHOME/bin/pg_config --with-raster --without-topology --prefix=$GPHOME
make USE_PGXS=1 clean all install	
```

Here USE_PGXS will specify the correct install path to gpdb.

Note that if psql is in path, there is no need to use --with-pgconfig flag.

## How to use it
After installing geospatial extension, run the following commands to enable it:

```
psql -d mydatabase -f ${GPHOME}/share/postgresql/contrib/postgis-2.1/postgis.sql
psql -d mydatabase -f ${GPHOME}/share/postgresql/contrib/postgis-2.1/postgis_comments.sql
psql -d mydatabase -f ${GPHOME}/share/postgresql/contrib/postgis-2.1/rtpostgis.sql
psql -d mydatabase -f ${GPHOME}/share/postgresql/contrib/postgis-2.1/raster_comments.sql
```

To configure raster utilities, please set the following environment variables on the master host and all the segment hosts. A suggested way to do this is to add these variables into your `$GPHOME/greenplum_path.sh` file to ensure they get set in all the segment hosts and the master host. **Make sure that you restart the database after setting them**.

```
export GDAL_DATA=$GPHOME/share/gdal
export POSTGIS_ENABLE_OUTDB_RASTERS=0
export POSTGIS_GDAL_ENABLED_DRIVERS=DISABLE_ALL
```

Note: to guarantee that `make check` test cases run correctly, all the gdal drivers are disabled. To enable specific types of gdal drivers for a certain use case, please refer to this [postgis manual](http://postgis.net/docs/manual-2.1/postgis_installation.html#install_short_version). An example can be like this:

```
POSTGIS_GDAL_ENABLED_DRIVERS="GTiff PNG JPEG GIF XYZ"
```
In near future we plan to create GUCs for these variables after we backport necessary features into the gpdb repository.

## Workaround for missing .so files

If any of the third party libraries are not installed in the default system path, you may see this issue while running the postgis.sql file
```sql
psql -d mydatabase -f ${GPHOME}/share/postgresql/contrib/postgis-2.1/postgis.sql
postgis-2.1.so": libgeos_c.so.1: cannot open shared object file: No such file or directory
```

This may happen because `postgis.so` cannot find one or more of the third party .so files to link against. Here is a workaround

1. Edit /etc/ld.so.conf and add all the non default library paths that are used by geospatial.

For e.g. if you compiled and installed `proj` in /tmp/proj-install, this is how
   /etc/ld.so.conf would look like
```
   include ld.so.conf.d/*.conf
   /tmp/proj-install/lib
```
2. Run ldconfig

## Sub-directories under planing
1. postgis
  * geometry
  * raster
2. trajectory
3. utilities

## Last update date
Jingyi Mei, Nov 28th, 2017	

Kuien Liu, Haozhou Wawng, 26 May 2016
