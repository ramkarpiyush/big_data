CREATE TABLE labours (
    id INT  AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    wage INT,
    role VARCHAR(50),
    email VARCHAR(50)
);

CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    labour_id INT NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME DEFAULT NULL,
    FOREIGN KEY (labour_id) REFERENCES home.labours(id)
);

CREATE TABLE skills (
    id INT AUTO_INCREMENT PRIMARY KEY,
    labour_id INT NOT NULL,
    skills VARCHAR(100),
    FOREIGN KEY (labour_id) REFERENCES home.labours(id)
);