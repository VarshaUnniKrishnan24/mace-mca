<?php
$aa=new mysqli("localhost","root","");
if($aa->connect_error)
{
    die("connection failed".$aa->connect_error);
}
$db="create database student_mca_22";
if($aa->query($db)===TRUE)
{
    echo "Database created";
}
 else
{
     echo "error found".$aa->error;
}
$aa->close();
?>
