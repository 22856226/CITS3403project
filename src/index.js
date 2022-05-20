

var level=0;//the first map
var box_number=[6,5,4]; //Number of boxes
var initial_position=[94,39,56];//The initial position of each map
var target=box_number[level]; //success condition
var position=initial_position[level];
var vertical =12; // the position value that needs to be changed when up and down
var movetimes = 0; // the steps moved
var steps=[]; //Record player actions
var record=[]; //Record if the box or batman moved, Need to use for back function
//Create a two-dimensional array, twelve in a row, corresponding to the div created by html
//0 is an unreachable area, 1 is a target (where to be pushed), 2 is a normal path (walkable), 3 is a wall, and 4 is a chest
var maps=[
    [
        0,0,3,3,3,3,3,3,3,3,3,0,
        0,0,3,2,2,3,3,2,2,2,3,0,
        0,0,3,2,2,2,4,2,2,2,3,0,
        0,0,3,4,2,3,3,3,2,4,3,0,
        0,0,3,2,3,1,1,1,3,2,3,0,
        0,3,3,2,3,1,1,1,3,2,3,3,
        0,3,2,4,2,2,4,2,2,4,2,3,
        0,3,2,2,2,2,2,3,2,2,2,3,
        0,3,3,3,3,3,3,3,3,3,3,3
    ],
    [
        0,0,0,0,3,3,3,3,3,3,0,0,
        0,0,0,0,3,2,2,2,2,3,0,0,
        0,0,3,3,3,4,4,4,2,3,0,0,
        0,0,3,2,2,4,1,1,2,3,0,0,
        0,0,3,2,4,1,1,1,3,3,0,0,
        0,0,3,3,3,3,2,2,3,0,0,0,
        0,0,0,0,0,3,3,3,3,0,0,0
    ],
    [
        0,3,3,3,3,0,0,3,3,3,3,3,
        3,3,2,2,3,0,0,3,2,2,2,3,
        3,2,4,2,3,3,3,3,4,2,2,3,
        3,2,2,4,1,1,1,1,2,4,2,3,
        3,3,2,2,2,2,3,2,2,2,3,3,
        0,3,3,3,3,3,3,3,3,3,3,0
    ]
];

$("#easy").click(function(){
    level=0;// easy ,medium or hard
    target = box_number[level]; // the number of boxes
    position = initial_position[level];// first position of the batman
    create(); // render the map 
})
$("#medium").click(function(){
    level=1;// easy ,medium or hard
    target = box_number[level]; // the number of boxes
    position = initial_position[level];// first position of the batman
    create(); // render the map 
})
$("#hard").click(function(){
    level=2;// easy ,medium or hard
    target = box_number[level]; // the number of boxes
    position = initial_position[level];// first position of the batman
    create(); // render the map 
})


var box=$('.box div');
create();
//construct the map
function create(){ //
    box.each(function(index){ //using "each" and "eq" function,iterate over each element in the map and render or initialize it
         // Initialize the map
        box.eq(index).removeClass();
    });
    box.each(function(index,element){ 
        if(maps[level][index]>0){ //Render this by numbers in the maps
            box.eq(index).addClass('type'+maps[level][index]);
        }
    });
    box.eq(initial_position[level]).addClass("pusher"); //the batman's position
}

$(document).keydown(function (e) {
    var key=e.which;
    switch(key){
        //up or w in the keyboard
        case 87:
        case 38:
            steps.push(-vertical ); //Record the player's movement path
            move(-vertical );
        break;
        //down or s in the keyboard
        case 83:
        case 40:
            steps.push(vertical );
            move(vertical );
        break;
        //left or a in the keyboard
        case 65:
        case 37:
            steps.push(-1);
            move(-1);
        break;
        //right or d in the keyboard
        case 68:
        case 39:
            steps.push(1); 
            move(1);
        break;
    }
    setTimeout(win,500); // Determine whether the player passes the game
});



function move(step){ 
    //Judging whether to move, there are three cases, only move the batman, move both the box and the batman , or cannot move anything
    var batman_position=box.eq(position); //present position
    var move_position=box.eq(position+step);// next position of batman
    var box_position=box.eq(position+step*2);// newt position of box
    if(!move_position.hasClass('type4')&&( move_position.hasClass('type1')||move_position.hasClass('type2'))){ 
        //Determine if the box will move by judging the position of the next move
        batman_position.removeClass("pusher");
        move_position.addClass("pusher"); //moving the batman
        position=position+step; //change the posinton 
        record.push(0); //The movement is recorded by three numbers: 0, 1, and 2. 
        movetimes++; //0 means only moving the batman, 1 means moving both, and 2 means moving nothing.
        times();
    }
    else if((move_position.hasClass('type4'))&&(!box_position.hasClass('type4'))&&(box_position.hasClass('type1')|| box_position.hasClass('type2')) ) {
        //Because the position of the next step will go to the position of the box, so changing the batman position will also move the box
       move_position.removeClass('type4');
        batman_position.removeClass("pusher");
        box_position.addClass('type4');
        move_position.addClass("pusher").addClass("type2");
        position=position+step;
        record.push(1);
        movetimes++;
        times();
    }
    else{
        record.push(2);
        movetimes++;
        times();
    }
}

function backup(back){
 //The operation is similar to the move function, and the record and steps arraries are used to withdraw to the previous step.   
    var batman_position = box.eq(position);
    var back_position = box.eq(position-back);
    var box_position = box.eq(position+back);
    var recording = record.pop();
    if(recording==0){
        batman_position.removeClass("pusher"); //batman withdraws to the last position
        back_position.addClass('pusher');
        movetimes++;
        position -= back;
        times();
    }
    else if(recording ==1) {
        batman_position.removeClass("pusher"); // batman and box withdraws to the last position
        back_position.addClass('pusher').addClass("type2");
        batman_position.addClass('type4');
        box_position.removeClass('type4').addClass("type2");
        movetimes++;
        position -= back;
        times();
    }
}
function times(){
    $("#movetimes").html("The number of times you moved was "+movetimes);
}
function win(){
    if($(".type1.type4").length===target){
        alert("Congratulations, the number of steps you move through this pass is"+ movetimes);
    }
}
