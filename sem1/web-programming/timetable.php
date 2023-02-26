
      <?php
 
         $marks = array( 
            "mohammad" => array (
               "physics" => 35,
               "maths" => 30,	
               "chemistry" => 39
            ),
            
            "qadir" => array (
               "physics" => 30,
               "maths" => 32,
               "chemistry" => 29
            ),
            
            "zara" => array (
               "physics" => 31,
               "maths" => 22,
               "chemistry" => 39
            )
         );
      echo "<table border = 5 ><tr><th colspan =4 >INTERNAL MARKS</th></tr> <tr><td>NAME</td><td>PHYSICS</td><td>MATHS</td><td>CHEMISTRY</td></tr>";
       
  foreach($marks as $name => $mark)
 {
      echo "<tr><td >".$name."</td>";
 foreach($mark as $num => $value)
 {
 echo"<td>" .$value. "</td>";
 }
 echo "</tr>";
 }
 echo "</table>"
      ?>
   


