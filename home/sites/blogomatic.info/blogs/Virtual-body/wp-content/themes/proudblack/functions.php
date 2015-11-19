<?php

function getTinyUrl($url) {
	$tinyurl = file_get_contents("http://tinyurl.com/api-create.php?url=".$url);
	return $tinyurl;
}

function create_my_customfeed() {
	load_template( TEMPLATEPATH . 'myfeed.php'); // You'll create a your-custom-feed.php file in your theme's directory
}
add_action('do_feed_customfeed', 'create_my_customfeed', 10, 1); // Make sure to have 'do_feed_customfeed'

function custom_feed_rewrite($wp_rewrite) {
	$feed_rules = array('feed/(.+)' => 'index.php?feed=' . $wp_rewrite->preg_index(1),'(.+).xml' => 'index.php?feed='. $wp_rewrite->preg_index(1));
	$wp_rewrite->rules = $feed_rules + $wp_rewrite->rules;
}
add_filter('generate_rewrite_rules', 'custom_feed_rewrite');

function SearchFilter($query) {
if ($query->is_search) {
$query->set('post_type', 'post');
}
return $query;
}

add_filter('pre_get_posts','SearchFilter');

if ( function_exists('register_sidebar') )
    register_sidebars(1,array(
       'before_widget' => '<div class="widget inner %2$s">',
        'after_widget' => '</div><!--/widget-->',
        'before_title' => '<h2>',
        'after_title' => '</h2>',
    ));
	
include(TEMPLATEPATH . '/php/social.php' ); 	
// Custom Theme Options

$themename = "Proudblack";
$shortname = "pb";
$options = array (    
	array(	"name" => "Twitter ID",
			"desc" => "Enter twitter username : ",
			"id" => $shortname."_twit",
			"std" => "",
			"type" => "text"
	),
	array(	"name" => "Flickr ID",
			"desc" => "Enter Flickr username : ",
			"id" => $shortname."_flickr",
			"std" => "",
			"type" => "text"
	),
	array(	"name" => "Copyright Information",
			"desc" => "Enter the name of your company . This will appear in the copyright area(footer)",
			"id" => $shortname."_copyright",
			"std" => "",
			"type" => "text"
	),
);

function mytheme_add_admin() {

    global $themename, $shortname, $options;

    if ( $_GET['page'] == basename(__FILE__) ) {
    
        if ( 'save' == $_REQUEST['action'] ) {

                foreach ($options as $value) {
                    update_option( $value['id'], $_REQUEST[ $value['id'] ] ); }

                foreach ($options as $value) {
                    if( isset( $_REQUEST[ $value['id'] ] ) ) { update_option( $value['id'], $_REQUEST[ $value['id'] ]  ); } else { delete_option( $value['id'] ); } }

                header("Location: themes.php?page=functions.php&saved=true");
                die;

        } else if( 'reset' == $_REQUEST['action'] ) {

            foreach ($options as $value) {
                delete_option( $value['id'] ); }

            header("Location: themes.php?page=functions.php&reset=true");
            die;

        }
    }

    add_theme_page($themename." Options", "Proudblack Options", 'edit_themes', basename(__FILE__), 'mytheme_admin');

}

function mytheme_admin() {

    global $themename, $shortname, $options;

    if ( $_REQUEST['saved'] ) echo '<div id="message" class="updated fade"><p><strong>'.$themename.' options saved.</strong></p></div>';
    if ( $_REQUEST['reset'] ) echo '<div id="message" class="updated fade"><p><strong>'.$themename.' options reset.</strong></p></div>';
    
?>
<div class="wrap">
<h2><?php echo $themename; ?> Settings</h2>

<form method="post">
<br/>
<table class="optiontable">

<?php foreach ($options as $value) { 
    
if ($value['type'] == "text") { ?>
        
<tr valign="top"> 
    <th scope="row"><?php echo $value['name']; ?>:</th>
    <td>
        <input name="<?php echo $value['id']; ?>" id="<?php echo $value['id']; ?>" type="<?php echo $value['type']; ?>" value="<?php if ( get_settings( $value['id'] ) != "") { echo get_settings( $value['id'] ); } else { echo $value['std']; } ?>" />
    </td>
</tr>

<?php } elseif ($value['type'] == "select") { ?>

    <tr valign="top"> 
        <th scope="row"><?php echo $value['name']; ?>:</th>
        <td>
            <select name="<?php echo $value['id']; ?>" id="<?php echo $value['id']; ?>">
                <?php foreach ($value['options'] as $option) { ?>
                <option<?php if ( get_settings( $value['id'] ) == $option) { echo ' selected="selected"'; } elseif ($option == $value['std']) { echo ' selected="selected"'; } ?>><?php echo $option; ?></option>
                <?php } ?>
            </select>
        </td>
    </tr>

<?php 
} 
}
?>

</table>

<p class="submit">
<input name="save" type="submit" value="Save changes" />    
<input type="hidden" name="action" value="save" />
</p>
</form>
<form method="post">
<p class="submit">
<input name="reset" type="submit" value="Reset" />
<input type="hidden" name="action" value="reset" />
</p>
</form>



<?php
}

function mytheme_wp_head() { ?>

<?php }
add_action('wp_head', 'mytheme_wp_head');
add_action('admin_menu', 'mytheme_add_admin');

?>