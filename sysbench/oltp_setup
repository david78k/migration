================= Setup OLTP ====================
Install MySQL
yum install mysql-server

set root password:
mysql
mysql> SET PASSWORD FOR 'root'@'localhost' = PASSWORD('newpwd');

Check if everything is ok:
mysql -u root -p'newpwd'
use mysql;
mysql> select Host,User,Password from user;

create a database called 'sbtest':
mysql> create database sbtest;

create a file called prepare:
sock=/var/lib/mysql/mysql.sock # centos
sock=/var/run/mysqld/mysqld.sock # debian
# prepare
sysbench --test=oltp --mysql-table-engine=myisam --oltp-table-size=1000000 \
        --mysql-socket=$sock \
        --db-driver=mysql \
        --mysql-user=root \
        --mysql-password=mysql \
        prepare

        #--mysql-db=test \

create a file called run:
sock=/var/lib/mysql/mysql.sock # centos
sock=/var/run/mysqld/mysqld.sock # debian
# run
sysbench --num-threads=`nproc` \
        --max-requests=100000 \
        --test=oltp \
        --mysql-socket=$sock \
        --oltp-table-size=1000000 \
        --oltp-read-only=on \
        --db-driver=mysql \
        --mysql-user=root \
        --mysql-password=mysql \
        run

================= Uninstalling mysql =================
To uninstall mysql server completely,
yum erase mysql mysql-server
rm -rf /var/lib/mysql

If you reinstall, you have to do restart mysqld to reset password:
service mysqld restart

=================== Results ====================
root@vm512-29:~# free
             total       used       free     shared    buffers     cached
Mem:           518        298        220          0          2        229

root@vm512-29:~# df
Filesystem            Size  Used Avail Use% Mounted on
/dev/sda1             913M  780M   87M  90% /
tmpfs                 260M     0  260M   0% /lib/init/rw
udev                  255M  100K  255M   1% /dev
tmpfs                 260M     0  260M   0% /dev/shm

================= Troubleshooting ==================
can't see 'mysql' database => reinstall mysql-server
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| test               |
+--------------------+
2 rows in set (0.00 sec)

FATAL: unable to connect to MySQL server, aborting...
FATAL: error 1049: Unknown database 'sbtest'
FATAL: failed to connect to database server!
=> create 
