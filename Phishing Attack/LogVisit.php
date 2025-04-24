<?php

    require 'Database.php';

    date_default_timezone_set("America/Chicago");

    $ip_address = $_SERVER['REMOTE_ADDR'];
    $type = "visit";
    $current_timestamp = date('Y-m-d H:i:s');

    $statement = $mysqli->prepare("INSERT INTO requests (ip_address, type, timestamp) VALUES (?, ?, ?)");

    if (!$statement) {
        // printf("Error Preparing Query: %s\n", $mysqli->error);
        echo json_encode(array("Response" => "Error Preparing Query: " . $mysqli->error));
        exit;
    } else {
        $statement->bind_param("sss", $ip_address, $type, $current_timestamp);
        $statement->execute();
        $statement->close();
        // printf("Query Sent Successfully!");
        echo json_encode(array("Response" => "Query Sent Successfully!"));
        exit;
    }
?>
