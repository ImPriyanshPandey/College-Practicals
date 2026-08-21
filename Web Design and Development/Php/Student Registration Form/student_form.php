<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $rollNumber = $_POST['rollNumber'];
    $firstName = $_POST['firstName'];
    $lastName = $_POST['lastName'];
    $gender = $_POST['gender'];
    $department = $_POST['department'];
    $dob = $_POST['dob'];

    echo "<h3>Form Data Submitted:</h3>";
    echo "Roll Number: $rollNumber<br>";
    echo "First Name: $firstName<br>";
    echo "Last Name: $lastName<br>";
    echo "Gender: $gender<br>";
    echo "Department: $department<br>";
    echo "Date of Birth: $dob<br>";
}
?>
