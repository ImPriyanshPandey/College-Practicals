<!DOCTYPE html>
<html>
<head>
    <title>Sum of Even Digits</title>
</head>
<body>
    <form method="POST">
        <label for="number">Enter a Number:</label>
        <input type="text" id="number" name="number" required>
        <button type="submit">Calculate</button>
    </form>
    <?php
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $number = $_POST['number'];
        $sum = 0;

        // Loop through each character in the string
        for ($i = 0; $i < strlen($number); $i++) {
            $digit = intval($number[$i]); // Convert character to integer
            if ($digit % 2 === 0) {       // Check if the digit is even
                $sum += $digit;          // Add the even digit to the sum
            }
        }

        // Correctly display the result
        echo "<p>Sum of even digits: $sum</p>";
    }
    ?>
</body>
</html>
