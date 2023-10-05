<?php
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
    $stmt = $conn->prepare("select * from registration where email = ?");
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $stmt_result = $stmt->get_result();
    if($stmt_result->num_rows > 0){
        $data = $stmt_result->fetch_assoc();
        if($data['password'] === $password){
            echo "<h2>Login Successfully</h2>";
        }else{
            echo "<h2>Invalid Email or Password</h2>";
        }
    }else{
        echo "<h2>Invalid Email or Password</h2>";
    }
}
?>