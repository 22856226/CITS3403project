<h1 align="center">Sokoban Games</h1>
It is a project of CITS3403 of The University of Western Australia in 2022 
and is a web version of a simple [Sobokan Games](). 
As shown in the picture below.
<p align="center">
    <img
        src= "./img/game.png"
        width="200"
        height="200"
        alt="Sokoban Games"
    />
</p>

## Directory
* [Requirements](#requirements)
    * [Required Languages](#required-packages)
    * [Required Packages](#required-packages)
* [Launch From Local Host](#getting-started)
    * [Gain Project file](#gain-Project-file)
    * [Steps](#steps)
* [Train of Thought](#train-of-thought)
    * [Level Maps](#level-maps)
* [Acceptance testing](#acceptance-testing)
* * *

## Requirements
### Required Languages
- HTML5, CSS3 and JavaScript
- Python
### Required Packages
- `unittest`
- `flask`, `flask_wtf`, `flask_sqlalchemy`, `flask_login`
- `werkzeug.security`
- `wtforms`, `wtforms.validators`
- `os`
- `sys`

## Launch From Local Host
### Gain Project file
- Download from [GitHub](https://github.com/22856226/CITS3403project.git) and then get a file named CITS3403project.
or
- Obtain the CITS3403project file package by other ways.
### Steps
1. Find the route to the CITS3403 file and enter it on the local host.
2. If the terminal environment is `(base)`, run the following command to go to the virtual environment `(venv)`:
```
$ source venv/bin/activate
```
- Also, you can exit virtual environment using the following command:
```
$ deactivate
```
3. Use the following command to install third-party packages required by the project：
```
$ pip install -Ur requirements.txt
```
4. Use the following command and visit 'http://127.0.0.1:5000':
```
$ export Flask_APP=microblog.py
$ flask fun
```
__Now, you can access the project from the local host.__

## Train of Thought
### Level Maps
Level 1 of the Sokoban Games will be used as an example.
**Picture form：**
<p align="center">
    <img
        src= "./img/game.png"
        width="200"
        height="200"
        alt="Sokoban Games"
    />
</p>
**The input form in the python code：**
```
[0,0,3,3,3,3,3,3,3,3,3,0,
0,0,3,2,2,3,3,2,2,2,3,0,
0,0,3,2,2,2,4,2,2,2,3,0,
0,0,3,4,2,3,3,3,2,4,3,0,
0,0,3,2,3,1,1,1,3,2,3,0,
0,3,3,2,3,1,1,1,3,2,3,3,
0,3,2,4,2,2,4,2,2,4,2,3,
0,3,2,2,2,2,2,3,2,2,2,3,
0,3,3,3,3,3,3,3,3,3,3,3]
```
`0` is an unreachable area, `1` is a target (where to be pushed), `2` is a normal path (walkable), 
`3` is a wall, and `4` is a chest.

## Acceptance testing

