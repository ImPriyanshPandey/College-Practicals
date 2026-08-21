<!DOCTYPE html>
<html>
<head>
    <title>Multiplication Table</title>
</head>
<body>
    <form method="POST">
        <label for="number">Enter a Number:</label>
        <input type="number" id="number" name="number" required>
        <button type="submit">Generate Table</button>
    </form>
    <?php
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $number = $_POST['number'];
        echo "<h3>Multiplication Table for $number</h3>";
        echo "<table border='1'>";
        for ($i = 1; $i <= 10; $i++) {
            $result = $number * $i;
            echo "<tr><td>$number x $i</td><td>$result</td></tr>";
        }
        echo "</table>";
    }
    ?>
</body>
</html>
