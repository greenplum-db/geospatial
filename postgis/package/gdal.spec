Summary:        GDAL library 
License:        MIT/X license        
Name:           gdal
Version:        %{gdal_ver}
Release:        %{gdal_rel} 
Group:          Development/Tools
Prefix:         /temp
AutoReq:        no
AutoProv:       no
Provides:       gdal = %{gdal_ver}, /bin/sh
Requires:       libexpat = %{libexpat_ver}

%description
The Geos module provides a geospatial data abstraction library which is used by PostGIS.

%install
mkdir -p %{buildroot}/temp/lib
cp -rf %{gdal_dir}/lib/libgdal*so* %{buildroot}/temp/lib/
mkdir -p %{buildroot}/temp/share
cp -rf %{gdal_dir}/share/gdal %{buildroot}/temp/share

%post
sed -i "s|export GDAL_DATA=\$GPHOME/share/gdal||g" $GPHOME/greenplum_path.sh
sed -i "s|export POSTGIS_ENABLE_OUTDB_RASTERS=0||g" $GPHOME/greenplum_path.sh
sed -i "s|export POSTGIS_GDAL_ENABLED_DRIVERS=DISABLE_ALL||g" $GPHOME/greenplum_path.sh
sed -i '${/^$/d}' $GPHOME/greenplum_path.sh
sed -i '${/^$/d}' $GPHOME/greenplum_path.sh
sed -i '${/^$/d}' $GPHOME/greenplum_path.sh
echo "export GDAL_DATA=\$GPHOME/share/gdal" >> $GPHOME/greenplum_path.sh
echo "export POSTGIS_ENABLE_OUTDB_RASTERS=0" >> $GPHOME/greenplum_path.sh
echo "export POSTGIS_GDAL_ENABLED_DRIVERS=DISABLE_ALL" >> $GPHOME/greenplum_path.sh

%postun
sed -i "s|export GDAL_DATA=\$GPHOME/share/gdal||g" $GPHOME/greenplum_path.sh
sed -i "s|export POSTGIS_ENABLE_OUTDB_RASTERS=0||g" $GPHOME/greenplum_path.sh
sed -i "s|export POSTGIS_GDAL_ENABLED_DRIVERS=DISABLE_ALL||g" $GPHOME/greenplum_path.sh
sed -i '${/^$/d}' $GPHOME/greenplum_path.sh
sed -i '${/^$/d}' $GPHOME/greenplum_path.sh
sed -i '${/^$/d}' $GPHOME/greenplum_path.sh

%files
/temp
