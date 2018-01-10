# mypkg

Codes for the demo of roslaunch and rosbridge

## Description

This repository contains codes copied from the repository of robosys2017 (https://github.com/ryuichiueda/robosys2017/). They are used for demonstrating roslaunch and rosbridge (functions of ROS).

## Setup

* Prepare Raspberry Pi 3.

* Install the image to a microSD card.
  * http://file.ueda.tech/RPIM_BOOK/ubuntu-16.04-raspimouse-ros-book-part1+catkin_ws.img.xz
  * Initial password, ID = "ubuntu"
  * ROS is already installed in the image.
  * Reference: https://lab.ueda.tech/?presenpress=%E3%83%AD%E3%83%9C%E3%83%83%E3%83%88%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E5%AD%A62016%E7%AC%AC12%E5%9B%9E#/15

* Clone this repository under the '~/catkin_ws/src' directory.
```
$ cd ~/catkin_ws/src
$ git clone https://github.com/masash1/mypkg.git
```

## Usage

* Start ROS.
  * Press Ctrl+c to quit.
```
$ roscore
```

* Launch the demo package.
```
$ roslaunch mypkg mypkg.launch
```
 
* Check the result by using a web browser.
  * Search 'raspberrypi's ip address:8000' in the window.
  
## Demo

* https://www.youtube.com/watch?v=53yxMH1T3Bs

## Reference

* https://github.com/ryuichiueda/robosys2017/blob/master/11.md
* https://github.com/ryuichiueda/robosys2017/blob/master/12.md
* https://github.com/ryuichiueda/robosys2017/blob/master/13.md

## License
This repository is licensed under the GPLv3 license, see [LICENSE](./LICENSE).
