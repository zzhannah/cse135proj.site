<?php
header('Content-Type: application/json');
header('Cache-Control: no-cache');

$time = date("l m-d H:i:sa Y");
$addr = getenv("REMOTE_ADDR");
$arr = array('title' => 'Hello, Php!', 'message' => 'This page was generated with the Php programming language', 'heading' => 'Hello, Php!', 'time' => $time, 'IP' => $addr);

echo json_encode($arr);
?>
