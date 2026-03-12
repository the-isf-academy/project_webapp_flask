import sqlite3

# DATABASE INTERACTIONS

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row #converts row to dictionary object
    return conn

def get_all_records(table_name,order_column):
    '''Returns all records from the database'''

    conn = get_db_connection()

    all_records = conn.execute(
        f"""
        SELECT *
        FROM {table_name}
        ORDER BY {order_column}
        """).fetchall()  
    
    conn.close()

    return all_records


def get_one_record(table_name, id):
    '''Returns one record  from the database'''

    conn = get_db_connection()

    record = conn.execute(
        """
        SELECT *
        FROM ?
        where id = ?
        """,(table_name, id,)).fetchone()  
    
    conn.close()

    return record



def get_random_records(table_name, num):
    '''Returns multiple random records from the database'''

    conn = get_db_connection()

    random_records = conn.execute(
       f"""
        SELECT *
        from {table_name}
        ORDER BY random()
        limit {num}""").fetchone()   
    
    conn.close()

    return random_records

def new_record(table_name,form_data):
    '''Inserts a new record into the database
    Returns the new record'''


    conn = get_db_connection()

    # 💻  EDIT THIS ↓ EXECUTE STATEMENT TO MATCH YOUR DATABASE
    conn.execute(
        """
        INSERT INTO 
        ? (name, red, green, blue) 
        VALUES (?, ?, ?, ?)""",
        (table_name,form_data['name'], form_data['red'], form_data['green'], form_data['blue'])
    )

    conn.commit()

    new_record = conn.execute(
        f"""
        SELECT * 
        FROM {table_name} 
        ORDER BY id desc
        LIMIT 1
        """).fetchone()

    conn.close()

    return new_record



if __name__=="__main__":
    # testing
    

