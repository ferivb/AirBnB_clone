# **0x00. AirBnB clone - The console**

![AirBnB clone](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220307%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220307T002914Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d39deb11964eb13976fae69d991b5811c6361b45a652db8484664bc5775532fa)

## Table of content

- [Description of the project](description-of-the-project)
- [Command interpreter](command-interpreter)
- [Installation](installation)
- [Usage](usage)
- [Commands](commands)
- [Classes](classes)
- [Authors](authours)

## **Description of the project**

This project is the first step towards building our first full web application: the AirBNB clone. In the AirBNB clone: the console, we put in place a parent class (BaseModel) to take care of the initialization, serialization and deserialization of future instances. We also implement classes used in AirBNB (User, State, City, Place, Review) that inherits from BaseModel.

To handle the storage of the new instances created, we developed an abstract storage engine called: FileStorage. 

To create new instances, show the instances already created, destroy instances and update current instances, we use the console itsel, wich is a command interpreter implemented using the cmd module, that allow us to manage the objects created in the project.

## **Command interpreter: the console**

### **How to start it**
To start the coomand interpreter to should execute the console.py typing ./console.py. 

After you execute the console.py program the prompt (hbnb) will pop up.

## **Installation**

Use git to clone this repository in your local machine (ssh)

```
git clone git@github.com:ferivb/AirBnB_clone.git
```
or for https

```
https://github.com/ferivb/AirBnB_clone.git
```
## **Usage**

- All the scripts are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- You can run the command line interpreter typing ./console.py
- The console can be executed in interactive mode this way:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## **Commands**

The commands implemented in the console are

| Command | Description            | Example     |
|-----    | --------               |----         |
| quit    | Exit the console       | quit        |
| EOF     | Exit the console       | CRL+D       |
| help    | Description of command | help EOF    | 
| create  | Creates a new instance | create BaseModel |
| show    | Prints the Prints the string representation of an instance based on the class name and id | show BaseModel 1234-1234-1234|
| destroy |  Deletes an instance based on the class name and id  (save the change into the JSON file) | destroy BaseModel 1234-1234-1234 |
| all | Prints all string representation of all instances based or not on the class name | all BaseModel or all |
| update |  Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) | update BaseModel 1234-1234-1234 email "aibnb@mail.com" | 

## **Classes**

All the following classes inherits from BaseModel

| Class name    | Description     |
| ------------- | --------------  |
| User | Set the class attributes: email, password, first_name and last_name |
| State | Set the class attribute: name |
| City | Set the class attributes: state_id and name |
| Amenity | Set the class attribute: name |
| Place | Set the class attributes: city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids |
| Review | set the class attributes: place_id, user_id and text |


## **Example**

Here's some examples about how to use the console commands.

**create**
```
./console.py
(hbnb) create User
e43a9e75-188b-45ea-8700-2c90a5fce979
```

**show**
```
show User e43a9e75-188b-45ea-8700-2c90a5fce979
[User] (e43a9e75-188b-45ea-8700-2c90a5fce979) {'id': 'e43a9e75-188b-45ea-8700-2c90a5fce979', 'created_at': datetime.datetime(2022, 3, 6, 22, 23, 12, 594988), 'updated_at': datetime.datetime(2022, 3, 6, 22, 23, 12, 595987)}
```
**all**
```
all
["[User] (e43a9e75-188b-45ea-8700-2c90a5fce979) {'id': 'e43a9e75-188b-45ea-8700-2c90a5fce979', 'created_at': datetime.datetime(2022, 3, 6, 22, 23, 12, 594988), 'updated_at': datetime.datetime(2022, 3, 6, 22, 23, 12, 595987)}"]
```

**all Class**
```
all User
["[User] (e43a9e75-188b-45ea-8700-2c90a5fce979) {'id': 'e43a9e75-188b-45ea-8700-2c90a5fce979', 'created_at': datetime.datetime(2022, 3, 6, 22, 23, 12, 594988), 'updated_at': datetime.datetime(2022, 3, 6, 22, 23, 12, 595987)}"]
```

**destroy**
```
destroy User e43a9e75-188b-45ea-8700-2c90a5fce979
(hbnb) show User e43a9e75-188b-45ea-8700-2c90a5fce979
** no instance found **
```

## **Authors**
- Felipe Rivas <fe.rivasb@gmail.com>
- Sergio Balcazar <3896@holbertonschool.com>
