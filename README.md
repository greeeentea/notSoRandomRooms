# randomRooms

`generateSTL.py` creates a stl-file representing a "room" with n objects. these objets are cuboids of random size (maximal room size/2), that are rotated randomly in the xy-plane.

![alt text](https://github.com/greeeentea/randomCubes/blob/main/img/randomroom.png?raw=true)

#### Naming of output stl-file

n{#objects}rs{room-size}d{date as day month year}t{time as hour minutes ..}.stl

### Prerequisites

    pip install numpy-stl
    
### Example

    ./generateStl.py -r 10 -p ./test -o 10 -rs 10


