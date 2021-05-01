<!DOCTYPE HTML>
<html>
<?php
    include("header.php")
?>

<body>
    <div class="container">
        <div class="row">
            <div class="col-md-12"> <h1> Handler </h1> </div>
        </div>
        <div class="row">
            <div class="col-md-12">
                <form method="get" action="./testing.php">
                    <input type="submit" value="Press to conduct another test."></input> <br><br>
                    <label for="time"> Time </label>
                    <input type="number" id="time" name="time" value="<?php echo $_POST["time"]?>"></input> <br><br>
                    <label for="id"> Name </label>
                    <input id="id" name="id" value="<?php echo $_POST["id"]?>"></input> <br><br>
                    <label for="angle"> Angle </label>
                    <input id="angle" name="angle" value="<?php echo $_POST["angle"]?>"></input> <br><br>
                </form>
            </div>
        </div>
    </div>
</body>

<?php
// script to send all of this data to a file.
$file = fopen("data.txt", "a") or die("Unable to open file!");

$time=$_POST["time"];
$id = $_POST["id"];
$answer = $_POST["answer"];
$correct = $_POST["correct"];
$angle = $_POST["angle"];

$data = "time: $time id: $id answer: $answer correct: $correct angle: $angle \n";

fwrite($file, $data);
?>
    
</html>
