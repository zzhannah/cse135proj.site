<?php
header('Content-Type: text/html');
header('Cache-Control: no-cache');
?>
<!DOCTYPE html>
<html>
    <head>
        <title>Environment Variables</title>
    </head>
    <body>
        <h1 align="center">Environment Variables</h1>
        <hr>
        <?php
            //echo "Environment Varib"
            $env_array = getenv();
            foreach ($env_array as $key=>$value){
                echo "$key => $value <br />";
            }
        ?>
    </body>    
</html>
