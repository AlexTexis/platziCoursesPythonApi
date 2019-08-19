# Solution challenge platzi

1. pip install requirements.txt

2. config env file

3. source env1/Scripts/activate and run flask run or py -m flask run

# API Documentation

## Url base :
https://flask-platz.herokuapp.com

## COURSES

### Methods GET

**GET COURSES**
> url_base/courses

Return Array of Courses:
```
{"data":[{
"_id":"5d537a7ab572f22f804dee52",
"name":"React",
"tutor":"midudev",
"description":"Curso basico de react",
"level":"Basico","alumns":[],
"class":[]},
...more
]}
```
**GET COURSE**

> url_base/courses/idCourse

Return Object of course : 

```
{
"data":{
"_id":"5d537a7ab572f22f804dee52",
"name":"React",
"tutor":"midudev",
"description":"Curso basico de react",
"level":"Basico","alumns":[],
"class":[]
}
```

### Methods POST

**Create new Course**

> url_base/courses

Send in Request Body Object :
```
{
    "name": "react",
    "tutor": "juan",
    "description": "react",
    "level": "Basico",
    "class": [],
    "alumns": []
}
```
Example with fetch Api
```
fetch(url,{
    method : 'POST',
    headers : new Headers({
        'Content-Type':'application/json'
    }),
    body : JSON.stringify(DATA)
})
```


Return object course created

```
{
    "data": {
        "name": "react",
        "tutor": "juan",
        "description": "react",
        "level": "Basico",
        "class": [],
        "alumns": [],
        "_id": "5d51abea4a9a84161c79b12b"
    }
}

```

**Add student**

> url_base/courses/idCourse/students

Send in Request Body Object :

```
{
	"_id" : "idStudent : string"
}
```

Example with fetch Api
```
fetch(url,{
    method : 'POST',
    headers : new Headers({
        'Content-Type':'application/json'
    }),
    body : JSON.stringify(DATA)
})
```

Return object student added

```
{
    "data": {
        "_id": "5d51acd5e31400282cc42221", // ID COURSE REFERENCE
        "saved": {
            "_id": "5d50c36e3b28be08f49f6ad9",
            "name": "Alex",
            "surnames": "Garrixen"
        }
    }
}
```

**Add class**

> url_base/courses/idCourse/class

Send in Request Body Object :

```
{
	"_id" : "idClass : string"
}
```

Example with fetch Api
```
fetch(url,{
    method : 'POST',
    headers : new Headers({
        'Content-Type':'application/json'
    }),
    body : JSON.stringify(DATA)
})
```

Return object class added

```
{
    "data": {
        "_id": "5d51acd5e31400282cc42221", // ID COURSE REFERENCE
        "saved": {
            "_id": "5d510458fa98a32f703622e3",
            "name": "subscriptios",
            "label": "graphql"
        }
    }
}
```

### Methods PUT

**Update course**

> url_base/courses/idCourse

Send in Request Body Object :


```
// You will send the fields you want to update

{
     "name": "React Basico",
     "tutor": "Leonidas",
}
```

Example with fetch Api
```
fetch(url,{
    method : 'PUT',
    headers : new Headers({
        'Content-Type':'application/json'
    }),
    body : JSON.stringify(DATA)
})
```

Return object course updated

```
{
    "data": {
        "_id": "5d51abea4a9a84161c79b12b",
        "name": "React Basico",
        "tutor": "Leonidas",
        "description": "react",
        "level": "Basico",
        "class": [],
        "alumns": []
    }
}
```

### Methods DELETE

**Delete course**


> url_base/courses/idCourse

Return object course removed

```
{
    "data": {
        "courseRemoved": "5d51abea4a9a84161c79b12b"
    }
}

```

**Delete student**

> url_base/courses/idCourse/students/idStudent

Return object student removed

```
{
    "data": {
        "_id": "5d51acd5e31400282cc42221", // ID COURSE REFERENCE
        "removed": "5d50c36e3b28be08f49f6ad9"
    }
}
```

**Delete class**

> url_base/courses/idCourse/class/idClass

Return object class removed

```
{
    "data": {
        "_id": "5d51acd5e31400282cc42221", // ID COURSE REFERENCE
        "removed": "5d510458fa98a32f703622e3"
    }
}
```

## STUDENTS

### Methods GET

**Get students**
> url_base/students

Return Array of students:
```
{
  "data": [{
    "_id":"5d537a62b572f22f804dee51",
    "name":"Alex","surnames":"Garrixen",
    "interest":"Ingenieria,desarrollo y programacion",
    "email":"alex@gmail.com",
    "description":"Frontend Developer",
    "twitter":"freddier"
    },
    ...more
  ]
}
```
**Get student**
> url_base/students/idStudent

Return Object of student : 

```
{
  "data":{
    "_id":"5d537a62b572f22f804dee51",
    "name":"Alex",
    "surnames":"Garrixen",
    "interest":"Ingenieria,desarrollo y programacion",
    "email":"alex@gmail.com",
    "description":"Frontend Developer",
    "twitter":"freddier"
  }
}
```

### Method POST

**Create new student**

> url_base/students

Send in Request Body Object 

```
{
  "name": "jessica",
  "surnames": "martinez",
  "email": "jess@gmail.com",
  "interest": "Backend developer",
  "description": "Never stop learning",
  "twitter": "jess10"
}
```
Example with fetch Api
```
fetch(url,{
    method : 'POST',
    headers : new Headers({
        'Content-Type':'application/json'
    }),
    body : JSON.stringify(DATA)
})
```

Return object studentd created

```
{
    "data": {
        "name": "jessica",
        "surnames": "martinez",
        "email": "jess@gmail.com",
        "interest": "marketing",
        "description": "soy marketing",
        "twitter": "https://twitter.com/",
        "_id": "5d51a4b56cd1cf2870a34137"
    }
}
```

### Method PUT

**Update student**

> url_base/students/idStudent

Send in Request Body Object 

```
{
	"name": "jessica",
    "surnames": "martinez",
}
```
Example with fetch Api
```
fetch(url,{
    method : 'PUT',
    headers : new Headers({
        'Content-Type':'application/json'
    }),
    body : JSON.stringify(DATA)
})
```

Return object student updated

```
{
    "data": {
        "_id": "5d51a4b56cd1cf2870a34137",
        "name": "jessica",
        "surnames": "martinez",
        "email": "jess@gmail.com",
        "interest": "marketing",
        "description": "soy marketing",
        "twitter": "feddier"
    }
}
```

### Method DELETE

**Remove student**

> url_base/students/idStudent

Return object student removed

```
{
    "data": {
        "studentRemoved": "5d51a4b56cd1cf2870a34137"
    }
}
```

## CLASSES

### Method GET

**Get classes**
> url_base/classes

Return Array of classes:

```
{
  "data" : [
    {
    	"_id" : "5d51b0c8b1593815acb27f2a",
    	"name" : "Que es react",
        "label" : "React"
    }
  ],
  ...more
}
```
### Method POST
**create class**
> url_base/classes

Send in Request Body Object

```
{
    "name" : "Que es react",
    "label" : "React"
}
```
Example with fetch Api
```
fetch(url,{
    method : 'POST',
    headers : new Headers({
        'Content-Type':'application/json'
    }),
    body : JSON.stringify(DATA)
})
```
Return object class created

```
{
    "data": {
        "name": "Que es react",
        "label": "React",
        "_id": "5d51b0c8b1593815acb27f2a"
    }
}
```

### Method DELETE

> url_base/classes/idClass

Return object class created

```
{
    "data": {
        "classRemoved": "5d51b0c8b1593815acb27f2a"
    }
}
```


