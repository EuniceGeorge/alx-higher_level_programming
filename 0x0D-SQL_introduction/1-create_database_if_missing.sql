-- script that creates the database hbtn_0c_0 in your MySQL server
DBNAME = "hbtn_0"
DBEXIST = $(mysql --batch --skip-column-names -e "SHOW DATABASES LIKE '"$DBNAME"';" | grep "$DBNAME" > /dev/null; echo "$?")
if [ $DBEXIST -eq 0 ];then
	CREATE DATABASE hbtn_0;
fi
