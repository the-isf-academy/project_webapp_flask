import sqlite3

# DATABASE INTERACTIONS

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row #converts row to dictionary object
    return conn

def get_all_colors(order_column):
    '''Returns all riddles from the database'''

    conn = get_db_connection()

    all_colors = conn.execute(
        f"""
        SELECT *
        FROM colors
        ORDER BY {order_column}
        """).fetchall()  
    
    conn.close()

    return all_colors


def get_one_color(id):
    '''Returns all riddles from the database'''

    conn = get_db_connection()

    color = conn.execute(
        """
        SELECT *
        FROM colors
        where id = ?
        """,(id,)).fetchone()  
    
    conn.close()

    return color

def get_colors_name(name):
    '''Returns riddles queried on the name database'''

    search_color = f"%{name}%"

    conn = get_db_connection()

    color = conn.execute(
        """
        SELECT *
        FROM colors
        where name like ?
        """,(search_color,)).fetchall()  
    
    conn.close()

    return color

def get_random_color():
    '''Returns all riddles from the database'''

    conn = get_db_connection()

    color = conn.execute(
       f"""
        SELECT *
        from colors
        ORDER BY random()
        limit 1""").fetchone()   
    
    conn.close()

    return color

def new_color(form_data):
    '''Inserts a new riddle into the database
    Returns the new riddle'''


    conn = get_db_connection()
    conn.execute(
        """
        INSERT INTO 
        colors (name, red, green, blue) 
        VALUES (?, ?, ?, ?)""",
        (form_data['name'], form_data['red'], form_data['green'], form_data['blue'])
    )

    conn.commit()

    new_color = conn.execute(
        """
        SELECT * 
        FROM colors 
        ORDER BY id desc
        LIMIT 1
        """).fetchone()

    conn.close()

    return new_color


def update_color(id, form_data):
    """Updates an existing color in the database by id."""
    conn = get_db_connection()
    print(form_data)
    conn.execute(
        """
        UPDATE colors
        SET name = ?, red = ?, green = ?, blue = ?
        WHERE id = ?
        """,
        (form_data['name'], form_data['red'], form_data['green'], form_data['blue'], id)
    )
    conn.commit()
    updated_color = conn.execute(
        """
        SELECT *
        FROM colors
        WHERE id = ?
        """,
        (id,)
    ).fetchone()
    conn.close()
    return updated_color


if __name__=="__main__":
    for color in get_all_colors():
        print(color['name'], color['red'], color['green'], color['blue'])

    

