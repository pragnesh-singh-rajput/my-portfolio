<html>
<body>
    <?php
    $db = pg_connect('host=ec2-23-23-151-191.compute-1.amazonaws.com dbname=d5j0psocpfpomk user=slzebheschodut password=e315cba5590679f755c775ca182ba5e3501993ff2564b841e92d6741d1dac9b5');

    $firstname = pg_escape_string($_POST['firstname']);
    $surname = pg_escape_string($_POST['surname']);
    $emailaddress = pg_escape_string($_POST['emailaddress']);

    $query = "INSERT INTO (firstname, surname, emailaddress) VALUES('" . $firstname . "', '" . $surname . "', '" . $emailaddress . "')";
    $result = pg_query($query);
    if (!$result) {
        $errormessage = pg_last_error();
        echo "Error with query: " . $errormessage;
        exit();
    }
    printf ("These values were inserted into the database - %s %s %s", $firstname, $surname, $emailaddress);
    pg_close();
    ?>
</body>
</html> 
