<center> <h1>HBNB - The Console</h1> </center>

This repository contains the second stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.  This iteration of the HBNB project implements the use of a MySQL database.

---

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](https://github.com/chrisvanndy/AirBnB_clone_v2/blob/master/AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests](https://github.com/chrisvanndy/AirBnB_clone_v2/tree/master/tests) | All class-defining modules are unittested |
| 3. Make BaseModel | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a parent class to be inherited by all model classes, forked codebase version |
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/chrisvanndy/AirBnB_clone_v2/blob/master/models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation, updated by S. Brooks, C. Vanndy|
| 5. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/_ _init_ _.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/__init__.py) [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a class to manage persistent file storage system, forked codebase version.|
| 6. Console | [console.py](https://github.com/chrisvanndy/AirBnB_clone_v2/blob/master/console.py) | Updated console module from codebase with methods allowing user to create, destroy, show, and update data|
| 7. More Classes | [/models/user.py](https://github.com/chrisvanndy/AirBnB_clone_v2/blob/master/models/user.py) [/models/place.py](https://github.com/chrisvanndy/AirBnB_clone_v2/blob/master/models/place.py) [/models/city.py](https://github.com/chrisvanndy/AirBnB_clone_v2/blob/master/models/city.py) [/models/amenity.py](https://github.com/chrisvanndy/AirBnB_clone_v2/blob/master/models/amenity.py) [/models/state.py](https://github.com/chrisvanndy/AirBnB_clone_v2/blob/master/models/state.py) [/models/review.py](https://github.com/chrisvanndy/AirBnB_clone_v2/blob/master/models/review.py) | Dynamically implements more updated classes |
<br>
<br>
<center> <h2>General Use</h2> </center>
The programs init function determines wether file_storage or db_storage will be utilized based on user input. Either module determines how class objects are created, edited, and stored.  Class modules have been updated to handle db_storage. 

##### Supported Classes
    * BaseModel
    * User
    * State
    * City
    * Amenity
    * Place
    * Review

##### Commands
    * create - Creates an instance based on supplied class type

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects, or all objects of a given class if specified.

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)


##### Alternative Syntax
Users are not able to use the following alternative syntax:

	Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands: 

    * all - Shows all objects the program has access to, or all objects of a given class

	* count - Return number of object instances by class

    * show - Shows an object based on class and UUID

	* destroy - Destroys an object based on class and UUID

    * update - Updates existing attributes an object based on class name and UUID

<br>
<br>
<center> <h2>Examples</h2> </center>
<h3>Primary Command Syntax</h3>

#### **Example 0: Create an object**
Usage: create <class_name> in the following way.
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```
#### **Example 1: Show an object**
Usage: show <class_name> <id> to return str of an object.

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```
#### **Example 2: Destroy an object**
Usage: destroy <class_name> <id> destroys an object in following way.
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
```
#### **Example 3: Update an object**
Usage: updates <class_name> <id> in the following way.
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```
<h3>Updated Console Syntax</h3>

#### **Example 0: Show all User objects**
Usage: <class_name>.all() shows all instances of a class in the following way.
```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

#### **Example 1: Destroy a User**
Usage: <class_name>.destroy(<id>) destroys an instance of a class in the following way.
```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
[]
(hbnb)
```
#### **Example 2: Update User (by attribute)**
Usage: <class_name>.update(<id>, <attribute_name>, "<attribute_value>") updates a sigle attribute of an object in the following way.
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
#### **Example 3: Update User (by dictionary)**
Usage: <class_name>.update(<id>, <dictionary>) updates multiple attributes in the following way.
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Derke Breww', 'email': 'sendmail@gmail.com'})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Derke Breww', 'email': 'sendmail@gmail.com', 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
<br>

### **Authors**
Ezra Nobrega <ezra.nobrega@outlook.com> <codebase author>
Justin Majetich <justinmajetich@gmail.com> <codebase author>
Stratton Brooks <2494@holbertonschool.com>
Chris Vanndy <2736@holbertonschool.com>
