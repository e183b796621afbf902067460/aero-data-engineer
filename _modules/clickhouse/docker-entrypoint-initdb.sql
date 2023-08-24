-- S3 Engine which consumes the data from 'cannabis' of S3
create TABLE IF NOT EXISTS clickhouse.dm_cannabis
(
    dm_cannabis_id                          UInt32,

    dm_cannabis_uid                         String,
    dm_cannabis_strain                      String,
    dm_cannabis_cannabinoid_abbreviation    String,
    dm_cannabis_cannabinoid                 String,
    dm_cannabis_terpene                     String,
    dm_cannabis_medical_use                 String,
    dm_cannabis_health_benefit              String,
    dm_cannabis_category                    String,
    dm_cannabis_type                        String,
    dm_cannabis_buzzword                    String,
    dm_cannabis_brand                       String,

    dm_cannabis_timestamp                   DateTime
)
ENGINE = S3(
    'http://s3-datalake:9000/datalake-bucket/cannabis/*',
    's3-datalake-user',
    's3-datalake-password',
    'CSV'
)
ORDER BY (dm_cannabis_id, dm_cannabis_uid);
