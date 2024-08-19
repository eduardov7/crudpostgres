from flask import render_template, request, redirect, url_for
from app import app
from app.db import get_db_connection

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM items')  # Asegúrate de que esta consulta refleje tu tabla
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', data=data)

@app.route('/add', methods=['POST'])
def add_record():
    conn = get_db_connection()
    cur = conn.cursor()
    name = request.form['name']
    cur.execute('INSERT INTO items (name) VALUES (%s)', (name,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['POST'])
def edit_record(id):
    conn = get_db_connection()
    cur = conn.cursor()
    name = request.form['name']
    cur.execute('UPDATE items SET name = %s WHERE id = %s', (name, id))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete_record(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM items WHERE id = %s', (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))
