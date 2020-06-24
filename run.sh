#Author: Guilherme Santos
#Github: https://github.com/eguidos
#LinkedIn Profile: https://www.linkedin.com/in/guilherme-santos-754864108/


BASEFILE=$(pwd)
SPARK_SUBMIT=/usr/local/spark/spark-3.0.0-bin-hadoop2.7/bin/spark-submit
MYSQL=$BASEFILE/mysql
APP=$BASEFILE/main

#This loop goes through every SQL file and executes its infrastrucure.

for file in $MYSQL/*.sql
do
  echo "Executing $file"
  mysql -h "localhost" -u "root" "-padmin" < $file
done

#The following command sets up python packages
export PYTHONPATH=:${PYTHONPATH}:${pwd}
sudo -H python3 -m pip install -r requirements.txt

#So that, Spark execution collect all data needed, and then inserts into OLIST database tables.
$SPARK_SUBMIT $APP/app.py >> log.txt
