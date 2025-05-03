import sqlite3
from datetime import datetime, timezone

DB_FILE = "gpt_memory.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memory_journal (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            message TEXT,
            timestamp TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prompt_queue (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            agent_name TEXT,
            prompt TEXT,
            priority INTEGER,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_event(source, message):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    timestamp = datetime.now(timezone.utc).isoformat()
    cursor.execute("INSERT INTO memory_journal (source, message, timestamp) VALUES (?, ?, ?)",
                   (source, message, timestamp))
    conn.commit()
    conn.close()

def queue_prompt(agent_name, prompt, priority):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    timestamp = datetime.now(timezone.utc).isoformat()
    cursor.execute("INSERT INTO prompt_queue (agent_name, prompt, priority, timestamp) VALUES (?, ?, ?, ?)",
                   (agent_name, prompt, priority, timestamp))
    conn.commit()
    conn.close()

def fetch_memory():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT source, message, timestamp FROM memory_journal ORDER BY id DESC")
    results = cursor.fetchall()
    conn.close()
    return [{"source": r[0], "message": r[1], "timestamp": r[2]} for r in results]

def fetch_prompt_queue():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT agent_name, prompt, priority FROM prompt_queue ORDER BY id ASC")
    results = cursor.fetchall()
    conn.close()
    return [{"agent_name": r[0], "prompt": r[1], "priority": r[2]} for r in results]

def clear_prompt_queue():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM prompt_queue")
    conn.commit()
    conn.close()

def log_event_to_db(source, message, timestamp):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO memory_journal (source, message, timestamp)
        VALUES (?, ?, ?)
    ''', (source, message, timestamp))
    conn.commit()
    conn.close()

def get_prompt_queue():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT agent_name, prompt, priority FROM prompt_queue ORDER BY priority DESC')
    rows = cursor.fetchall()
    conn.close()
    return [{"agent_name": r[0], "prompt": r[1], "priority": r[2]} for r in rows]

def clear_prompt_queue():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM prompt_queue')
    conn.commit()
    conn.close()

