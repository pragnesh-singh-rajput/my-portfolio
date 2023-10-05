<?php
$name = $_POST['name'];
$email = $_POST['email'];
$password = $_POST['password'];

// Env Secrets
$host = getenv('GITHUB_ACTIONS_HOST');
$username = getenv('GITHUB_ACTIONS_USERNAME');
$password = getenv('GITHUB_ACTIONS_PASSWORD');
$database = getenv('GITHUB_ACTIONS_DATABASE');

// Database connection
$conn = new mysqli($host, $username , $password , $database );
if($conn->connect_error){
    die('Connection Failed : '.$conn->connect_error);
}else{
    $stmt = $conn->prepare("insert into registration(name, email, password)
    values(?, ?, ?)");
    $stmt->bind_param("sss",$name, $email, $password);
    $stmt->execute();
    echo "Registration Successfully...";
    $stmt->close();
    $conn->close();
}
?>