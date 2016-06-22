#!/usr/local/bin/python3
import sqlite3
import os

current_directory = os.path.dirname(os.path.realpath(__file__))


def insert(db, row):
    db.execute('insert into test (t1, i1) values (?, ?)', (row['t1'], row['i1']))
    db.commit()


def retrieve(db, t1):
    cursor = db.execute('select * from test where t1 = ?', (t1,))
    return cursor.fetchone()


def update(db, row):
    db.execute('update test set i1 = ? where t1 = ?', (row['i1'], row['t1']))
    db.commit()


def delete(db, t1):
    db.execute('delete from test where t1 = ?', (t1,))
    db.commit()


def display_rows(db):
    cursor = db.execute('select * from test order by t1')
    for row in cursor:
        print('  {}: {}'.format(row['t1'], row['i1']))


class DatabaseObject:
    def __init__(self, **kwargs):
        self.filename = kwargs.get('filename')
        self.table = kwargs.get('table', 'test')

    def sql_do(self, sql, *params):
        self._db.execute(sql, params)
        self._db.commit()

    def insert(self, row):
        self._db.execute('insert into {} (t1, i1) values (?, ?)'.format(self._table), (row['t1'], row['i1']))
        self._db.commit()

    def retrieve(self, key):
        cursor = self._db.execute('select * from {} where t1 = ?'.format(self._table), (key,))
        return dict(cursor.fetchone())

    def update(self, row):
        self._db.execute(
            'update {} set i1 = ? where t1 = ?'.format(self._table),
            (row['i1'], row['t1']))
        self._db.commit()

    def delete(self, key):
        self._db.execute('delete from {} where t1 = ?'.format(self._table), (key,))
        self._db.commit()

    def display_rows(self):
        cursor = self._db.execute('select * from {} order by t1'.format(self._table))
        for row in cursor:
            print('  {}: {}'.format(row['t1'], row['i1']))

    def __iter__(self):
        cursor = self._db.execute('select * from {} order by t1'.format(self._table))
        for row in cursor:
            yield dict(row)

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, fn):
        self._filename = fn
        self._db = sqlite3.connect(fn)
        self._db.row_factory = sqlite3.Row

    @filename.deleter
    def filename(self):
        self.close()

    @property
    def table(self):
        return self._table

    @table.setter
    def table(self, t):
        self._table = t

    @table.deleter
    def table(self):
        self._table = 'test'

    def close(self):
        self._db.close()
        del self._filename


# sqlite3
def main():
    db = sqlite3.connect(os.path.join(current_directory, 'test.db'))
    db.execute('drop table if exists test')
    db.execute('create table test (t1 text, i1 int)')
    db.execute('insert into test (t1, i1) values (?, ?)', ('one', 1))
    db.execute('insert into test (t1, i1) values (?, ?)', ('two', 2))
    db.execute('insert into test (t1, i1) values (?, ?)', ('three', 3))
    db.execute('insert into test (t1, i1) values (?, ?)', ('four', 4))
    db.execute('insert into test (t1, i1) values (?, ?)', ('five', 5))
    db.commit()
    cursor = db.execute('select * from test order by t1')
    for row in cursor:
        print(row)
    db.execute('drop table if exists test')
    db.execute('create table test (t1 text, i1 int)')
    print()

    db.row_factory = sqlite3.Row
    cursor = db.execute('select * from test order by t1')
    for row in cursor:
        print(dict(row), row['t1'], row['i1'])
    print()

    print('--CRUD part')
    print('Create rows')
    insert(db, dict(t1='one', i1=1))
    insert(db, dict(t1='two', i1=2))
    insert(db, dict(t1='three', i1=3))
    insert(db, dict(t1='four', i1=4))
    display_rows(db)

    print('Retrieve rows')
    print(dict(retrieve(db, 'one')), dict(retrieve(db, 'two')))

    print('Update rows')
    update(db, dict(t1='one', i1=101))
    update(db, dict(t1='three', i1=103))
    display_rows(db)

    print('Delete rows')
    delete(db, 'one')
    delete(db, 'three')
    display_rows(db)
    print()

    print('--DBO')
    db = DatabaseObject(filename='test.db', table='test')

    print('Create table test')
    db.sql_do('drop table if exists test')
    db.sql_do('create table test ( t1 text, i1 int )')

    print('Create rows')
    db.insert(dict(t1='one', i1=1))
    db.insert(dict(t1='two', i1=2))
    db.insert(dict(t1='three', i1=3))
    db.insert(dict(t1='four', i1=4))
    for row in db:
        print(row)

    print('Retrieve rows')
    print(db.retrieve('one'), db.retrieve('two'))

    print('Update rows')
    db.update(dict(t1='one', i1=101))
    db.update(dict(t1='three', i1=103))
    for row in db:
        print(row)

    print('Delete rows')
    db.delete('one')
    db.delete('three')
    for row in db:
        print(row)


if __name__ == '__main__':  # some comments in source code
    main()
