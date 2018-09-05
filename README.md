# notes-n-things

notes-n-things is the group Software Development project for Group 6

[insert super awesome description here]

Production Server: www.notes-n-things.tk<br  />
Dev Server 1: dev1.notes-n-things.tk<br />
Dev Server 2: dev2.notes-n-things.tk<br />
Dev Server 3: dev3.notes-n-things.tk Testing server<br />
Dev Server 4: dev4.notes-n-things.tk<br />
Dev Server 5: dev5.notes-n-things.tk<br />

## Running Frank Tests

###Getting the most recent build for frank
<pre><code>
  Starting in notes-n-things git repo
  $cd iosApp/notes-n-things
  $frank build
</code></pre>

###Starting and running the tests
<pre><code>
  Starting in notes-n-things git repo
  $cd iosApp/notes-n-things/Frank
  $cucumber
  when the iOS simulator opens it needs to have the hardware switched to iPad
  select the iOS simulator and go to the Hardware menu then Devices then select iPad
  then once the new simulator loads find app named Frankify and start
  this needs to be done for every feature file
</code></pre>

###Notes about failing tests

Some tests have a chance to fail if the app fails to grab data from the server this can happen in login.feature or navaigation.feature
If this happens for one of the features it is easier to change what cucumber runs to just that file
<pre><code>
  change
  $cucumber
  to
  $cucumber features/*.feature
  where * is navigation or login depending on which had a fail
</code></pre>

## Running Selenium Tests

Selenium tests should be run on a clean database (that is with no entries other than a user with id of 1 named guest, and a course with an id of 1 named COMP 1010).

To avoid messing up the database, run CreateUserCheckIfShowsUpInUserTab first.

Selenium Tests should be run on slow mode.

## Running QUnit Tests

Visit the /tests.html path on the production server or on the testing server.

## Running Server Side Tests

Run app_tests.py using the Python from the Notes 'N Things environment's bin.

## Server Maintenance

###Adding python modules
<pre><code>
  $cd /opt/apps/notes-n-things-env
  $source bin/activate
  $pip install [python module]
  $deactivate
</code></pre>

###Resarting Web Server
<pre><code>
  # killall -9 uwsgi
  # service nginx restart
  # uwsgi /opt/apps/notes-n-things-env/notes-n-things/config/uwsgi-settings.ini
</code></pre>

## Server set up
This part of the readme is for reference on how to properly set up the environment. Once the environment is finalized this information will not be strictly necessary and will function more for back up purposes (ie. if we lose the server image or something). For proper setup use the server image to create the server instace.

Server image: ami-ba83e08a<br />
[User and keypair stuff here]

Get an instance:
Obviously before the server set up can happen, you a server instance. This is the relevant section from Alex Korn's setup tutorial: http://www.alexkorn.com/blog/2011/03/getting-php-mysql-running-amazon-ec2/

>Once you’ve gotten that set up, go to the AWS Management Console, and click on “Instances” in the Navigation panel. An >Instance is just a virtual server – so let’s create one! Click “Launch Instance” under “My Instances”, and select >“Basic 64-bit Amazon Linux AMI”. On the Instance Details phase, select “Micro” (which is Free tier eligible). Continue >until you need to enter the “Name” – if you don’t know what else to call it, just use “Web/DB server”.
>
>Next you create a Key Pair – this will be the credentials you’ll use to SSH into the box. The instructions here should >be fairly straightforward. Next is the Security Group, which will be used to specify the firewall used for your >instance. Feel free to use the default Group for now. Continue to the Review phase and launch it!
>
>You should now be able to SSH into your instance using your .pem file with ssh -i [FILE NAME].pem ec2-user@ec2-[IP >ADDRESS].compute-1.amazonaws.com. Alright, we’ve got a server up and running! However, you may notice that this server >has very little installed on it."

One 

##Setup Software:
This section will probably change substantially over the next day or two as the exact environment is finalized.

###Notes on syntax

<pre><code>
# implies the command should be run as root, this usually means via sudo.
  The one exception to this is editing the postgres conf file, which must be done as root as 
  for security reasons no users except root can even read those directories. 
  (to switch to root run $sudo su)

$ implies the command is run as the current user

postgres# means the command is run from within the postgres rdbms
</code></pre>

###postgres sql

<pre><code>
  #apt-get install postgresql postgresql-contrib
  #su postgres
  $createdb notes_n_things
  $psql notes_n_things &lt; /opt/apps/notes-n-things-env/notes-n-things/config/schemapostgres.sql
  $exit
</code></pre>

<pre><code>
  To set up test database:
  #su postgres
  $psql
  postgres=# CREATE DATABASE notes_n_things_testdb WITH TEMPLATE notes_n_things OWNER postgres;
  postgres=# \q
  $exit
</code></pre>

###SqlALchemy

<pre><code>
  sudo apt-get install libpq-dev
  . /opt/apps/notes-n-things-env/bin/activate
  pip install flask-sqlalchemy
  pip install psycopg2
  deactivate

  restart postgresql server
</code></pre>

###git
<pre><code>
   #yum install git
</code></pre>

###Python, Flask and plugins
<pre><code>
   #apt-get install gcc python-setuptools python-pip python-devel
   #easy_install virtualenv
   #mkdir /opt/apps
   #chown ubuntu:ubuntu /opt/apps
   $ cd /opt/apps
   $ virtualenv --no-site-packages notes-n-things-env
   $ cd notes-n-things-env
   $ source bin/activate
   (notes-n-things-env)$ pip install flask
   (notes-n-things-env)$ git clone git://github.com/jasonpharder/notes-n-things
   (notes-n-things-env)$ deactivate
</code></pre>

###uWSGI and upstart
<pre><code>
  #pip install uwsgi
  #vim /etc/init/uwsgi.conf
</code></pre>
Paste the following into the the file
<pre><code>
# simple uWSGI script

description "uwsgi tiny instance"
start on runlevel [2345]
stop on runlevel [06]

exec uwsgi /opt/apps/notes-n-things-env/notes-n-things/config/uwsgi-settings.ini
</code></pre>

###nginx
<pre><code>
   #apt-get install nginx
   #vim /etc/nginx/sites-available/default
</pre></code>
Delete the contents of the file and make them:
<pre><code>
  server {
        listen 80 default_server;

        root /opt/apps/notes-n-things-env/notes-n-things;
        index index.html index.htm;

        location / { try_files /public/$uri @notes; }

        location @notes {
                uwsgi_pass     127.0.0.1:49152;
                include        uwsgi_params;
        }
}
</pre></code>
finnish by running
<pre><code>
   #uwsgi /opt/apps/notes-n-things-env/notes-n-things/uwsgi-settings.ini
   #service nginx start
</code></pre>

###updating instance security rules
<pre><code>
   <a href="http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Internet_Gateway.html#Add_IG_Security_Groups">Updating the Security Group Rules | AWS Documentation</a>
</code></pre>
