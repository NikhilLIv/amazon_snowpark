import sys
import logging
import os
from snowflake.snowpark import Session, DataFrame
from snowflake.snowpark.functions import col,lit,row_number, rank
from snowflake.snowpark import Window
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '', '.env'))

# initiate logging at info level
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%I:%M:%S')

# snowpark session
def get_snowpark_session() -> Session:
    # creating snowflake session object
    return Session.builder.config("connection_name", "myconnection").create()  

def filter_dataset(df, column_name, filter_criterian) -> DataFrame:
    # Payment Status = Paid
    # Shipping = Delivered
    return_df = df.filter(col(column_name) == filter_criterian)

    return return_df

def source_to_curated_us():

    #get the session object and get dataframe
    session = get_snowpark_session()
    sales_df = session.sql("select * from us_sales_order")

    # apply filter to select only paid and delivered sale orders
    # select * from us_sales_order where PAYMENT_STATUS = 'Paid' and SHIPPING_STATUS = 'Delivered'
    paid_sales_df = filter_dataset(sales_df,'PAYMENT_STATUS','Paid')
    shipped_sales_df = filter_dataset(paid_sales_df,'SHIPPING_STATUS','Delivered')

    # adding country and region to the data frame
    # select *, 'IN' as Country, 'APAC' as Region from us_sales_order where PAYMENT_STATUS = 'Paid' and SHIPPING_STATUS = 'Delivered'
    country_sales_df = shipped_sales_df.with_column('Country',lit('US')).with_column('Region',lit('NA'))

    # join to add forex calculation
    forex_df = session.sql("select * from sales_dwh.common.exchange_rate")
    sales_with_forext_df = country_sales_df.join(forex_df,country_sales_df['order_dt']==forex_df['date'],join_type='outer')
    #sales_with_forext_df.show(2)

    #de-duplication
    #print(sales_with_forext_df.count())
    unique_orders = sales_with_forext_df.with_column('order_rank',rank().over(Window.partitionBy(col("order_dt")).order_by(col('_metadata_last_modified').desc()))).filter(col("order_rank")==1).select(col('SALES_ORDER_KEY').alias('unique_sales_order_key'))
    final_sales_df = unique_orders.join(sales_with_forext_df,unique_orders['unique_sales_order_key']==sales_with_forext_df['SALES_ORDER_KEY'],join_type='inner')
    target_sales_df = session.sql("select * from sales_dwh.curated.us_sales_order")
    final_sales_df = final_sales_df.join(target_sales_df,final_sales_df['SALES_ORDER_KEY']==target_sales_df['SALES_ORDER_KEY'],join_type='leftanti')
    final_sales_df = final_sales_df.select(
        col('SALES_ORDER_KEY'),
        col('ORDER_ID'),
        col('ORDER_DT'),
        col('CUSTOMER_NAME'),
        col('MOBILE_KEY'),
         col('Country'),
        col('Region'),
        col('ORDER_QUANTITY'),
        lit('USD').alias('LOCAL_CURRENCY'),
        col('UNIT_PRICE').alias('LOCAL_UNIT_PRICE'),
        col('PROMOTION_CODE').alias('PROMOTION_CODE'),
        col('FINAL_ORDER_AMOUNT').alias('LOCAL_TOTAL_ORDER_AMT'),
        col('TAX_AMOUNT').alias('local_tax_amt'),
        col('USD2INR').alias("Exhchange_Rate"),
        (col('FINAL_ORDER_AMOUNT')/col('USD2USD')).alias('US_TOTAL_ORDER_AMT'),
        (col('TAX_AMOUNT')/col('USD2USD')).alias('USD_TAX_AMT'),
        col('payment_status'),
        col('shipping_status'),
        col('payment_method'),
        col('payment_provider'),
        col('phone').alias('conctact_no'),
        col('shipping_address')
    )

    # final_sales_df.show(5)
    final_sales_df.write.save_as_table("sales_dwh.curated.us_sales_order",mode="append")
    session.close()
    
if __name__ == '__main__':
    source_to_curated_us()