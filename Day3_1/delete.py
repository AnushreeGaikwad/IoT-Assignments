import dbcoon

def delete_person(uid):
    # get connection
    conn = dbcoon.get_connection()

    # form a query
    query = f"delete from employee where uid = %s;"
    val = (uid, )

    # create a cursor
    cursor = conn.cursor()

    # execute the query
    cursor.execute(query, val)

    # commit the changes
    conn.commit()

    # close cursor as well as connection
    cursor.close()
    conn.close()





