CREATE TABLE IF NOT EXISTS clients(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    salt TEXT,
    balance REAL DEFAULT 0,
    message TEXT);

CREATE TABLE IF NOT EXISTS login_attems(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	client_id INTEGER,
	attempt_status TEXT,
	timestamp DATETIME,
	FOREIGN KEW(client_id) REFERENCES clients(id)
	);