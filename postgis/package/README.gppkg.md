Notes for generating gppkg with pre-compiled libraries

### 1. Download 3rd party libraries

======================================

To build postgis gppkg, we first need to download the third-party libraries from
lvy repo by using make sync_tools provided by gpdb.

Usage:
-  located to gpdb/gpAux folder
-  run make sync_tools [BLD_ARCH="rhel5_x86_64"]

Below lines should be contained within file 'gpdb/gpAux/releng/make/dependencies/ivy.xml'.
```xml
 <!-- dependency for PostGIS -->
      <dependency org="geos"                  name="geos"      rev="3.4.2"          conf="rhel5_x86_64->rhel5_x86_64;suse10_x86_64->suse10_x86_64" />
      <dependency org="json-c"                name="json-c"    rev="0.12"           conf="rhel5_x86_64->rhel5_x86_64;suse10_x86_64->suse10_x86_64" />
      <dependency org="PROJ.4"                name="proj"      rev="4.8.0"          conf="rhel5_x86_64->rhel5_x86_64;suse10_x86_64->suse10_x86_64" />
      <dependency org="Geospatial-Foundation" name="gdal"      rev="1.11.1"         conf="rhel5_x86_64->rhel5_x86_64;suse10_x86_64->suse10_x86_64" />
      <dependency org="expat"                 name="libexpat"  rev="2.1.0"          conf="rhel5_x86_64->rhel5_x86_64;suse10_x86_64->suse10_x86_64" />
```

### 2. Compile postgis gppkg

======================================

After downloaded libraries, go to package folder. And run make BLD_TARGETS="gppkg"
with user-defined parameters, which include BLD_ARCH (the os version), GPROOT (the
location of gpAux folder), BLD_TOP (the location of libraries, usually same as GPROOT), 
POSGIS_DIR (the location of postgis source folder), INSTLOC (the location of installed
gpdb), and use gppkg as build traget. 

An example is to write a shell 'build.sh' with lines:
```sh
source ~/greenplum-db-devel/greenplum_path.sh

make \
	BLD_TARGETS="gppkg" \
	BLD_ARCH="rhel5_x86_64" \
	INSTLOC=$GPHOME \
	BLD_TOP="/home/gpadmin/workspace/gpdb/gpAux" \
	POSTGIS_DIR="/home/gpadmin/workspace/geospatial/postgis/build/postgis-2.1.5" \
	gppkg
```

To clean it, run:
```sh
	make BLD_TOP="/home/gpadmin/workspace/gpdb/gpAux" clean
```

### 3. Verification and installation

======================================

run belowing command to verify postgis.gppkg is ready.
```sh
	gppkg --query postgis-ossv2.1.5_pv2.1_gpdb4.4-rhel5-x86_64.gppkg
```

run belowing belowing to install postgis.gppkg into gpdb.
```sh
	gppkg -i postgis-ossv2.1.5_pv2.1_gpdb4.4-rhel5-x86_64.gppkg
```
