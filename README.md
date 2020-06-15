# flask-mongodb-autocompletion
A autocomplete setup using flask and mongoDB


If you are newbie i recommend you to go through the following steps.

**1. MongoDB download and installation **

Here i will show you how to install using home brew on macOS

# Installs Homebrew
*Installs Homebrew*
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

*Taps Homebrew*
brew tap mongodb/brew

*Installing MongoDB using Homebrew*
brew install mongodb-community

**2. MongoDB download and installation **

*Navigate to the volume using the command*
sudo mkdir -p /System/Volumes/Data/data/db

*Grant permission*
sudo chown -R `id -un` /System/Volumes/Data/data/db

**3. Checking MongoDB **

*start MongoDB*
brew services run mongodb-community

*Checking MongoDB - this will list all running services and  If MongoDB is running, mongodb-community will have a status set to started *
brew services list

*Enter MongoDB shell-this is where you write down the monogDB commands*
mongo

*this is to stop MongoDB*
brew services stop mongodb-community

To rush through basics of MongoDB , go through this link https://www.freecodecamp.org/news/learn-mongodb-a4ce205e7739/

**4.Installling Flask**

*if you have python already installed on your computer**
type out this command

pip install Flask

if not  downlaod python and do the step given above https://www.python.org/downloads/

**5.Importing .csv files on MongoDB**

CSV is the acronym for the comma-separated values file which allows saving the data in the table structured format.
1)Navigate to the folder where MongoDB is installed 
2)Further Navigated to bin in that folder
3)Paste the .csv file
4)Navigate to the bin folder 
5)Run the following command on your terminal(not on mongo shell

mongoimport -d myDB -c myCollection --type CSV --file data.csv --headerline

Note: 
myDB is the database name

myCollection is the collection name.

–type CSV denotes that file type that is being imported is of type CSV.

data.csv is the file name that we are importing.

–headerline is the header of the CSV file, below which listed data is mentioned (here in this example it is ‘word ‘).

*alter only the database name, collection name and file name you are importing*

Check if import was executed properly. Use the following commands. 

show databases
use <your_db_name>
db.myCollection.find().pretty() 
Note: use your db name instead of db and collection anme of myCollection

Meanwhile we will do some front end part

**6. Frontend**

*As we are usign flask let's create virtual environment*

Why do we need a virtual environment?
Imagine a scenario where you are working on two web based python projects and one of them uses a Django 1.9 and the other uses Django 1.10 and so on. In such situations virtual environment can be really useful to maintain dependencies of both the projects.

Use thi
pip install virtualenv

*Activating vitual environment*

Execute the following commands (foldername can be your folder name)
mkdir foldername
cd foldername
python3 -m venv env
source env/bin/activate

*Within that folder create a folder called templates*

this is where all your html files going to be there

*Paste the index.html file in your templates folder* 

**7. Backend **

*Come back to main folder and paste the main.py file *

additionally you need to install pymongo in your terminal so you can use mongodb with python

pip install pymongo

**8.Conslusion**

Run the python file using

python3 main.py runserver

Open http://127.0.0.1:5000/ in your browser .


**Note the project is still under development , might add few more features**

*Happy Coding !! *








