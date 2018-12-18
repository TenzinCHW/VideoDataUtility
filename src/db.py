import sqlite3
import os

#proj_root = os.path.join('..', os.path.dirname(__file__))
proj_root = '..'

class DatabaseConnector():
    def __init__(self, DBs=None):
        if DBs is not None:
            self.conns = {}
            self.curs = {}
            for db in DBs:
                self.conns[db], self.curs[db] = self.connect(db)

    def connect(self, db):
        db_path = os.path.join(proj_root, 'db', db + '.db')
        connection = sqlite3.connect(db_path)
        c = connection.cursor()
        return connection, c

    def init_db_table(self, db, table, values):
        try:
            self.curs[db].execute('CREATE TABLE {} ({})'.format(table, values))
        except sqlite3.Error as e:
            print('Error occurred: ', e.args[0])
        self.conns[db].commit()

    def fetchone(self, db, table, cols, cond):  # TODO support >1 cond
        cols = ','.join(cols)
        statement = 'SELECT ' + cols + ' FROM ' + table + ' WHERE ' + cond[0] + '=?'
        self.curs[db].execute(statement, (cond[1],))
        return  self.curs[db].fetchone()

    def insert(self, db, table, cols, values):
        cols = '(' + ','.join(cols) + ')'
        replace_val = '(' + ','.join('?' for _ in values) + ')'
        statement = table + cols
        self.curs[db].execute('INSERT INTO ' + statement + ' VALueS '
                        + replace_val, values)
        self.conns[db].commit()

    def update(self, db, table, cols, values, cond):    # TODO support >1 cond
        pass

    def __del__(self):
        try: _ = self.conns
        except: return
        for conn in self.conns.values():
            conn.close()
