"""MySQL where: safe MySQL mini-project using session-scoped demo tables."""

import os

import mysql.connector


def main() -> None:
    required = ("MYSQL_HOST", "MYSQL_USER", "MYSQL_PASSWORD", "MYSQL_DATABASE")
    missing = [key for key in required if not os.environ.get(key)]
    if missing:
        raise RuntimeError("Configure a local development connection: " + ", ".join(missing))
    connection = mysql.connector.connect(
        host=os.environ["MYSQL_HOST"],
        port=int(os.environ.get("MYSQL_PORT", "3306")),
        user=os.environ["MYSQL_USER"],
        password=os.environ["MYSQL_PASSWORD"],
        database=os.environ["MYSQL_DATABASE"],
        connection_timeout=5,
    )
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("CREATE TEMPORARY TABLE course_topic_rows (id INT AUTO_INCREMENT PRIMARY KEY, category VARCHAR(40) NOT NULL, score INT NOT NULL)")
        cursor.executemany(
            "INSERT INTO course_topic_rows (category, score) VALUES (%s, %s)",
            [("alpha", 72), ("beta", 88), ("gamma", 95)],
        )
        cursor.execute("SELECT id, category, score FROM course_topic_rows WHERE score >= %s", (80,))
        print(cursor.fetchall())
        connection.commit()
        cursor.close()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


if __name__ == "__main__":
    main()
