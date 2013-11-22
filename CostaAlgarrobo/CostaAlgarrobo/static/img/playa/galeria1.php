<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title>Costa Algarrobo - Inicio</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width">

        <link rel="stylesheet" href="css/bootstrap.min.css">
        <link rel="stylesheet" href="css/bootstrap-theme.min.css">
        <link rel="stylesheet" href="css/main.css">
	<link rel="stylesheet" href="css/galeria.css">
	<link rel="stylesheet" href="css/galeria1.css">

        <script src="js/vendor/modernizr-2.6.2-respond-1.1.0.min.js"></script>
    </head><!-- Fin Head -->
    <body onload="$('#carruselFondo').carousel()">
    
        <!--[if lt IE 7]>
            <p class="chromeframe">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">activate Google Chrome Frame</a> to improve your experience.</p>
        <![endif]-->
        <div>
        	<?php 

        		include 'header.php';

        	?><!-- Fin Header -->
			
        	<div id="carruselFondo" class="carousel slide">
        		<div class="carousel-inner">
               			<div id="slider1" class="item active" style="background-image: url(img/playa/9.jpg);">
        			</div>
				<div id="slider2" class="item" style="background-image: url(img/playa/1.jpg);">
        			</div>
				<div id="slider3" class="item" style="background-image: url(img/playa/2.jpg);">
        			</div>
				<div id="slider4" class="item" style="background-image: url(img/playa/3.jpg);">
        			</div>
				<div id="slider5" class="item" style="background-image: url(img/playa/4.jpg);">
        			</div>
				<div id="slider6" class="item" style="background-image: url(img/playa/5.jpg);">
        			</div>
				<div id="slider7" class="item" style="background-image: url(img/playa/6.jpg);">
        			</div>
				<div id="slider8" class="item" style="background-image: url(img/playa/7.jpg);">
        			</div>
				<div id="slider9" class="item" style="background-image: url(img/playa/8.jpg);">
        			</div>
        		</div>
        	</div><!-- Fin Carrusel -->

        	<?php 

        		include 'menu.php';

        	?>
		
			<div id="content">
    		    <section class="main container">
    		    </section><!-- Fin Main -->
            </div><!-- Fin Content -->


		    <div id="footerDesplegable">
			   <div class="botonDesplegable">
				<div class="menuDesplegable">
					<div class="menuizq">EDIFICIOS</div>
					<div class="menuizq1">BOSQUE</div>
					<div class="menuizq2 seleccionado">PLAYA</div>
				   	<img src="img/up.png" class="upDesplegable">
					<div class="menuder2">PILOTOS</div>
					<div class="menuder1">RECREACIÓN</div>
					<div class="menuder">OTRAS</div>
				</div>
			   </div>
			   <div class="desplegable">
			   	<div id="contentDesplegable">
    		    <section class="main container">
    		    	<div class="desplegableContent">
    		    	
			<div class="scrolls bosque encendido">
				<div class="imageDiv">
					<ol class="carousel-indicators">
						<li data-target="#carruselFondo" data-slide-to="8" class="fotoGaleria active" style="background-image: url(img/playa/9.jpg);"></li>
						<li data-target="#carruselFondo" data-slide-to="0" class="fotoGaleria" style="background-image: url(img/playa/1.jpg);"></li>
						<li data-target="#carruselFondo" data-slide-to="1" class="fotoGaleria" style="background-image: url(img/playa/2.jpg);"></li>
						<li data-target="#carruselFondo" data-slide-to="2" class="fotoGaleria" style="background-image: url(img/playa/3.jpg);"></li>
						<li data-target="#carruselFondo" data-slide-to="3" class="fotoGaleria" style="background-image: url(img/playa/4.jpg);"></li>
						<li data-target="#carruselFondo" data-slide-to="4" class="fotoGaleria" style="background-image: url(img/playa/5.jpg);"></li>
						<li data-target="#carruselFondo" data-slide-to="5" class="fotoGaleria" style="background-image: url(img/playa/6.jpg);"></li>
						<li data-target="#carruselFondo" data-slide-to="6" class="fotoGaleria" style="background-image: url(img/playa/7.jpg);"></li>
						<li data-target="#carruselFondo" data-slide-to="7" class="fotoGaleria" style="background-image: url(img/playa/8.jpg);"></li>
					</ol>

				</div>
			</div>



    		    	</div>
    		    </section><!-- Fin Main -->
            </div><!-- Fin Content -->
			   </div>
			   <div class="baseDesplegable">
			   </div>

			</div><!-- Fin Content -->


		</div><!-- Fin Wrapper -->
		<?php 

        	include 'footer.php';

        ?>

	<!-- Fin Footer -->
	    

	    <!-- Scripts para cargas finales -->
		<!--<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js"></script>
	    <script>window.jQuery || document.write('<script src="js/vendor/jquery-1.10.1.min.js"><\/script>')</script>-->
	    <script src="js/vendor/jquery-1.10.1.min.js"></script>
	    <script src="js/vendor/bootstrap.min.js"></script>
	    <script src="js/main.js"></script>
		<script> 
		  $(document).ready(function(){
		    $(".upDesplegable").click(function(){
		      if($(".baseDesplegable").hasClass('click')) {
		        $(".baseDesplegable").animate({height:0},200).removeClass('click');
		      } else { 
		        $(".baseDesplegable").animate({height:77},200);
		        $(".baseDesplegable").addClass('click');
		      }
		    });
		    $(".menuizq2").click(function(){
			      if($(".baseDesplegable").hasClass('click')) {
				$(".baseDesplegable").animate({height:0},200).removeClass('click');
			      } else { 
				$(".baseDesplegable").animate({height:77},200);
				$(".baseDesplegable").addClass('click');
			      }
		    });
		  });
		</script>
	    <!--<script>
	        var _gaq=[['_setAccount','UA-XXXXX-X'],['_trackPageview']];
	        (function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];
	        g.src='//www.google-analytics.com/ga.js';
	        s.parentNode.insertBefore(g,s)}(document,'script'));
	    </script>-->
    </body><!-- Fin Body -->
</html><!-- Fin Pagina -->
