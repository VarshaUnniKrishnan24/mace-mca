<html>
    <head>
        <style>
            table{
                border-collapse:collapse;
                border-color:black;
            }
        </style>
    </head>
    
    <body>
        <form method="post" action="">
            <center><h1>Enter details of items</h1>
                <h3>Item code <input type="text" name="ic" placeholder="1,2,3,4"/></h3>
                <h3>Item name <input type="text" name="in"/></h3>
                <h3>Quantity  <input type="text" name="qu"/></h3>
                <h3>Rate      <input type="text" name="ra"/></h3>
                <input type="submit" value="submit"/>
            </center>
                
        </form>
    </body>
</html>


<?php
if($_POST){
         
         $ic=$_POST['ic'];
         $in=$_POST['in'];
         $qu=$_POST['qu'];
         $ra=$_POST['ra'];
         
         
         $ico=explode(',',$ic);
         $n=count($ico);
         $ina=explode(',',$in);
         $qua=explode(',',$qu);
         $rate=explode(',',$ra);
         $tot=0;
         
         for($x=0;$x<$n;$x++)
         {
             $tot+=($qua[$x]*$rate[$x]);
         }
         
         echo "<table align=center border=1>";
         echo "<tr><td> <b>Item code</b></td><td><b>Item name</b></td><td> <b>Quantity</b></td><td> <b>Rate</b></td></tr>";
         for($x=0;$x<$n;$x++)
         echo "<tr><td>".$ico[$x]."</td><td>".$ina[$x]."</td><td>".$qua[$x]."</td><td>".$rate[$x]."</td></tr>";
          echo "<tr><th colspan=4></th></tr>";
         echo "<tr><th colspan=3>Total amount</th><td>".$tot."</td></tr>";
         echo "</table>";
         
}
?>
     
                
