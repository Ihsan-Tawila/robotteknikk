from robodk import *      # RoboDK API
from robolink import *    # Robot toolbox
sim = Robolink()

robot = sim.Item("UR10")
base = sim.Item("UR10 Base")
robot.setPoseFrame(base)
robot_tool = sim.Item("Gripper RobotiQ 85 Opened")
home = sim.Item("Home")
take_plan = sim.Item("take_plan")
take = sim.Item("take")

radios = 53
x = -308
y = -698.71
z = -268

ry_robot = 4.33
ry = 180 - ry_robot

take_plan.setPose(transl(x,y,z) * rotx((-90*pi)/180)* roty((ry*pi)/180)*rotz((180*pi)/180))

robot.setPoseFrame(take_plan)
robot.MoveL(home)
robot.Pause(1000)

robot.MoveL(take.Pose() * transl(radios + 24, radios + 102, -100))
robot.RunInstruction("tfg_grip(10, 80, external_grip=True,stop_if_no_force=False,tool_index=0, blocking=True)", INSTRUCTION_INSERT_CODE)

robot.Pause(1000)

robot.MoveL(take.Pose() * transl(radios + 24, radios + 102, 95))
robot.RunInstruction("tfg_grip(105, 100, external_grip=False,stop_if_no_force=True,tool_index=0, blocking=True)", INSTRUCTION_INSERT_CODE)
robot.Pause(1000) 

robot.MoveL(take.Pose() * transl(radios + 24, 250 + radios , 80))
robot.Pause(1000) 

robot.MoveL(take.Pose() * transl(radios + 24, 250 + radios , -100))
robot.Pause(1000) 
