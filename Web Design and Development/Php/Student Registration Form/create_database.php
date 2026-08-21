<?php
$conn = new mysqli('localhost', 'root', '', '');

// Create database
$sql = "CREATE DATABASE IF NOT EXISTS StudentDB";
if ($conn->query($sql) === TRUE) {
    echo "Database created successfully.<br>";
} else {
    echo "Error creating database: " . $conn->error;
}

// Create table
$conn->select_db('StudentDB');
$tableSql = "CREATE TABLE IF NOT EXISTS Students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    roll_number VARCHAR(10),
    name VARCHAR(50),
    department VARCHAR(50)
)";
if ($conn->query($tableSql) === TRUE) {
    echo "Table created successfully.";
} else {
    echo "Error creating table: " . $conn->error;
}
$conn->close();
?>
