/*
 *
 * webserver.py
 *
 * Copyright (C) 2018 masash1 <kmasash1995@gmail.com>
 * 
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 */

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy, os
import SimpleHTTPServer

def kill():
    os.system("kill -KILL " + str(os.getpid())) #強制シャットダウン

os.chdir(os.path.dirname(__file__))  #scriptsディレクトリが見えるように
rospy.init_node("webserver")         #rosのノード登録
rospy.on_shutdown(kill)              #kill関数の登録
SimpleHTTPServer.test()              #サーバ立ち上げ
