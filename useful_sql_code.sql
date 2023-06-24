-- Working with datetimes

select current_timestamp AT TIME ZONE 'aest';

select now()  AT TIME ZONE 'aest';

select current_time  AT TIME ZONE 'aest';

select localtime  AT TIME ZONE 'aest';

select 
    date_part('month', age(sales_month, load_timestamp)) as months_old
from 
    retail.stg_unpivot_clean