<?php

    // Prepare variables for database connection
   
    $dbusername = "root";  // enter database username, I used "arduino" in step 2.2
    $dbpassword = "";  // enter database password, I used "arduinotest" in step 2.2

    try{
        $conn = new PDO('mysql:dbname=test;host=localhost',$dbusername,$dbpassword);
        if(!isset( $_GET["value"])){
            throw new Exception('value not found');
        }
        $value = $_GET["value"];
        $sql = "INSERT INTO `sensor` ( `value`) VALUES (:value);";
        $stm = $conn->prepare($sql);
        $stm->execute(['value'=> $value]);
        echo 'done';
    }
    catch (Exception $e){
        echo $e->getMessage();
    }


?>