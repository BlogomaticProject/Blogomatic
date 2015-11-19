# Creates a new blog.
#
# Parameters:
#	- Title
#	- Shortname
#	- Search

EXPECTED_ARGS=3
E_BADARGS=65

if [ $# -ne $EXPECTED_ARGS ]
then
	echo "Error with arguments: $@"
	echo
	echo "Usage: `basename $0` [TITLE] [SHORTNAME] [SEARCH]"
	exit $E_BADARGS
fi

. /etc/blog-o-maticrc
. $BLOGOMATICPATH/etc/blog.conf

BLOG_TITLE=$1
BLOG_NAME=$2	# XXX This sould not have spaces and must be unique.
BLOG_SEARCH=$3

BLOG_ID=`cat $BLOG_COUNTER`
echo "$(($BLOG_ID+1))" > $BLOG_COUNTER

cd $BLOG_DIR

# Uncompress blog template
tar zxfv $BLOG_SOURCE
mv wordpress $BLOG_NAME

cd $BLOG_NAME

# Change configuration file
sed "s/database_name_here/$DB_NAME/g;s/username_here/$DB_USER/g;s/password_here/$DB_PW/g;s/wp_/$BLOG_PREFIX$BLOG_ID\_/g" wp-config-sample.php > wp-config.php

# Enable XML-RPC # XXX Modify this directly in the $BLOG_SOURCE file
mv wp-admin/includes/schema.php wp-admin/includes/schema.php.tmp
sed "s/'enable_xmlrpc' => 0,/'enable_xmlrpc' => 1,/g" wp-admin/includes/schema.php.tmp > wp-admin/includes/schema.php

# Create database calling WordPress installation script
wget -q --post-data "weblog_title=$BLOG_TITLE&user_name=$BLOG_ADMIN&admin_password=$BLOG_PW&admin_password2=$BLOG_PW&admin_email=$BLOG_EMAIL" $BLOG_URL/$BLOG_NAME/wp-admin/install.php?step=2

# Perform search and update blog
cd $BLOGOMATICPATH/bin
./updater.py --search "$BLOG_SEARCH" --url "$BLOG_URL/$BLOG_NAME/xmlrpc.php" --urlshort "$BLOG_NAME" --admin "$BLOG_ADMIN" --password "$BLOG_PW" --limit 2000 --citation
