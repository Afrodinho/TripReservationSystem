<html>
<head>
    <title>Login</title>
</head>
<body>
    <?php
    if (isset($_POST['Login'])) {
        $username = "Username: " . $_POST['username'];
        $password = "Password: " . $_POST['password'];

        $passcodes = "passcodes.txt";
        // Reading Passcodes.txt for admin information
        $passcodeFile = fopen($passcodes, 'r');
        // Perform operations on file if needed
        fclose($passcodeFile);
    }
    ?>
    //redirect_to('reserve.html');
</body>
</html>
