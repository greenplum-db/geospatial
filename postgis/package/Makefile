#------------------------------------------------------------------#
# To deploy PostGIS onto Greenplum Database, we need to install
# a set of 3rd-party libraries, e.g., geos, gdal, json-c, proj4,
# etc. This file is created to deal with this kind of jobs.
# 
# Copyright (c) 2015 - 2016, Pivotal Inc. 
# 
#------------------------------------------------------------------#

#TODO will be fixed after set git submodule
#BLD_TOP=$(shell cd ../../.. && pwd)
#BLD_TOP=$(shell cd ~/workspace/gpdb/gpAux/ && pwd)
include $(BLD_TOP)/Makefile.global     # for BLD_ARCH
include $(BLD_TOP)/releng/tools.mk
EXT_TOP=$(BLD_TOP)/ext/$(BLD_ARCH)

#GPDB
PG_CONFIG=$(BLD_TOP)/../src/bin/pg_config/pg_config

PG_DEP_LIB_DIR=$(shell $(PG_CONFIG) --libdir)
GPDB_LIB_DIR=$(PG_DEP_LIB_DIR)
GPDB_DIR=$(shell cd $(GPDB_LIB_DIR)/.. && pwd)

#ape from $(BLD_TOP)/src/Makefile.global etc
INSTALL=$(BLD_TOP)/config/install-sh -c
INSTALL_SHLIB=$(BLD_TOP)/config/install-sh -c -m 755
INSTALL_DATA=$(BLD_TOP)/config/install-sh -c -m 644
INSTALL_PROGRAM=$(BLD_TOP)/config/install-sh -s
mkinstalldirs=$(BLD_TOP)/config/mkinstalldirs

# versions for these 3rd party libraries and Postgis
include ../Makefile.version

#GOES
GEOS_DIR=$(EXT_TOP)/geos-$(GEOS_VER)
GEOS_CONFIG=$(GEOS_DIR)/bin/geos-config
GEOS_RPM_FLAGS="--define 'geos_dir $(GEOS_DIR)' --define 'geos_ver $(GEOS_VER)' --define 'geos_rel $(GEOS_REL)'"
GEOS_RPM=geos-$(GEOS_VER)-$(GEOS_REL).$(ARCH).rpm

#Proj.4
PROJ_DIR=$(EXT_TOP)/proj-$(PROJ_VER)
PROJ_RPM_FLAGS="--define 'proj_dir $(PROJ_DIR)' --define 'proj_ver $(PROJ_VER)' --define 'proj_rel $(PROJ_REL)'"
PROJ_RPM=proj-$(PROJ_VER)-$(PROJ_REL).$(ARCH).rpm

#json-c
JSON_DIR=$(EXT_TOP)/json-c-$(JSON_VER)
JSON_RPM_FLAGS="--define 'json_dir $(JSON_DIR)' --define 'json_ver $(JSON_VER)' --define 'json_rel $(JSON_REL)'"
JSON_RPM=json-c-$(JSON_VER)-$(JSON_REL).$(ARCH).rpm

#GDAL
GDAL_DIR=$(EXT_TOP)/gdal-$(GDAL_VER)
GDAL_CONFIG=$(GDAL_DIR)/bin/gdal-config
GDAL_RPM_FLAGS="--define 'gdal_dir $(GDAL_DIR)' --define 'gdal_ver $(GDAL_VER)' --define 'gdal_rel $(GDAL_REL)' --define 'libexpat_ver $(LIBEXPAT_VER)' --define 'libexpat_rel $(LIBEXPAT_REL)'"
GDAL_RPM=gdal-$(GDAL_VER)-$(GDAL_REL).$(ARCH).rpm

#XML2
XML2_DIR=$(EXT_TOP)
XML2_CONFIG=$(XML2_DIR)/bin/xml2-config

# LIBEXPAT
LIBEXPAT_DIR=$(EXT_TOP)/libexpat-$(LIBEXPAT_VER)
LIBEXPAT_RPM_FLAGS="--define 'libexpat_dir $(LIBEXPAT_DIR)' --define 'libexpat_ver $(LIBEXPAT_VER)' --define 'libexpat_rel $(LIBEXPAT_REL)'"
LIBEXPAT_RPM=libexpat-$(LIBEXPAT_VER)-$(LIBEXPAT_REL).$(ARCH).rpm

# POSTGIS
POSTGIS_DIR=$(shell cd ../build/postgis-$(POSTGIS_VER) && pwd)
POSTGIS_PKG_VER=ossv$(POSTGIS_VER)_pv$(PIVOTAL_VER)_gpdb$(GPDB_VER)orca
POSTGIS_RPM_FLAGS="--define 'bld_top $(BLD_TOP)' --define 'postgis_dir $(POSTGIS_DIR)' --define 'postgis_ver $(POSTGIS_VER)' --define 'postgis_rel $(POSTGIS_REL)' --define 'geos_ver $(GEOS_VER)' --define 'proj_ver $(PROJ_VER)' --define 'json_ver $(JSON_VER)' --define 'gdal_ver $(GDAL_VER)' --define 'libexpat_ver $(LIBEXPAT_VER)'"
DEPENDENT_RPMS="$(GEOS_RPM) $(PROJ_RPM) $(JSON_RPM) $(GDAL_RPM) $(LIBEXPAT_RPM)"
POSTGIS_RPM=postgis-$(POSTGIS_VER)-$(POSTGIS_REL).$(ARCH).rpm

#GPPKG
POSTGIS_GPPKG=postgis-$(POSTGIS_PKG_VER)-$(OS)-$(ARCH).gppkg
TARGET_GPPKG=$(POSTGIS_GPPKG)
EXTRA_CLEAN+=$(GEOS_RPM) $(PROJ_RPM) $(JSON_RPM) $(GDAL_RPM) $(LIBEXPAT_RPM) $(POSTGIS_RPM) $(POSTGIS_GPPKG)

#
# Generic rules to build gppkgs included here
#
include $(BLD_TOP)/releng/gppkg.mk

# trigger the compiling process
build_postgis:
	cd $(POSTGIS_DIR) && $(POSTGIS_DIR)/configure --with-geosconfig=$(GEOS_CONFIG) --with-projdir=$(PROJ_DIR) --with-jsondir=$(JSON_DIR) --with-gdalconfig=$(GDAL_CONFIG) --with-pgconfig=$(PG_CONFIG) --with-xml2config=$(XML2_CONFIG) --with-raster --without-topology	--prefix=$$GPHOME 
	$(MAKE) -C ..


# for regressing
DEP_LIBS_PATH=$(GEOS_DIR) $(PROJ_DIR) $(JSON_DIR) $(GDAL_DIR)
DEP_LIBS_BE=$(GEOS_LIBS_BE) $(PROJ_LIBS_BE) $(JSON_LIBS_BE) $(GDAL_LIBS_BE)
DEP_LIBS_AF=$(GEOS_LIBS_AF) $(PROJ_LIBS_AF) $(JSON_LIBS_AF) $(GDAL_LIBS_AF)

#for data dir copying during source-code-building (not form GPROOT)
DEP_LIBS_DATA=$(GDAL_DIR)/share/gdal $(PROJ_DIR)/share/proj
GPDB_DATA_AF=$(GPDB_DIR)/share/gdal $(GPDB_DIR)/share/proj

SHLIB_LINK_F = @SHLIB_LINK@
SHLIB_LINK := $(SHLIB_LINK_F) $(SHLIB_LINK)

# for compiling

gppkg: build_postgis gppkg_only

gppkg_only: $(GEOS_DIR) $(PROJ_DIR) $(JSON_DIR) $(GDAL_DIR) $(LIBEXPAT_DIR)
	$(MAKE) $(GEOS_RPM) RPM_FLAGS=$(GEOS_RPM_FLAGS)
	$(MAKE) $(PROJ_RPM) RPM_FLAGS=$(PROJ_RPM_FLAGS)
	$(MAKE) $(JSON_RPM) RPM_FLAGS=$(JSON_RPM_FLAGS)
	$(MAKE) $(GDAL_RPM) RPM_FLAGS=$(GDAL_RPM_FLAGS)
	$(MAKE) $(LIBEXPAT_RPM) RPM_FLAGS=$(LIBEXPAT_RPM_FLAGS)
	$(MAKE) $(POSTGIS_RPM) RPM_FLAGS=$(POSTGIS_RPM_FLAGS)
	$(MAKE) $(POSTGIS_GPPKG) MAIN_RPM=$(POSTGIS_RPM) DEPENDENT_RPMS=$(DEPENDENT_RPMS)

.PHONY: gppkg
