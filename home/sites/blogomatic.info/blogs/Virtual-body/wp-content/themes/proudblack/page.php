<?php get_header(); ?>
<div id="content" class="fullspan">

 	<div class="container_16">
		<div id="main" class="grid_11">
    		<div id="main-top"></div>
        <div id="main-area" class="clearfix">
            	<?php while (have_posts()) : the_post(); ?>	
							<div class="post">
									<h2 class="page-title"><?php the_title(); ?></h2>
			            <div class="entry"><?php the_content(); ?></div>
							</div>
            	<?php endwhile; ?>
            </div>
         <div id="main-bottom"></div>
            
		</div>
    <?php get_sidebar(); ?>
	</div>

</div>
<div class="clearfix"></div>
<?php get_footer(); ?>