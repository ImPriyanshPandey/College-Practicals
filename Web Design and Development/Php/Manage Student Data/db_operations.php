<?php
$conn = new mysqli('localhost', 'root', '', 'StudentDB');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $action = $_POST['action'];
    $rollNumber = $_POST['rollNumber'];
    $name = $_POST['name'];
    $department = $_POST['department'];

    if ($action === 'add') {
        $sql = "INSERT INTO Students (roll_number, name, department) VALUES ('$rollNumber', '$name', '$department')";
        if ($conn->query($sql) === TRUE) {
            echo "The record is added in the database!";
        } else {
            echo "Error: " . $conn->error;
        }
    } elseif ($action === 'delete') {
        $sql = "DELETE FROM Students WHERE roll_number='$rollNumber'";
        if ($conn->query($sql) === TRUE) {
            echo "A record is deleted from the database!";
        } else {
            echo "Error: " . $conn->error;
        }
    } elseif ($action === 'display') {
        $sql = "SELECT * FROM Students";
        $result = $conn->query($sql);
        if ($result->num_rows > 0) {
            echo "<table border='1'><tr><th>ID</th><th>Roll Number</th><th>Name</th><th>Department</th></tr>";
            while ($row = $result->fetch_assoc()) {
                echo "<tr><td>" . $row['id'] . "</td><td>" . $row['roll_number'] . "</td><td>" . $row['name'] . "</td><td>" . $row['department'] . "</td></tr>";
            }
            echo "</table>";
        } else {
            echo "No records found.";
        }
    }
}
$conn->close();
?>
