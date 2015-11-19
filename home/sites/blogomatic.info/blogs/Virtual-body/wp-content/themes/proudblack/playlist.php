<?php 
session_start();
/*
Template Name: playlist
*/
// Include WordPress 
define('WP_USE_THEMES', false);
require_once('/home/sites/blog.melomics.com/htdocs/wp-load.php');

if ( isset ( $_SESSION['playlist'] ) ) {
 // Si existe
 query_posts($_SESSION['playlist']);
} 	

//echo "<pre>"; print_r($wp_query->query_vars); echo "</pre>";
if (have_posts()){ 
echo "<rss version='2.0' xmlns:jwplayer='http://developer.longtailvideo.com/trac/' xmlns:media='http://search.yahoo.com/mrss/'>\n"; 
echo "<channel>\n ";
echo    "\t<title>Melomics Videoblog</title>\n";  


	 while (have_posts()): the_post();
			 	$video=get_post_meta($post->ID,'video',true);
			 	$title= get_the_title($post->ID);//get_post_meta($post->ID,'title',true);
			 	$thumbnail = get_post_meta($post->ID,'thumbnail',true);
			 	$imgplaylist = get_post_meta($post->ID,'imgplaylist',true);
			  if (! empty($video)){
			 	    echo "\t<item>\n"; 
		      	echo "\t\t<title>".$title."</title>\n"; 
		      	echo "\t\t<media:content url=\"". $video."\" />\n"; 
		      	echo "\t\t<media:thumbnail url=\"".$thumbnail."\" />\n";
		        echo "\t\t<jwplayer:playlist.image>".$imgplaylist."</jwplayer:playlist.image>\n"; 
		    		echo "\t</item>\n";
				}					
	endwhile;
	
echo "</channel>\n";
echo "</rss>";
}
?>
