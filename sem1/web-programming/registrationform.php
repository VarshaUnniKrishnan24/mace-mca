<html>
    <head>
        <title>registration form</title>
        <script type="text/javascript">
            function validate()
            {
                if(document.reg.n.value=="")
                {
                    alert("Name required");
                    document.reg.n.focus();
                    return false;
                }
                
                if(document.reg.p.value=="")
                {
                    alert("Phone number required");
                    document.reg.p.focus();
                    return false;
                }
            }
            </script>
    </head>
    
    
    
    <body bgcolor="tomato">
    <center>
        <h1>REGISTRATION FORM</h1>
        <form action="registrationform.php" method="POST" name="reg" onsubmit="return(validate());">
            <table>
                <tr>
                    <th>Name</th>
                    <td><input type="text" name="n"></td>
                </tr>
                
                
                <tr>
                    <th>Date of Birth</th>
                    <td><input type="date" name="d"></td>
                </tr>
                
                
                <tr>
                    <th>Gender</th>
                    <td>Male<input type="radio" name="g"><br>Female<input type="radio" name="g"><br>Other<input type="radio" name="g"></td>
                </tr>
                
                
                <tr>
                    <th>Address</th>
                    <td><textarea></textarea></td>
                </tr>
                
                
                <tr>
                    <th>Phone Number</th>
                    <td><input type="text" name="p"></td>
                </tr>
                
                
                <tr>
                    <th>Guardian</th>
                    <td><input type="text" name="gu"></td>
                </tr>
                
                <tr>
                    <th>Hobbies</th>
                    <td>Dancing<input type="checkbox" name="d"><br>Singing<input type="checkbox" name="s"><br>Drawing<input type="checkbox" name="dr"><br>Reading<input type="checkbox" name="r"><br.Playing<input type="checkbox" name="pl"><br>Other<input type="checkbox" name="O"></td>
                    
                </tr>
                
                <tr>
                    <th>Extra Curricular Activities</th>
                    <td><input type="text" name="EX"></td>
                </tr>
                
               
                <tr>
                    <th>Courses</th>
                    <td><select id="Courses">
                            <option Value=""></option>
                            <option Value="BA">BA</option>
                            <option Value="B.Sc">B.Sc</option>
                            <option Value="BCA">BCA</option>
                        </select>
                    </td>
                </tr>
                
                
            </table>
            <br><input type="submit" value="submit">
        </form>
    </center>
        
    </body>
    
</html>