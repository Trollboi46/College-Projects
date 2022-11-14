<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>book</title>

    <!-- swiper css link  -->
    <link rel="stylesheet" href="https://unpkg.com/swiper@7/swiper-bundle.min.css" />

    <!-- font awesome cdn link  -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

    <!-- custom css file link  -->
    <link rel="stylesheet" href="css/style.css">

</head>

<body>
    <?php
    require('db.php');
    // When form submitted, check and create user session.
    if (isset($_POST['username'])) {
        $username = stripslashes($_REQUEST['username']);    // removes backslashes
        $username = mysqli_real_escape_string($con, $username);
        $password = stripslashes($_REQUEST['password']);
        $password = mysqli_real_escape_string($con, $password);
        // Check user is exist in the database
        $query    = "SELECT * FROM `users` WHERE username='$username'
                     AND password='" . md5($password) . "'";
        $result = mysqli_query($con, $query) or die(mysql_error());
        $rows = mysqli_num_rows($result);
        if ($rows == 1) {
            function function_alert($msg)
            {
                echo "<script type='text/javascript'>alert('$msg');</script>";
            }
            function_alert("You have logged in !");
            session_start();
            $_SESSION['username'] = $username;
            // Redirect to user dashboard page
            header("Location: home.php");

        } else {
            echo "<div class='form'>
                  <h3>Incorrect Username/password.</h3><br/>
                  <p class='link'>Click here to <a href='login.php'>Login</a> again.</p>
                  </div>";
        }
    } else {
    ?>
        <!-- header section starts  -->

        <section class="header">

            <a href="home.php" class="logo">travel.</a>

            <nav class="navbar">
                <a href="home.php">home</a>
                <a href="about.php">about</a>
                <a href="package.php">package</a>
                <a href="book.php">book</a>
                <a href="login.php">login</a>
                <a href="registration.php">register</a>
            </nav>

            <div id="menu-btn" class="fas fa-bars"></div>

        </section>

        <!-- header section ends -->

        <div class="heading" style="background:url(images/header-bg-3.png) no-repeat">
            <h1>login</h1>
        </div>

        <!-- booking section starts  -->

        <section class="login">

            <h1 class="heading-title">login to book your trip !</h1>

            <form action="login.php" method="post" class="login-form">

                <div class="flex">
                    <div class="inputBox">
                        <span>username :</span>
                        <input type="text" placeholder="enter your name" name="username">
                    </div>
                    <div class="inputBox">
                        <span>password :</span>
                        <input type="password" placeholder="enter your number" name="password">
                    </div>
                </div>

                <input type="submit" value="submit" class="btn" name="send">

            </form>
        </section>

        <!-- booking section ends -->

















        <!-- footer section starts  -->

        <section class="footer">

            <div class="box-container">

                <div class="box">
                    <h3>quick links</h3>
                    <a href="home.php"> <i class="fas fa-angle-right"></i> home</a>
                    <a href="about.php"> <i class="fas fa-angle-right"></i> about</a>
                    <a href="package.php"> <i class="fas fa-angle-right"></i> package</a>
                    <a href="book.php"> <i class="fas fa-angle-right"></i> book</a>
                </div>

                <div class="box">
                    <h3>extra links</h3>
                    <a href="#"> <i class="fas fa-angle-right"></i> ask questions</a>
                    <a href="#"> <i class="fas fa-angle-right"></i> about us</a>
                    <a href="#"> <i class="fas fa-angle-right"></i> privacy policy</a>
                    <a href="#"> <i class="fas fa-angle-right"></i> terms of use</a>
                </div>

                <div class="box">
                    <h3>contact info</h3>
                    <a href="#"> <i class="fas fa-phone"></i> +123-456-7890 </a>
                    <a href="#"> <i class="fas fa-phone"></i> +111-222-3333 </a>
                    <a href="#"> <i class="fas fa-envelope"></i> shaikhanas@gmail.com </a>
                    <a href="#"> <i class="fas fa-map"></i> mumbai, india - 400104 </a>
                </div>

                <div class="box">
                    <h3>follow us</h3>
                    <a href="#"> <i class="fab fa-facebook-f"></i> facebook </a>
                    <a href="#"> <i class="fab fa-twitter"></i> twitter </a>
                    <a href="#"> <i class="fab fa-instagram"></i> instagram </a>
                    <a href="#"> <i class="fab fa-linkedin"></i> linkedin </a>
                </div>

            </div>

            <div class="credit"> created by <span>mr. web designer</span> | all rights reserved! </div>

        </section>

        <!-- footer section ends -->









        <!-- swiper js link  -->
        <script src="https://unpkg.com/swiper@7/swiper-bundle.min.js"></script>

        <!-- custom js file link  -->
        <script src="js/script.js"></script>
    <?php
    }
    ?>
</body>

</html>