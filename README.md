<h1 align="center">Sokoban Games</h1>
It is a project of CITS3403 of The University of Western Australia in 2022 
and is a web version of a simple [Sobokan Games](). 
As shown in the picture below.
<p align="center">
    <img
        src= "./img/game.png"
        width="400"
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
    * [Movements](#movements)
    * [Score Scale](#score-scale)
* [Update and Vet Levels](#update-and-vet-levels)
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
Level 1 of the Sokoban Games will be used as an example.<br/>
**Picture form：**
<p align="center">
    <img
        src= "./img/game.png"
        width="400"
        height="200"
        alt="Sokoban Games"
    />
</p>

**The input form in the python code：**
```
[0,3,3,3,3,0,0,3,3,3,3,3,
3,3,2,2,3,0,0,3,2,2,2,3,
3,2,4,2,3,3,3,3,4,2,2,3,
3,2,2,4,1,1,1,1,2,4,2,3,
3,3,2,2,2,2,3,2,2,2,3,3,
0,3,3,3,3,3,3,3,3,3,3,0]
```
As shown above, the rules of the level maps are `0` is an unreachable area, `1` is a target position(where to be pushed), 
`2` is a normal path (walkable), `3` is a wall, and `4` is a chest.

### Movements
To get through the level, player need to push all the chests into all the light colored places on the level map. As shown below picture.  
At the same time, the number of steps recorded is compared to other players based on the score scale.
<p align="center">
    <img
        src= "./img/win.png"
        width="400"
        height="200"
        alt="Level Maps"
    />
</p>

### Score Scale
1. The number of steps per level will be roughly divided into three scoring levels, with the fewer steps the higher the score. 
2. The more difficult the level is, the higher the score level will be. </br>
* For example, in level 1, the score is 40 for steps less than 60, 30 for steps greater than 60 and less than 80, and 20 for all others. Correspondingly, in level 3, the score is 60 for steps less than 140, 50 for steps greater than 140 and less than 170, and 40 for other times.</br>
* Of course, you can change the detailed rules of scoring by modifying the `win` function in the `index.js`.
However, you have to follow the two above rules.

## Update and Vet Levels
1. Firstly, go to the `src` file in CITS3403 file and open `index.js`.
2. Add the new level map that follows the map rules in `maps` variable, which shown below:
<p align="center">
    <img
        src= "./img/maps.png"
        width="200"
        height="200"
        alt="Level Maps"
    />
</p>

3. Also, add the folloing command to the `index.js` and you only need to change the `x` variable,
which is the number of level you want to add:
```
$("#levelx").click(function(){
    level=x-1;
    target = box_number[level]; // the number of boxes
    position = initial_position[level];// first position of the batman
    steps=[];
    record=[];
    movetimes=0;
    times();
    create(); // render the map 
})
```
4. Then, create a new scoring rule for the new level, as detailed in the [Score Scale](#update-and-vet-levels) section.
5. Finally, save the `index.js` and re-execute all commands, and you can see the changes on the Web page.

## Acceptance testing

