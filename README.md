Porazdeljeni števci (Distributed Counters)
==========================================

Opis projekta
-------------
Porazdeljeni števci so rešitev zemantinega programerskega izziva.

Rešitev problema temelji na replikaciji podatkovne baze MySQL, v kateri so shranjene informacije o števcih.
Za izvedbo replikacije je uporabljen Galera Cluster, na voljo pa je tudi enostavni spetni uporabniški vmesnik (django).


Namestitev in zagon clusterja
-----------------------------
Vse strežnike najprej povežemo v Galera CLuster. Na vsakem strežniku izvedemo naslednje ukaze:

    sudo apt-get update
    sudo apt-get install python-software-properties
    sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db
    sudo add-apt-repository 'deb http://mirror.jmu.edu/pub/mariadb/repo/5.5/ubuntu precise main'
    sudo apt-get update
    sudo apt-get install mariadb-galera-server galera
    sudo apt-get install rsync

Nato na vseh strežnikih ustvarimo konfiguracijsko datoteko /etc/mysql/conf.d/cluster.cnf:

    [mysqld]
    query_cache_size=0
    binlog_format=ROW
    default-storage-engine=innodb
    innodb_autoinc_lock_mode=2
    query_cache_type=0
    bind-address=0.0.0.0

    # Galera Provider Configuration
    wsrep_provider=/usr/lib/galera/libgalera_smm.so
    #wsrep_provider_options="gcache.size=32G"

    # Galera Cluster Configuration
    wsrep_cluster_name="test_cluster"
    wsrep_cluster_address="gcomm://1.1.1.1,2.2.2.2,3.3.3.3"

    # Galera Synchronization Congifuration
    wsrep_sst_method=rsync
    #wsrep_sst_auth=user:pass

    # Galera Node Configuration
    wsrep_node_address="1.1.1.1"
    wsrep_node_name="node1"


wsrep_cluster_address mora vsebovati naslove vseh strežnikov clusterja

wsrep_node_address in wsrep_node_name pa na vsakem strežniku vsebujeta naslov ter ime strežnika

Zgornji primer je konfiguracijska datotega strežnika na naslovu 1.1.1.1, ki je znotraj clusterja z strežniki: 1.1.1.1, 2.2.2.2 ter 3.3.3.3


Preden zaženemo cluster, je potrebno konfiguracijsko datoteko /etc/mysql/debian.cnf z enega izmed strežnikov kopirati na vse ostale.
Nato je potrebno na vseh strežnikih ustaviti mysql:

    sudo service mysql stop

Cluster nato zaženemo tako, da na enem izmed strežnikov najprej poženemo:

    sudo service mysql start --wsrep-new-cluster

Na vseh ostalih strežnikih pa zaženemo:

    sudo service mysql start


Podrobnejši opis namestitve se nahaja [tu](https://www.digitalocean.com/community/articles/how-to-configure-a-galera-cluster-with-mariadb-on-ubuntu-12-04-servers).

Namestitev in zagon aplikacije
------------------------------

Na vsak strežnik prenesemo vsebino tega repozitorija.

Namestimo potrebne pakete:

    sudo apt-get install python-pip
    sudo apt-get install python-mysqldb
    sudo pip install django

Pred prvim zagonom na enem izmed strežnikov ustvarimo podatkovno bazo in izvedemo syncdb:

    mysql -u root -psecret -e 'CREATE DATABASE playground;'
    python manage.py syncdb

Ter zaženemo strežnik:

    python manage.py runserver 0.0.0.0:8000

