CREATE OR REPLACE VIEW geometry_columns AS
  SELECT current_database()::varchar(256) AS f_table_catalog,
    n.nspname::varchar(256) AS f_table_schema,
    c.relname::varchar(256) AS f_table_name,
    a.attname::varchar(256) AS f_geometry_column,
    COALESCE(NULLIF(postgis_typmod_dims(a.atttypmod),2),
             postgis_constraint_dims(n.nspname, c.relname, a.attname),
             2) AS coord_dimension,
    COALESCE(NULLIF(postgis_typmod_srid(a.atttypmod),0),
             postgis_constraint_srid(n.nspname, c.relname, a.attname),
             0) AS srid,
    -- force to be uppercase with no ZM so is backwards compatible
    -- with old geometry_columns
    replace(
      replace(
        COALESCE(
          NULLIF(upper(postgis_typmod_type(a.atttypmod)::text), 'GEOMETRY'),
          postgis_constraint_type(n.nspname, c.relname, a.attname),
          'GEOMETRY'
        ), 'ZM', ''
      ), 'Z', ''
    )::varchar(30) AS type
  FROM pg_class c, pg_attribute a, pg_type t, pg_namespace n
  WHERE t.typname = 'geometry'::name
    AND a.attisdropped = false
    AND a.atttypid = t.oid
    AND a.attrelid = c.oid
    AND c.relnamespace = n.oid
    AND (c.relkind = 'r'::"char" OR c.relkind = 'v'::"char" OR c.relkind = 'm'::"char" OR c.relkind = 'f'::"char")
    AND NOT pg_is_other_temp_schema(c.relnamespace)
    AND NOT ( n.nspname = 'public' AND c.relname = 'raster_columns' )
    AND has_table_privilege( c.oid, 'SELECT'::text );

CREATE OR REPLACE VIEW geography_columns AS
  SELECT
    current_database() AS f_table_catalog,
    n.nspname AS f_table_schema,
    c.relname AS f_table_name,
    a.attname AS f_geography_column,
    postgis_typmod_dims(a.atttypmod) AS coord_dimension,
    postgis_typmod_srid(a.atttypmod) AS srid,
    postgis_typmod_type(a.atttypmod) AS type
  FROM
    pg_class c,
    pg_attribute a,
    pg_type t,
    pg_namespace n
  WHERE t.typname = 'geography'
        AND a.attisdropped = false
        AND a.atttypid = t.oid
        AND a.attrelid = c.oid
        AND c.relnamespace = n.oid
        AND NOT pg_is_other_temp_schema(c.relnamespace)
        AND has_table_privilege( c.oid, 'SELECT'::text );

CREATE OR REPLACE VIEW raster_columns AS
  SELECT
    current_database() AS r_table_catalog,
    n.nspname AS r_table_schema,
    c.relname AS r_table_name,
    a.attname AS r_raster_column,
    COALESCE(_raster_constraint_info_srid(n.nspname, c.relname, a.attname), (SELECT ST_SRID('POINT(0 0)'::geometry))) AS srid,
    _raster_constraint_info_scale(n.nspname, c.relname, a.attname, 'x') AS scale_x,
    _raster_constraint_info_scale(n.nspname, c.relname, a.attname, 'y') AS scale_y,
    _raster_constraint_info_blocksize(n.nspname, c.relname, a.attname, 'width') AS blocksize_x,
    _raster_constraint_info_blocksize(n.nspname, c.relname, a.attname, 'height') AS blocksize_y,
    COALESCE(_raster_constraint_info_alignment(n.nspname, c.relname, a.attname), FALSE) AS same_alignment,
    COALESCE(_raster_constraint_info_regular_blocking(n.nspname, c.relname, a.attname), FALSE) AS regular_blocking,
    _raster_constraint_info_num_bands(n.nspname, c.relname, a.attname) AS num_bands,
    _raster_constraint_info_pixel_types(n.nspname, c.relname, a.attname) AS pixel_types,
    _raster_constraint_info_nodata_values(n.nspname, c.relname, a.attname) AS nodata_values,
    _raster_constraint_info_out_db(n.nspname, c.relname, a.attname) AS out_db,
    _raster_constraint_info_extent(n.nspname, c.relname, a.attname) AS extent
  FROM
    pg_class c,
    pg_attribute a,
    pg_type t,
    pg_namespace n
  WHERE t.typname = 'raster'::name
    AND a.attisdropped = false
    AND a.atttypid = t.oid
    AND a.attrelid = c.oid
    AND c.relnamespace = n.oid
    AND c.relkind = ANY(ARRAY['r'::char, 'v'::char, 'm'::char, 'f'::char])
    AND NOT pg_is_other_temp_schema(c.relnamespace);

CREATE OR REPLACE VIEW raster_overviews AS
  SELECT
    current_database() AS o_table_catalog,
    n.nspname AS o_table_schema,
    c.relname AS o_table_name,
    a.attname AS o_raster_column,
    current_database() AS r_table_catalog,
    split_part(split_part(s.consrc, '''::name', 1), '''', 2)::name AS r_table_schema,
    split_part(split_part(s.consrc, '''::name', 2), '''', 2)::name AS r_table_name,
    split_part(split_part(s.consrc, '''::name', 3), '''', 2)::name AS r_raster_column,
    trim(both from split_part(s.consrc, ',', 2))::integer AS overview_factor
  FROM
    pg_class c,
    pg_attribute a,
    pg_type t,
    pg_namespace n,
    pg_constraint s
  WHERE t.typname = 'raster'::name
    AND a.attisdropped = false
    AND a.atttypid = t.oid
    AND a.attrelid = c.oid
    AND c.relnamespace = n.oid
    AND c.relkind = ANY(ARRAY['r'::char, 'v'::char, 'm'::char, 'f'::char])
    AND s.connamespace = n.oid
    AND s.conrelid = c.oid
    AND s.consrc LIKE '%_overview_constraint(%'
    AND NOT pg_is_other_temp_schema(c.relnamespace);
