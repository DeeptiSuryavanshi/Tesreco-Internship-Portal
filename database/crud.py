from database.db import get_connection

def add_intern(name,email,domain):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO Interns(name,email,domain)
    VALUES(?,?,?)
    """,(name,email,domain))

    conn.commit()
    conn.close()

def get_all_interns():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM Interns")

    interns = cur.fetchall()

    conn.close()

    return interns

def update_intern(id,name,email,domain):

    conn = get_connection()

    conn.execute("""
    UPDATE Interns
    SET name=?,email=?,domain=?
    WHERE intern_id=?
    """,(name,email,domain,id))

    conn.commit()
    conn.close()

def delete_intern(id):

    conn = get_connection()

    conn.execute("""
    DELETE FROM Interns
    WHERE intern_id=?
    """,(id,))

    conn.commit()
    conn.close()        
