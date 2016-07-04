#!/usr/bin/python3
import sqlite3

_DB_FILE = 'rss.db'


class RssDb:
    def __init__(self):
        self._db = sqlite3.connect(_DB_FILE)
        self._db.row_factory = sqlite3.Row
        self._db.execute('''
            CREATE TABLE IF NOT EXISTS feed (
                id INTEGER PRIMARY KEY,
                url TEXT UNIQUE,
                title TEXT,
                description TEXT
            )
        ''')

    def insert(self, rec):
        self._db.execute('''
            INSERT INTO feed (url, title, description)
                VALUES (:url, :title, :description)
        ''', rec)
        self._db.commit()

    def get_by_url(self, url):
        c = self._db.cursor()
        c.execute('SELECT * FROM feed WHERE url = ?', (url,))
        return c.fetchone()

    def get_by_id(self, id):
        c = self._db.cursor()
        c.execute('SELECT * FROM feed WHERE id = ?', (id,))
        return c.fetchone()

    def update(self, rec):
        self._db.execute('''
            UPDATE feed
                SET title = :title, description = :description 
                WHERE url = :url
            ''', rec)
        self._db.commit()

    def del_by_id(self, id):
        self._db.execute('DELETE FROM feed WHERE id = ?', (id,))
        self._db.commit()

    def list(self):
        c = self._db.cursor()
        c.execute('SELECT * FROM feed ORDER BY UPPER(title)')
        for r in c:
            yield r;


def main():
    db = RssDb()
    print('all recs from {}:'.format(_DB_FILE))
    for r in db.list():
        print('{title} [{url}] {description}'.format(**r))


if __name__ == '__main__':
    main()
