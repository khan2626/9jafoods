#!/usr/bin/python3
"""connects to my database"""
from sqlalchemy import create_engine, text



engine = create_engine(conn_string)

def load_Igbo_Foods():
    """It loads Igbo foods list from database"""
    with engine.connect() as conn:
            result = conn.execute(text('SELECT * FROM `Igbo-foods`'))
            columns = result.keys()
            foods = [dict(zip(columns, row)) for row in result.fetchall()]
            return(foods)
    

def load_Hausa_Foods():
    with engine.connect() as conn:
            """It loads Hausa foods list from database"""
            result = conn.execute(text('SELECT * FROM `Hausa-foods`'))
            columns = result.keys()
            foods = [dict(zip(columns, row)) for row in result.fetchall()]
            return(foods)
    

def load_Yoruba_Foods():
    """It loads Yoruba foods list from database"""
    with engine.connect() as conn:
            result = conn.execute(text('SELECT * FROM `Yoruba-foods`'))
            columns = result.keys()
            foods = [dict(zip(columns, row)) for row in result.fetchall()]
            return(foods)


def load_Drinks():
    """It returns list popular Nigerian drinks from database"""
    with engine.connect() as conn:
            result = conn.execute(text('SELECT * FROM Drinks'))
            columns = result.keys()
            drinks = [dict(zip(columns, row)) for row in result.fetchall()]
            return (drinks)

def load_Pop_Foods():
    """It returns list popular Nigerian drinks from database"""
    with engine.connect() as conn:
            result = conn.execute(text('SELECT * FROM `Pop-foods`'))
            columns = result.keys()
            foods = [dict(zip(columns, row)) for row in result.fetchall()]
            return (foods)