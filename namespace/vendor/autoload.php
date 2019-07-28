<?php

spl_autoload_register(function ($class_name) {

    $dir = "php-classe";
    $filename = $dir.DIRECTORY_SEPARATOR. $class_name. ".php";

    if(file_exists($filename)){

        echo $filename."<br>";
        require_once ("$filename");

    }

});