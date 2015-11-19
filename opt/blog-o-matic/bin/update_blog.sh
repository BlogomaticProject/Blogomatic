# Updates a blog.
#
# Parameters:
#
#	- Shortname
#	- Search

EXPECTED_ARGS=2
E_BADARGS=65

if [ $# -ne $EXPECTED_ARGS ]
then
	echo "Error with arguments: $@"
	echo
	echo "Usage: `basename $0` [SHORTNAME] [SEARCH]"
	exit $E_BADARGS
fi

. /etc/blog-o-maticrc
. $BLOGOMATICPATH/etc/blog.conf

BLOG_NAME=$1	# XXX This sould not have spaces and must be unique.
BLOG_SEARCH=$2

# Perform search and update blog
cd $BLOGOMATICPATH/bin
./updater.py --search "$BLOG_SEARCH" --url "$BLOG_URL/$BLOG_NAME/xmlrpc.php" --urlshort "$BLOG_NAME" --admin "$BLOG_ADMIN" --password "$BLOG_PW" --limit 2000 --citation
