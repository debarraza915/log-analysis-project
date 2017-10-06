# Log-Analysis

### Project Overview
>This project is part of the Udacity Full Stack Nanodegree program. In this project, you will get practice interacting with a live database both from the command line and from your code. You will explore a large database with over a million rows. And you will build and refine complex queries and use them to draw business conclusions from data.

### To Run

#### PreRequisites:
  * [Python3](https://www.python.org/)
  * [Vagrant](https://www.vagrantup.com/)
  * [VirtualBox](https://www.virtualbox.org/)

#### Setup Project:
  1. Install VirtualBox. [You can download it from virtualbox.org, here.](https://www.virtualbox.org/wiki/Downloads)
  2. Install Vagrant. [Download it from vagrantup.com](https://www.vagrantup.com/downloads.html)
  3. Download the VM configuration. You can download and unzip this file: [FSND-Virtual-Machine.zip](FSND-Virtual-Machine.zip)
  3. Next, [download the data here.](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) Unzip the file after downloading it. The file inside is called **newsdata.sql**. Put this file into the vagrant directory found inside the previously downloaded **FSND-Virtual-Machine** folder.
  5. Copy the content of this current repository, by either downloading or cloning it from
  [here](https://github.com/sagarchoudhary96/Log-Analysis)

#### Launching the Virtual Machine:
  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded **FSND-Virtual-Machine** repository using command:

  ```
    $ vagrant up
  ```
  2. Then Log into this using command:

  ```
    $ vagrant ssh
  ```
  3. Change directory to /vagrant and look around with ls.

#### Setting up the database and Creating Views:

  1. Load the data in local database using the command:

  ```
    psql -d news -f newsdata.sql
  ```
  The database includes three tables:
  * The authors table includes information about the authors of articles.
  * The articles table includes the articles themselves.
  * The log table includes one entry for each time a user has accessed the site.

  2. Use `psql -d news` to connect to database.



#### Running the queries:
  1. From the vagrant directory inside the virtual machine,run logs.py using:
  ```
    $ python3 logs.py
  ```
