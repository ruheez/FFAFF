<!DOCTYPE html>
<html>
<head>
    <title>Web Traffic Generator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        h1 {
            text-align: center;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <h1>Web Traffic Generator</h1>

    <pre>
        <?php
        // Execute the Python script
        $output = shell_exec('python gen.py');

        // Display the output
        echo $output;
        ?>
    </pre>
</body>
</html>
