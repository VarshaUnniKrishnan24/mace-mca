<?php
 
         $marks = array( 
            "Anjaly" => array (
               "PHYSICS" => 25,
               "MATHEMATICS" => 20,	
               "CHEMISTRY" => 22
            ),
            
            "Beema" => array (
               "PHYSICS" => 23,
               "MATHEMATICS" => 24,
               "CHEMISTRY" => 22
            ),
            
            "Suriya" => array (
               "PHYSICS" => 29,
               "MATHEMATICS" => 27,
               "CHEMISTRY" => 26
            )
         );
      echo "<table border = 5 ><tr><th colspan =4 >INTERNAL MARKS</th></tr> <tr><td>NAME</td><td>PHYSICS</td><td>MATHEMATICS</td><td>CHEMISTRY</td></tr>";
       
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
   
