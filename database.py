"""
=========================================================
AlgoPipX Educational Assistant
Database Manager
=========================================================
"""

import sqlite3
from datetime import datetime
from config import DATABASE_NAME


# -------------------------------------------------------
# Database Connection
# -------------------------------------------------------

def get_connection():
    return sqlite3.connect(DATABASE_NAME)


# -------------------------------------------------------
# Initialize Database
# -------------------------------------------------------

def init_database():

    conn = get_connection()
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (

        user_id INTEGER PRIMARY KEY,

        username TEXT,

        first_name TEXT,

        language TEXT DEFAULT 'en',

        joined_date TEXT

    )
    """)


    # FAQ table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS faqs (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        question TEXT,

        answer TEXT

    )
    """)


    conn.commit()
    conn.close()


# -------------------------------------------------------
# User Management
# -------------------------------------------------------

def add_user(
        user_id,
        username=None,
        first_name=None
):

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("""
    INSERT OR IGNORE INTO users
    (
        user_id,
        username,
        first_name,
        joined_date
    )
    VALUES (?, ?, ?, ?)

    """,
    (
        user_id,
        username,
        first_name,
        datetime.utcnow().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    ))


    conn.commit()
    conn.close()



def update_language(
        user_id,
        language
):

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        """
        UPDATE users
        SET language = ?
        WHERE user_id = ?
        """,
        (
            language,
            user_id
        )
    )


    conn.commit()
    conn.close()



def get_user_language(user_id):

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT language
        FROM users
        WHERE user_id = ?
        """,
        (user_id,)
    )


    result = cursor.fetchone()

    conn.close()


    if result:
        return result[0]

    return "en"



def get_all_users():

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT user_id
        FROM users
        """
    )


    users = cursor.fetchall()

    conn.close()


    return [
        user[0]
        for user in users
    ]



def get_user_count():

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT COUNT(*)
        FROM users
        """
    )


    count = cursor.fetchone()[0]

    conn.close()


    return count



# -------------------------------------------------------
# FAQ Management
# -------------------------------------------------------

def add_faq(question, answer):

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO faqs
        (
            question,
            answer
        )
        VALUES (?, ?)
        """,
        (
            question,
            answer
        )
    )


    conn.commit()
    conn.close()



def get_faqs():

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT id, question, answer
        FROM faqs
        ORDER BY id DESC
        """
    )


    data = cursor.fetchall()

    conn.close()


    return data



def get_faq(faq_id):

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT question, answer
        FROM faqs
        WHERE id = ?
        """,
        (faq_id,)
    )


    faq = cursor.fetchone()

    conn.close()


    return faq



def delete_faq(faq_id):

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        """
        DELETE FROM faqs
        WHERE id = ?
        """,
        (faq_id,)
    )


    conn.commit()
    conn.close()



# -------------------------------------------------------
# Backup / Utility
# -------------------------------------------------------

def clear_database():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM users"
    )

    cursor.execute(
        "DELETE FROM faqs"
    )


    conn.commit()
    conn.close()
