<!DOCTYPE HTML>
<html>
<?php
    include("header.php")
?>

<body>
    <div class="container">
        <div class="row">
            <div class="col-md-12"> <h1> Please enter the necessary data below. </h1> </div>
        </div>
        <div class="row">
            <div class="col-md-12">
                <form method="get" action="testing.php">
                    <label for="id"> Participant ID </label> <br>
                    <input type="text" id="id" name="id"></input> <br> <br>

                    <label for="time"> Reaction time </label> <br>
                    <input type="number" id="time" name="time"/> <br> <br>

                    <input type="submit" value="Begin Testing"></input>
                </form>
            </div>
        </div>
    </div>
</body>
    
</html>
