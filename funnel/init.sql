CREATE DATABASE IF NOT EXISTS idsBench;
USE idsBench;

CREATE TABLE IF NOT EXISTS brokerMessage(
    id INT AUTO_INCREMENT PRIMARY KEY, 
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    temperature DECIMAL(3,1),
    capacity INT,
    message VARCHAR(50)
);

INSERT INTO brokerMessage (time, message) VALUES
    ('2023-01-01 12:00:00', 'Sample message 1'),
    ('2023-02-15 08:30:00', 'Another message here'),
    ('2023-03-20 18:45:00', 'This is a third message');