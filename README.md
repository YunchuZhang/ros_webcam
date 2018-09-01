# ros_webcam
# Utilize usb camera ,ros ,cv_bridge and zeromq to transform image information to another machine

The first step is to install usb_drive:   
Install usb_cam ROS node with needed dependencies:
        
    $ sudo apt install ros-kinetic-usb-cam    
And then:   
use this command to launch it 
    
    $roslaunch usb_cam usb_cam-test.launch    
After that use ros to subscribe image/raw topic and use cv_bridge to transform    
for compressed image topic, the code is a little bit different in callback function and subscriber part   



At last, use zeromq to send it
