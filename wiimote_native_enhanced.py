#Enable wiimote sensor reading
wiimote[0].enable(WiimoteCapabilities.MotionPlus)
wiimote[0].enable(WiimoteCapabilities.Extension)

#Variables
DPadUp = wiimote[0].buttons.button_down(WiimoteButtons.DPadUp)
DPadDown = wiimote[0].buttons.button_down(WiimoteButtons.DPadDown)
DPadLeft = wiimote[0].buttons.button_down(WiimoteButtons.DPadLeft)
DPadRight = wiimote[0].buttons.button_down(WiimoteButtons.DPadRight)
A = wiimote[0].buttons.button_down(WiimoteButtons.A)
B = wiimote[0].buttons.button_down(WiimoteButtons.B)
Plus = wiimote[0].buttons.button_down(WiimoteButtons.Plus)
Minus = wiimote[0].buttons.button_down(WiimoteButtons.Minus)
Home = wiimote[0].buttons.button_down(WiimoteButtons.Home)
One = wiimote[0].buttons.button_down(WiimoteButtons.One)
Two = wiimote[0].buttons.button_down(WiimoteButtons.Two)
Pitch = round(wiimote[0].ahrs.pitch)
Yaw = round(wiimote[0].ahrs.yaw)
Roll = round(wiimote[0].ahrs.roll)
WiiMote_X = round(wiimote[0].acceleration.x)
WiiMote_Y = round(wiimote[0].acceleration.y)
WiiMote_Z = round(wiimote[0].acceleration.z)
Nunchuck_Joy_X = wiimote[0].nunchuck.stick.x
Nunchuck_Joy_Y = wiimote[0].nunchuck.stick.y
Nunchuck_Btn_C = wiimote[0].nunchuck.buttons.button_down(NunchuckButtons.C)
Nunchuck_Btn_Z = wiimote[0].nunchuck.buttons.button_down(NunchuckButtons.Z)
Nunchuck_X = round(wiimote[0].nunchuck.acceleration.x)
Nunchuck_Y = round(wiimote[0].nunchuck.acceleration.y)
Nunchuck_Z = round(wiimote[0].nunchuck.acceleration.z)

#All Diagnostics
diagnostics.watch(DPadUp)
diagnostics.watch(DPadDown)
diagnostics.watch(DPadLeft)
diagnostics.watch(DPadRight)
diagnostics.watch(A)
diagnostics.watch(B)
diagnostics.watch(Plus)
diagnostics.watch(Minus)
diagnostics.watch(Home)
diagnostics.watch(One)
diagnostics.watch(Two)

#Define Call Diagnostics
def log_motionplus():
	diagnostics.watch(Pitch)
	diagnostics.watch(Yaw)
	diagnostics.watch(Roll)
	
def log_acceleration():
	diagnostics.watch(WiiMote_X)
	diagnostics.watch(WiiMote_Y)
	diagnostics.watch(WiiMote_Z)
	
def log_nunchuck():
	diagnostics.watch(Nunchuck_Joy_X)
	diagnostics.watch(Nunchuck_Joy_Y)
	diagnostics.watch(Nunchuck_X)
	diagnostics.watch(Nunchuck_Y)
	diagnostics.watch(Nunchuck_Z)
	diagnostics.watch(Nunchuck_Btn_C)
	diagnostics.watch(Nunchuck_Btn_Z)

#Call Diagnostics when in use
wiimote[0].motionplus.update += log_motionplus
wiimote[0].acceleration.update += log_acceleration
wiimote[0].nunchuck.update += log_nunchuck

#Start hydra driver
hydra[0].start = True
hydra[0].isDocked = False
hydra[0].side = 'R'

#Map wiimote controlls to hydra
hydra[0].pitch = Pitch
hydra[0].yaw = Yaw
hydra[0].roll = Roll
hydra[0].trigger = B
hydra[0].x = WiiMote_X
hydra[0].y = WiiMote_Y
hydra[0].z = WiiMote_Z

Rone = DPadUp or DPadDown or DPadLeft or DPadRight
Rfour = Plus
Rstart = Home
Rbumper = A

hydra[0].one = Rone
hydra[0].four = Rfour
hydra[0].start = Rstart
hydra[0].bumper = Rbumper
hydra[0].joybutton = Rone
if DPadRight:
	hydra[0].joyx = 1
elif DPadLeft:
	hydra[0].joyx = 0
if DPadUp:
	hydra[0].joyy = 1
elif DPadDown:
	hydra[0].joyy = 0