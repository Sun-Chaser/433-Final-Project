<?php

    require 'Database.php';

    $ip_address = $_SERVER['REMOTE_ADDR'];
    $type = "visit";
    $current_timestamp = date('Y-m-d H:i:s');

    $statement = $mysqli->prepare("INSERT INTO requests (ip_address, type, timestamp) VALUES (?, ?, ?)");

    if (!$statement) {
        // printf("Error Preparing Query: %s\n", $mysqli->error);
        exit;
    } else {
        $statement->bind_param("sss", $ip_address, $type, $current_timestamp);
        $statement->execute();
        $statement->close();
        // printf("Query Sent Successfully!");
        exit;
    }
?>
