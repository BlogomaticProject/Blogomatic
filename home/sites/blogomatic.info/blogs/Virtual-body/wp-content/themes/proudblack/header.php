<?php 
session_start();
wp_head(); 

?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" <?php language_attributes(); ?>>

<head profile="http://gmpg.org/xfn/11">
<meta http-equiv="Content-Type" content="<?php bloginfo('html_type'); ?>; charset=<?php bloginfo('charset'); ?>" />

<title><?php bloginfo('name'); ?> <?php if ( is_single() ) { ?> &raquo; Blog Archive <?php } ?> <?php wp_title(); ?></title>

<meta name="generator" content="WordPress <?php bloginfo('version'); ?>" /> <!-- leave this for stats -->

	<link rel="stylesheet" type="text/css" href="<?php bloginfo('template_url'); ?>/css/dummy.css" id="dummy_css"  />
    <link rel="stylesheet" type="text/css" media="all" href="<?php bloginfo('template_directory'); ?>/css/reset.css" />
	<link rel="stylesheet" type="text/css" media="all" href="<?php bloginfo('template_directory'); ?>/css/text.css" />
	<link rel="stylesheet" type="text/css" media="all" href="<?php bloginfo('template_directory'); ?>/css/960.css" />
	<link rel="stylesheet" type="text/css" media="all" href="<?php bloginfo('template_directory'); ?>/style.css" />
	<link rel="alternate" type="application/rss+xml" title="RSS 2.0" href="<?php bloginfo('rss2_url'); ?>" />
  <link rel="alternate" type="text/xml" title="RSS .92" href="<?php bloginfo('rss_url'); ?>" />
	<link rel="alternate" type="application/atom+xml" title="Atom 0.3" href="<?php bloginfo('atom_url'); ?>" />

	<link rel="pingback" href="<?php bloginfo('pingback_url'); ?>" />
  
  <script type="text/javascript" src="<?php bloginfo('template_url'); ?>/js/applesearch.js"></script>
  <script type="text/javascript" src="<?php bloginfo('template_url'); ?>/js/mootools.v1.11.js"></script>
	<script type="text/javascript" src="<?php bloginfo('template_url'); ?>/js/sliding-tabs.js"></script>
	<script type="text/javascript" src="<?php bloginfo('template_url'); ?>/js/boxover.js"></script>
  <script type="text/javascript" src="<?php bloginfo('template_url'); ?>/js/sf.js"></script>
  <script type='text/javascript' src='wp-content/uploads/jwplayer.js'></script>
	<script type="text/javascript">
	//<![CDATA[
		window.onload = function () { applesearch.init(); }
	//]]>
	</script>
    

</head>

<body>
<div id="wrapper">
	<div id="header" class="fullspan">
    <div class="container_16">
    	<div class="grid_16" id="topmenu">
       		 <ul>							
				<li <?php if(is_home()) { echo 'class="current_page_item"';} ?>>
            		<!--a href="<?php bloginfo('siteurl'); ?>">Home</a-->
            	</li>
            	<!--?php wp_list_pages('title_li=&depth=3&exclude=21070911' ); ?-->			
        	</ul>
       </div>
       <div class="grid_12" id="logo">
       		<a href="<?php echo get_option('home'); ?>/"><img src="http://blog.melomics.com/wp-content/themes/proudblack/images/melomics-blog-logo.png"></a>
       </div>
       <div class="grid_4" id="search">
       	<!--?php jsearch_gbox(150,20); ?-->
       	<?php include (TEMPLATEPATH . '/searchform.php'); ?>
       </div>
       <!--div class="grid_4" id="rss">
       	<a href="<?php bloginfo('rss2_url'); ?>"><img src="http://pruebas.melomics.com/wp-content/themes/proudblack/images/rss.gif">
       </div-->
       <!--div class="grid_4" id="search">
       		<span id="jsearch_adv"><a id="jsearch_adv" href="http://pruebas.melomics.com/?page_id=21070911">Advanced search</a></span>
       </div-->	
   </div>
   </div>
