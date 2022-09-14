# notSoRandomRooms

`generateSTL.py` creates a stl-file representing of a "room" with n objects. these objects are randomly placed cuboids, that are rotated randomly in the xy-plane. they can overlap! 

the object-size as well as the room-size can be specified. otherwise they are also chosen randomly.

![alt text](https://github.com/greeeentea/randomCubes/blob/main/img/randomroom.png?raw=true)

#### Naming of output stl-file

_{given object-size}_n{#objects}rs{room-size}d{date as day month year}t{time as hour minutes ..}.stl

### Prerequisites

    pip install numpy-stl
    
### Example

    ./generateStl.py -r 10 -p ./test -o 10 -rs 10 -os 1


