<?php

    require 'database.php';

    $ip_address = $_SERVER['REMOTE_ADDR'];
    $type = "submit";

    $statement = $mysqli->prepare("insert into requests (ip_address, type) values (?, ?)");

    if (!$statement) {
        printf("Error Preparing Query: %s\n", $mysqli->error);
        exit;
    } else {
        $statement->bind_param("ss", $ip_address, $type);
        $statement->execute();
        $statement->close();
        printf("Query Sent Successfully!");
        exit;
    }

?>
