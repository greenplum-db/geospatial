Summary:        Geospatial extensions for Greenplum Database
License:        GPLv2
Name:           postgis
Version:        %{postgis_ver}
Release:        %{postgis_rel}
Group:          Development/Tools
Prefix:         /temp
AutoReq:        no
AutoProv:       no
Provides:       postgis = %{postgis_ver}

%description
The PostGIS module provides geospatial extensions for Greenplum Database.

%install
make -C %{postgis_dir} BLD_TOP=%{bld_top} install prefix=%{buildroot}/temp

mkdir -p %{buildroot}/temp/bin
cp $GPHOME/bin/pgsql2shp %{buildroot}/temp/bin
cp $GPHOME/bin/shp2pgsql %{buildroot}/temp/bin
cp $GPHOME/bin/raster2pgsql %{buildroot}/temp/bin

mkdir -p %{buildroot}/temp/lib/postgresql
cp $GPHOME/lib/postgresql/postgis-3.so %{buildroot}/temp/lib/postgresql/postgis-3.so
cp $GPHOME/lib/postgresql/postgis_raster-3.so %{buildroot}/temp/lib/postgresql/postgis_raster-3.so
cp $GPHOME/lib/postgresql/address_standardizer-3.so %{buildroot}/temp/lib/postgresql/address_standardizer-3.so

mkdir -p %{buildroot}/temp/share/postgresql/contrib/postgis-3.3/
mkdir -p %{buildroot}/temp/share/postgresql/contrib/postgis-3.3/{install,upgrade,uninstall}/
mkdir -p %{buildroot}/temp/share/postgresql/extension/

cp $GPHOME/share/postgresql/contrib/postgis-3.3/postgis.sql %{buildroot}/temp/share/postgresql/contrib/postgis-3.3/install/
cp $GPHOME/share/postgresql/contrib/postgis-3.3/rtpostgis.sql %{buildroot}/temp/share/postgresql/contrib/postgis-3.3/install/
cp $GPHOME/share/postgresql/contrib/postgis-3.3/*comments.sql %{buildroot}/temp/share/postgresql/contrib/postgis-3.3/install/
cp $GPHOME/share/postgresql/contrib/postgis-3.3/spatial_ref_sys.sql %{buildroot}/temp/share/postgresql/contrib/postgis-3.3/install/

cp $GPHOME/share/postgresql/contrib/postgis-3.3/*upgrade*.sql %{buildroot}/temp/share/postgresql/contrib/postgis-3.3/upgrade/
cp $GPHOME/share/postgresql/contrib/postgis-3.3/legacy*.sql %{buildroot}/temp/share/postgresql/contrib/postgis-3.3/upgrade/
cp $GPHOME/share/postgresql/contrib/postgis-3.3/rtpostgis_legacy.sql %{buildroot}/temp/share/postgresql/contrib/postgis-3.3/upgrade/

cp $GPHOME/share/postgresql/contrib/postgis-3.3/uninstall*.sql %{buildroot}/temp/share/postgresql/contrib/postgis-3.3/uninstall/

cp %{postgis_dir}/../../package/postgis_manager.sh %{buildroot}/temp/share/postgresql/contrib/postgis-3.3/postgis_manager.sh

cp %{postgis_dir}/../../package/postgis_replace_views.sql %{buildroot}/temp/share/postgresql/contrib/postgis-3.3/postgis_replace_views.sql
cp %{postgis_dir}/../../package/postgis--unpackaged--2.1.5.sql %{buildroot}/temp/share/postgresql/contrib/postgis-3.3/upgrade/
cp %{postgis_dir}/../../package/postgis.control-2.1.5 %{buildroot}/temp/share/postgresql/contrib/postgis-3.3/upgrade/

cp $GPHOME/share/postgresql/extension/postgis.control %{buildroot}/temp/share/postgresql/extension/
cp $GPHOME/share/postgresql/extension/postgis_raster.control %{buildroot}/temp/share/postgresql/extension/
cp $GPHOME/share/postgresql/extension/postgis_tiger_geocoder.control %{buildroot}/temp/share/postgresql/extension/
cp $GPHOME/share/postgresql/extension/address_standardizer.control %{buildroot}/temp/share/postgresql/extension/
cp $GPHOME/share/postgresql/extension/address_standardizer_data_us.control %{buildroot}/temp/share/postgresql/extension/
cp $GPHOME/share/postgresql/extension/postgis*.sql %{buildroot}/temp/share/postgresql/extension/
cp $GPHOME/share/postgresql/extension/address_standardizer*.sql %{buildroot}/temp/share/postgresql/extension/

%files
/temp/bin/raster2pgsql
/temp/bin/pgsql2shp
/temp/bin/shp2pgsql
/temp/share/postgresql/contrib/postgis-3.3/postgis_replace_views.sql
/temp/share/postgresql/contrib/postgis-3.3/install/topology_comments.sql
/temp/share/postgresql/contrib/postgis-3.3/install/postgis_comments.sql
/temp/share/postgresql/contrib/postgis-3.3/install/spatial_ref_sys.sql
/temp/share/postgresql/contrib/postgis-3.3/install/rtpostgis.sql
/temp/share/postgresql/contrib/postgis-3.3/install/raster_comments.sql
/temp/share/postgresql/contrib/postgis-3.3/install/sfcgal_comments.sql
/temp/share/postgresql/contrib/postgis-3.3/install/postgis.sql
/temp/share/postgresql/contrib/postgis-3.3/upgrade/legacy_gist.sql
/temp/share/postgresql/contrib/postgis-3.3/upgrade/rtpostgis_legacy.sql
/temp/share/postgresql/contrib/postgis-3.3/upgrade/postgis--unpackaged--2.1.5.sql
/temp/share/postgresql/contrib/postgis-3.3/upgrade/postgis.control-2.1.5
/temp/share/postgresql/contrib/postgis-3.3/upgrade/legacy_minimal.sql
/temp/share/postgresql/contrib/postgis-3.3/upgrade/postgis_upgrade.sql
/temp/share/postgresql/contrib/postgis-3.3/upgrade/rtpostgis_upgrade.sql
/temp/share/postgresql/contrib/postgis-3.3/upgrade/legacy.sql
/temp/share/postgresql/contrib/postgis-3.3/postgis_manager.sh
/temp/share/postgresql/contrib/postgis-3.3/uninstall/uninstall_legacy.sql
/temp/share/postgresql/contrib/postgis-3.3/uninstall/uninstall_rtpostgis.sql
/temp/share/postgresql/contrib/postgis-3.3/uninstall/uninstall_postgis.sql
/temp/share/postgresql/extension/postgis_raster--3.1.2--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.2.2--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.5.8--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--3.1.6--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.1.7--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.3.9--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.1.1--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.3.2--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.3.0--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.3.7--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.2.6--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.1.6--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.1.5--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.3.11--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.1.2--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.2.2--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.1.4--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.4.6--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.4.4--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.2.4--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.0.3--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.3.10--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--3.3.0--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.4.3--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.1.6--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.0.2--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.2.8--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.0.4--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.4.5--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.5.4--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.2.1--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.2.1--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--3.1.4--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.1.0--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.2.1--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.0.3--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.1.4--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.3.2next--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.0.6--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.2.0--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.0.2--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.4.6--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.4.10--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.1.9--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.1.6--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.4.5--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.4.1--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.0.3--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--ANY--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.3.5--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.1.3--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.5.7--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.2.3--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.4.0--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.4.4--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.2.3--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.5.3--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.5.6--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--3.1.7--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.3.6--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.1.8--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.0.2--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--3.0.0--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.3.5--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.3.9--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.1.5--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.5.0--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.1.8--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.1.1--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.5.5--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.2.5--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.3.1--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--3.3.2next--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.2.1--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.3.9--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.4.8--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.3.3--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.1.8--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.5.7--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.4.9--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.2.4--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.4.7--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.1.6--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.1.1--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.2.7--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.1.2--3.3.2.sql
/temp/share/postgresql/extension/postgis--unpackaged--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.1.5--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.3.3--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--3.2.3--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.3.8--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.0.3--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.4.1--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.3.7--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.2.4--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.4.7--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--3.0.1--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.0.2--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.4.8--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.0.6--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.2.0--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.5.4.sql
/temp/share/postgresql/extension/postgis_raster--3.0.6--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.0.8--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--3.1.2--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.5.7--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.2.4--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.2.4--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.0.2--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.4.6--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.0.0--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.0.7--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.2.0--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--3.1.1--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.4.9--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.4.7--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.3.0--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.1.5--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.3.8--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.5.1--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.3.1--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.2.4--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.3.11--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.1.3--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.1.3--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.1.0--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.3.1--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.1.8--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.5.8--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.2.3--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.1.5--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.3.7--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.3.2--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.5.2--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.1.4--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.5.4--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.0.0--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.3.1--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.2.5--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.4.5--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--3.2.3--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer.control
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.0.4--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--3.3.0--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.5.5--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--3.2.4--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.3.0--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.1.4--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.5.3--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.3.11--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.2.6--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.0.6--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.1.1--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.5.3--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.3.4--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.2.8--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.1.8--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.0.2--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.4.4--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.5.9--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.4.10--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--3.3.2--3.3.2next.sql
/temp/share/postgresql/extension/postgis--2.3.11--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--3.2.4--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.5.5--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--3.1.1--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.5.9--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.0.3--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.4.8--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.4.5--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.4.1--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.1.4--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.4.2--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.1.3--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.4.3--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.1.0--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.5.4--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.1.4--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.0.1--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.1.2--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.1.0--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.3.6--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.1.0--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.0.7--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.1.2--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.0.4--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.4.6--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.0.1--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.0.5--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.4.2--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.0.5--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.2.1--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.3.2--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.1.8--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.1.9--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.5.0--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.0.0--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.5.8--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.1.5--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.3.9--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.2.2--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--3.3.2--3.3.2next.sql
/temp/share/postgresql/extension/postgis_raster--3.1.7--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.4.3--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.2.0--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.3.1--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.3.0--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.0.7--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.4.7--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.4.2--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.2.7--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.2.2--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.4.3--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.2.2--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.2.3--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.4.8--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.0.6--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.0.3--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.2.1--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.2.5--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.3.10--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.3.10--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.1.2--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.1.6--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.1.7--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.4.8--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.1.5--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.5.5--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.0.6--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.3.1--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--unpackaged.sql
/temp/share/postgresql/extension/postgis--2.3.0--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--3.1.3--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.3.4--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.4.5--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.0.3--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.5.5--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.3.2next--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us.control
/temp/share/postgresql/extension/postgis--2.2.3--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.5.1--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.1.0--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.2.6--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--3.1.0--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.5.3--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--3.0.3--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.3.8--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.3.0--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.0.5--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--3.1.4--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--3.0.1--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.0.8--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.4.10--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.1.0--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.3.0--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.3.2next--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.3.11--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.0.4--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.5.6--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.5.3--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.3.3--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.0.5--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--3.0.6--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.1.3--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--3.1.8--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.5.6--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.0.7--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.1.9--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.3.6--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.3.8--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.1.0--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.2.2--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--3.1.8--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.5.8--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.5.4--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--3.1.5--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.2.3--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--3.0.4--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.4.0--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.1.6--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.1.2--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.2.1--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.3.6--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.4.10--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.5.2--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.3.2--3.3.2next.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.1.3--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.5.0--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--ANY--2.5.4.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.1.1--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.5.0--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.0.7--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.1.7--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.1.4--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.1.2--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.0.8--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.0.6--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.1.8--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.1.6--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.3.4--3.3.2.sql
/temp/share/postgresql/extension/postgis--unpackaged.sql
/temp/share/postgresql/extension/postgis--2.3.10--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.2.0--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.1.7--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.4.2--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.0.1--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.0.7--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.3.1--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.3.8--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.3.2--3.3.2next.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.2.8--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.2.0--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.1.1--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.5.7--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.5.0--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--3.1.6--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.2.5--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.4.4--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.0.5--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.3.4--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.4.4--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--1.0--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.2.0--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.3.9--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.3.1--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.3.4--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.2.2--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.5.8--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.0.7--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.0.5--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.4.9--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.0.0--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.4.2--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.5.7--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.0.5--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.3.3--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.2.6--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.0.0--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.1.6--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.4.1--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.2.8--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.4.3--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.5.1--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.3.10--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.5.4.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.3.7--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.4.0--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.2.4--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.2.1--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--3.0.4--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.0.0--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.2.7--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.5.9--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--unpackaged--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.1.4--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.4.9--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--3.0.2--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--3.0.0--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.0.0--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.4.10--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.5.6--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.0.6--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.0.5--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.0.1--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--3.3.2next--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.0.4--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.3.5--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.2.3--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.0.1--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.0.7--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.5.2--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--3.0.2--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.5.9--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--ANY--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.0.3--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--3.0.8--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.1.7--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--ANY--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.5.9--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.2.2--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--3.2.1--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--3.2.0--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.1.3--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.5.1--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.0.6--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--3.2.0--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--unpackaged--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--3.0.7--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.5.4--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.1.9--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--3.3.1--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.2.3--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--3.1.5--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.3.3--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--3.0.5--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.1.2--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.1.1--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.1.7--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--ANY--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--3.1.3--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--3.0.5--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.2.6--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.0.1--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.5.1--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.2.4--3.3.2.sql
/temp/share/postgresql/extension/postgis--ANY--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.5.4--2.5.4next.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.2.0--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.2.8--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.1.5--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--3.2.1--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.4.0--3.3.2.sql
/temp/share/postgresql/extension/postgis--3.0.4--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.0.1--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.1.8--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.0.4--3.3.2.sql
/temp/share/postgresql/extension/postgis.control
/temp/share/postgresql/extension/postgis_raster.control
/temp/share/postgresql/extension/address_standardizer--2.4.9--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.3.6--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.0.2--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.0.1--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.3.5--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.0.4--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.5.6--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--3.0.7--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--2.4.0--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.4.6--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--3.0.8--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder.control
/temp/share/postgresql/extension/postgis_raster--3.0.3--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.5.2--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.3.2--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.2.7--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.0.0--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.4.7--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.5.4next--2.5.4.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.3.5--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.5.2--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.1.7--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.2.5--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.3.7--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.2.7--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--2.1.1--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.1.7--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--3.1.0--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--3.3.0--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer--1.0--2.5.4.sql
/temp/share/postgresql/extension/address_standardizer--3.2.2--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--2.3.2--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.1.3--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--3.3.1--3.3.2.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.4.1--3.3.2.sql
/temp/share/postgresql/extension/postgis--2.0.2--3.3.2.sql
/temp/share/postgresql/extension/address_standardizer_data_us--3.3.2--3.3.2next.sql
/temp/share/postgresql/extension/postgis_tiger_geocoder--2.1.9--3.3.2.sql
/temp/share/postgresql/extension/postgis_raster--3.2.2--3.3.2.sql
/temp/lib/postgresql/address_standardizer-3.so
/temp/lib/postgresql/postgis_raster-3.so
/temp/lib/postgresql/postgis-3.so

