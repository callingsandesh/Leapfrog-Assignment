import sys
file_path = '/home/sandesh/Desktop/Leapfrog/Data/3rd Week(OLAP Design)/Day3'
sys.path.append(file_path)


from src.utils import connect       #here, the connect takes the name of the database as an argument

#importing different SQL queries function
from src.helper import execute_select_query
from src.helper import execute_insert_query
from src.helper import  execute_delete_query


from src.pipeline.extract_data_from_ecommerce_dump import extract_data_from_ecommerce


def load_sales_to_sales_archive():
    """This is the method to select data from sales_raw and push to the sales_archive"""

    #query to select all the data from sales table of sales_raw database
    query="""
    SELECT * FROM sales
    """
    data=execute_select_query(query,connect("sales_raw"))

    #query to insert all the data to sales table of sales_archive database
    query_1= """
    INSERT INTO sales VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    #execute the above insert query
    execute_insert_query(query_1,connect("sales_archive"),data)


def load_data_to_sales_raw_and_archive():
    """This is the method which is performs all the necessary work of ETL"""

    #extracting data from ecommerce_dump database
    data = extract_data_from_ecommerce()

    # Making all the data inside sale_raw database archive
    load_sales_to_sales_archive()

    ## deleting all the data from sales table of sales_raw database as we have already archived it
    query=""" DELETE FROM sales"""
    execute_delete_query(query,connect("sales_raw"))


    # query to insert data into table sales of sales_raw database
    query="""
    INSERT INTO sales VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    execute_insert_query(query,connect("sales_raw"),data)
    
    

if __name__ == '__main__':
    load_data_to_sales_raw_and_archive()