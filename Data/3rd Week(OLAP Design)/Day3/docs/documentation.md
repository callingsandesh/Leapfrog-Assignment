## 1.Explanation about create\_table\_sale.sql file in schema.

* `schema/create_table_sales.sql`


```
CREATE TABLE sales(

    user_id INTEGER,

    username VARCHAR(45) NOT NULL,

    product_id INTEGER,

    category_id INTEGER,

    category_name VARCHAR(45),

    current_price DOUBLE PRECISION NOT NULL,

    sold_price DOUBLE PRECISION,

    sold_quantity INTEGER,

    remaining_quantity INTEGER,

    sales_date TIMESTAMP

);
```

Here, I have created a sales table with necessary columns required.

The description of different attributes of sales columns are:

- user\_id:INTEGER is used as the user\_id is integer.
- username :VARCHAR(45) NOT NULL is used as the username is of varying characters and it cannot be null.
- product\_id: INTEGER is used as the product\_id is numeric.
- category\_id: INTEGER is used as the category\_id is numeric
- current\_price: DOUBLE PRECISION NOT NULL is used as it is variable-precision and has 6 decimal digits precision as price can have that range
- sold\_price:DOUBLE PRECISION is is used as it is variable-precision and has 6 decimal digits precision as price can have that range
- sold\_quantity:INTEGER is used as the sold quantity is an integer.
- remaining\_quantity:INTEGER is used as the remaining\_quantity is an integer.
- sales\_data:TIMESTAMP is used as it is the date and time of the product sold. 


## 2. utils.py file inside src

* `src/utils.py`

We use Postgresql database and use python driver Psycopg2 to connect it .So, we make a method to that with the parameter database\_name to connect to the respective database.

```
Import psycopg2
def connect(database\_name):
    return psycopg2.connect(user="postgres",

                                 password="admin",

                                 host="localhost",

                                 port="5432",

                                 database=database_name

                                 )

```

## 3.healper.py file inside src

There are three methods inside the helper.py file inside src, I will explain them respectively.

# i) 

```
def execute_select_query(query,connection):
    """This is the method to execute the select sql query given the parameter the query and connection method"""
    try:
        conn=connection
        cur=conn.cursor()
        cur.execute(query)
        data=cur.fetchall()

    except(Exception) as e:
        print(e)
    finally:
    if(conn):
        cur.close()
        conn.close()
        return data
```

This is the method which executes the select query given the parameters, query and connection.

So, here we have made the connection and cursor object and executed the query.After the query is executed we have fetched all the data and finally closed the cursor and connection and returned the respective data.

# ii)

```
def execute_insert_query(query,connection,data):
    """This is the method to execute the insert sql query given the parameter the query and connection method and data"""

    try:
        conn=connection
        cur=conn.cursor()
        for item in data:
            cur.execute(query,item)
        conn.commit()
        print(query+",Sucessfully inserted data")
    except(Exception) as e:
        print(e)
    finally:
        if(conn):
            cur.close()
            conn.close()
```


This is the method which executes the insert query given the parameter query , connection and data to be inserted.

Similarly , we have made the connection and cursor object and looped over the data and executed each row and saved the changes to the database by executing the commit method in the conn.

Finally we have closed the cursor and the connection.


# iii)

```
def execute_delete_query(query,connection):
    """This is the method which deletes the table contents"""
    
    try:
        conn=connection
        cur=conn.cursor()
        cur.execute(query)
        conn.commit()
        print(query+",Sucessfully deleted data from sales table of sales_raw")
    except(Exception) as e:
        print(e)
    finally:
        if(conn):
            cur.close()
            conn.close()
```

This is the method to delete all the data from a table, give the query and connection object.

Similarly , we have made the connection and cursor object and deleted the data from the table by executing the query in the cursor object and saved the changes to the database by executing the commit method in the conn.

Finally we have closed the cursor and the connection.


## 4) extract_data_from_ecommerce_dump.py file inside the src/pipeline folder.
* `src/pipeline/extract_data_from_ecommerce_dump.py`

```

from src.helper import execute_select_query
from src.utils import connect

def extract_data_from_ecommerce():
    """This is a method to extract data from ecommerce database"""

    query = """
    SELECT s.user_id , u.username,p.id,c.id,c.name,
    p.price,s.price,s.quantity,(p.quantity-s.quantity),
    s.updated_at  
    FROM sales s
    INNER JOIN users u
        ON s.user_id = u.id
    INNER JOIN products p
        ON s.product_id = p.id
    INNER JOIN categories c 
        ON  p.category_id = c.id
    """
    data=execute_select_query(query,connect("ecommerce_dumb"))
    return data
```

This is the method `extract_data_from_ecommerce()`, which is used to extract the necessary data from the `ecommerce_dumb` database.

This method has a query to select the necessary data.

After that , we use the above mentioned method in  3(i) i.e. `execute_select_query(query,connection)` , to execute the select query by passing the necessary parameter which is the respective query and connect method which takes the database_name as a parameter.

Finally it returns the data.

## 5. load_data_to_sales_and_sales_arhcive.py file inside the src/pipeline folder.

```
import sys
file_path = '/home/sandesh/Desktop/Leapfrog/Data/3rd Week(OLAP Design)/Day3'
sys.path.append(file_path)
```
Firstly , I have used the absolute path to import necessary modules.


```
from src.utils import connect  
```
Importing of the connect function from `src/utils.py` file as described above in (2).



```
from src.helper import execute_select_query
from src.helper import execute_insert_query
from src.helper import  execute_delete_query
```
Importing different functions to execute the necessary SQL queries, It is described above in detail at (3).

```
from src.pipeline.extract_data_from_ecommerce_dump import extract_data_from_ecommerce
```
This is the function to extract the data from the `ecommerce_dump` database.It is describe above in detail at (4).

```
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
```
This is the method which selects all the data from the `sales` table from `sales_raw` database by executing the select query function to get the necessary data.i.e `execute_select_query(query,connect("sales_raw"))`

After that it inserts the data to the sales table of `sales_archive` database.i.e `execute_insert_query(query_1,connect("sales_archive"),data)`

```
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
```

This is the method which is called in the main method.Firsty , it fetches all the data from the ecommerce\_dump by calling the function `extract_data_from_ecommerce()`.

After that is loades the data available in `sales_raw` database to `sales_archive` database.

Then , after successfully loading the data from `sale_raw` database to `sale_archive` , we can clear the `sales_raw` database, so we execute the delete query in the sales table of `sales_raw` database.i.e. `execute_delete_query(query,connect("sales_raw"))` passing the necessary parameters.

After that the necessary new data is inserted into the `sales_raw` by calling the `execute_insert_query(query,connect("sales_raw"),data)` passing the necessary parameters..
