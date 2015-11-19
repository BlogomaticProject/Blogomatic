<div id="sidebar" class="grid_5">
<!--?php include(TEMPLATEPATH . '/sidebartab.php' ); ?--> 
<div id="sidebartop"></div>
<div id="sidebarmid" class="clearfix">
	<div class="widget inner widget_tag_cloud">
	<h2> </h2>
	<div id="nube">
		<?php //wp_tag_cloud('number=20&smallest=11&largest=15&format=flat&orderby=count');?>
		<?php wp_tag_cloud('number=20');?>
	</div>		
	<div id="nubebottom"></div-->	
	</div>		
   <?php if (function_exists('dynamic_sidebar') && dynamic_sidebar(1) ) : else : ?>	
            
            <?php endif; ?>        

</div> 

<div id="sidebarbottom"></div>
</div>
