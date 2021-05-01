<!DOCTYPE HTML>
<html>
<?php
    include("header.php")
?>

<?php
    // number to be tested for accuracy.
    $NUMBER = rand(1, 9);
?>

<script>
let elements = [
    0, 4, 4, 4, 6, 5, 7, 8, 8, 5
];
number = <?php echo $NUMBER?>;
picture = Math.floor(Math.random()*elements[number]);
console.log(number, picture);
src = `./Tests/${number}/${picture}.PNG`

img = new Image(400, 300)
img.src = src;

function display() {
    milliseconds = <?php echo $_GET["time"]?>;
    console.log(milliseconds);

    el = document.querySelector("#workspace")

    el.appendChild(img);

    setTimeout(() => {
        console.log("run");
        img.style.display = 'none';
    }, milliseconds);
}
</script>

<body>
    <div class="container">
        <div class="row">
            <div class="col-md-12"> <h1> Test </h1> </div>
        </div>

        <div class="row">
        <div class="col-lg-12"> <button onclick="display()"> Conduct Test </button></div>
        </div>
        <div class="row" id="workspace" style="text-align:center">
        </div>

        <div class="row">
            <div class="col-md-12">
                <form method="post" action="handler.php">
                    <label for="answer" name="answer"> Enter Answer (Required) </label> <br>
                    <input type="number" name="answer" id="answer"/> <br><br>

                    <label for="angle" name="angle"> Enter the angle </label> <br>
                    <input type="angle" name="angle" id="angle" value="<?php echo $_GET["angle"]?>"/> <br><br>
                    
                    <!-- metadata about experiment (can be changed) -->
                    <label for="time" name="time"> Reaction Time (leave alone unless changes). </label> <br>
                    <input type="number" name="time" id="time" value="<?php echo $_GET["time"]?>"/> <br><br>

                    <input type="hidden" id="id" name="id" value="<?php echo $_GET["id"]?>"></input>
                    <input type="hidden" id="correct" name="correct" value="<?php echo $NUMBER ?>"></input>


                    <input type="submit" value="Submit"></input>
                </form>
            </div>
        </div>
    </div>
</body>


    
</html>
