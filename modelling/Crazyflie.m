clear all;

vrep=remApi('remoteApi'); % using the prototype file (remoteApiProto.m)
vrep.simxFinish(-1);
clientID=vrep.simxStart('127.0.0.1',19999,true,true,5000,5);

 [returnCode,Quadricopter_target]=vrep.simxGetObjectHandle(clientID,'Quadricopter_target',vrep.simx_opmode_oneshot_wait);
 [returnCode,ResizableFloor_5_25]=vrep.simxGetObjectHandle(clientID,'ResizableFloor_5_25',vrep.simx_opmode_oneshot_wait);

if (clientID>-1)
    disp('connected');
    
    switch_move=input('Whether to perform displacement simlation input 1 or 0');
    
     [returnCode,position]=vrep.simxGetObjectPosition(clientID,Quadricopter_target,-1,vrep.simx_opmode_blocking);
     Posx=position(1,1);
     Posy=position(1,2);
     Posz=position(1,3);
    
    if switch_move==1
    
    target_position=input('Enter Quadricopter final coordinates x y z as [x y z]: ');
    x=target_position(1,1);
    y=target_position(1,2);
    z=target_position(1,3);


  
   % [returnCode]=vrep.simxSetObjectPosition(clientID,Quadricopter_target,-1,[1,1,1],vrep.simx_opmode_blocking);
    %[returnCode]=vrep.simxSetObjectOrientation(clientID,Quadricopter_target,Quadricopter,[0,0,0.5],vrep.simx_opmode_blocking)
    %vrep.simxAddDrawingObject_points(number size, array color, array coords, string topic)
    

    pause(2);
    for(i=1:36)

        
       [returnCode]=vrep.simxSetObjectPosition(clientID,Quadricopter_target,ResizableFloor_5_25,[Posx+(x-Posx)/36*i,Posy+(y-Posy)/36*i,Posz+(z-Posz)/36*i],vrep.simx_opmode_blocking);
       

      
        pause(0.4);
    end
    
    elseif switch_move==0
        
         circle_position=input('Enter circle centre coordinates x y z as [x y z]: ');
         Cx=circle_position(1,1);
         Cy=circle_position(1,2);
         Cz=circle_position(1,3);
         
        
         
        pause(2);
        for(i=1:36)

        r=sqrt((Cx-Posx)^2+(Cy-Posy)^2);
        
        [returnCode]=vrep.simxSetObjectPosition(clientID,Quadricopter_target,ResizableFloor_5_25,[Cx-r*cos(i*pi/18),Cy-r*sin(i*pi/18),Posz],vrep.simx_opmode_blocking);
        
         pause(0.4);

        end
        
        elseif switch_move==2
        
         Numcircle=input('Enter the number of circle: ');
         
         for (i=1:36*Numcircle)
        
         [returnCode]=vrep.simxSetObjectOrientation(clientID,Quadricopter_target,-1,[0,0,i*pi/18],vrep.simx_opmode_blocking);
        
          pause(0.4);
          
         end
    end
    
    
    vrep.simxFinish(-1);
     
end