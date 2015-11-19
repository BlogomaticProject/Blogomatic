<?php get_header(); ?>
<div id="content" class="fullspan">

 	<div class="container_16">
		<div id="main" class="grid_11">
    		<div id="main-top"></div>
        <div id="main-area" class="clearfix">
        	<?php while (have_posts()) : the_post(); ?>	
					<div class="post">
							<h2 class="post-title"><a title="<?php the_title(); ?>" href="<?php the_permalink() ?>" rel="bookmark"><?php the_title(); ?></a></h2>
	            <div class="post-meta-top"><!--div class="post-date"><?php the_time('l, jS F Y'); ?></div--></div>
							<div class="post-category"><?php //the_category(' '); ?></div>	
	            <div class="entry">
	            		<?php $video=get_post_meta($post->ID,'video',true);
	            		if (! empty($video)){ ?>
	            			<div id="video">
	            				
	            				<p><embed src="wp-content/uploads/player.swf" width="560" height="345" bgcolor="#" allowscriptaccess="always" allowfullscreen="true" flashvars="file=<?php echo $video ?>&skin=http://www.youtubereloaded.com/embed/skin1.swf"/></p></div><div id="empty"></div><?php }?>
	            		     		
	            		<?php the_content(); ?>
	            		
	            		<?php $citation=get_post_meta($post->ID,'citation',true);
	            		if (! empty($citation)) {?><div id="citation"><?php echo $citation ?></div><div id="empty"></div><?php }?>
	            		
	            		<?php /*$turl = getTinyUrl(get_permalink($post->ID));
										echo 'TinyURL for this post: <a href="'.$turl.'">'.$turl.'</a><br>'; */?>
										
	            		<?php if( function_exists('ADDTOANY_SHARE_SAVE_KIT') ) { ADDTOANY_SHARE_SAVE_KIT(); } ?></div>
	            <div class="post-meta"><?php the_tags('<p>',' ','</p>'); ?></div>
	            
				  </div>
       		<?php comments_template(); ?>
        	<?php endwhile; ?>
        </div>
      	<div id="main-bottom"></div>
        
		</div>
		<?php get_sidebar(); ?>
	</div>
</div>
<div class="clearfix"></div>
<?php get_footer(); ?>