-- put file://my-location/forex/exchange-rate.csv @my_internal_stg/exchange/ parallel=10 auto_compress=false;;

list @my_internal_stg/exchange/;

use schema common;
create or replace transient table exchange_rate(
    date date, 
    usd2usd decimal(10,7),
    usd2eu decimal(10,7),
    usd2can decimal(10,7),
    usd2uk decimal(10,7),
    usd2inr decimal(10,7),
    usd2jp decimal(10,7)
);

copy into sales_dwh.common.exchange_rate
from 
(
select 
    t.$1::date as exchange_dt,
    to_decimal(t.$2) as usd2usd,
    to_decimal(t.$3,12,10) as usd2eu,
    to_decimal(t.$4,12,10) as usd2can,
    to_decimal(t.$4,12,10) as usd2uk,
    to_decimal(t.$4,12,10) as usd2inr,
    to_decimal(t.$4,12,10) as usd2jp
from 
     @sales_dwh.source.my_internal_stg/exchange/exchange-rate-data.csv
     (file_format => 'sales_dwh.common.my_csv_format') t
);