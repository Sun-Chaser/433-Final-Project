<?php

    $mysqli = new mysqli('localhost', 'jack', '!@#$', 'security_project');
    if ($mysqli->connect_errno) {
        printf("Connection Failed: %s\n", $mysqli->connect_error);
        exit;
    }
