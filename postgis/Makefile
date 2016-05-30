# common settings for compiling and gppkg generation
include Makefile.version

# compiling directory
POSTGIS_BLD_TOP     = $(shell mkdir -p build && cd ./build && pwd)
POSTGIS_BLD_DIR     = $(POSTGIS_BLD_TOP)/postgis-$(POSTGIS_VER)

# tar ball and patch file
POSTGIS_TAR_BALL    = source/postgis-$(POSTGIS_VER).tar.gz
POSTGIS_PATCH_FILE  = patch/postgis-$(POSTGIS_VER)-GPDB.patch

# entry
all install uninstall clean distclean maintainer-clean test check installcheck docs docs-install docs-uninstall utils:
	@if [ ! -d $(POSTGIS_BLD_DIR) ] ; then \
		echo "NOTICE: Extract $(POSTGIS_TAR_BALL), patch it, and run configure."; \
		make prepare ;\
		if [ x"$$GPHOME" = x ]; then \
			echo "WARNING: You need to set the 'GPHOME' first."; \
			echo "WARNING: And PostGIS will be installed into 'GPHOME' dirs."; \
			make remove; \
			false ; \
		else \
		 	cd $(POSTGIS_BLD_DIR) && $(POSTGIS_BLD_DIR)/configure \
				--with-raster \
				--without-topology \
				--with-pgconfig=$$GPHOME/bin/pg_config \
				--prefix=$$GPHOME; \
		fi; \
	fi
	@echo "PostGIS source-code is ready in $(POSTGIS_BLD_DIR)."
	@echo "Will compile it with: make $@."
	@echo "-----------------------------------------------------------------------"
	@echo
	make -C $(POSTGIS_BLD_DIR) $@ USE_PGXS=1

# prepare the compiling dir
prepare:
	@echo
	@echo "-----------------------------------------------------------------------"
	@echo "Prepare the compiling directory for postgis-$(POSTGIS_VER)."
	@echo "-----------------------------------------------------------------------"
	@if [ -d $(POSTGIS_BLD_DIR) ]; then \
		echo "NOTICE: $(POSTGIS_BLD_DIR) already exists."; \
		echo "    It's better to run 'make remove' firstly."; \
	else \
		echo "    1. extract $(POSTGIS_TAR_BALL) to $(POSTGIS_BLD_DIR) ..."; \
		tar -zxf $(POSTGIS_TAR_BALL) -C $(POSTGIS_BLD_TOP); \
		echo "    2. patch it with $(POSTGIS_PATCH_FILE) ..."; \
		patch -d $(POSTGIS_BLD_DIR) -p 4 --silent < $(POSTGIS_PATCH_FILE); \
		echo "-----------------------------------------------------------------------"; \
		echo "Done"; \
		echo "-----------------------------------------------------------------------"; \
	fi

remove:
	rm -rf $(POSTGIS_BLD_DIR)
