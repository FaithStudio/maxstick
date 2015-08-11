(
    with undo off (
        local obj = selection[1]
        if obj != undefined then (

            global maxstick_accel = {stick.z} * -1
            global maxstick_rot_x = {stick.x} * 1.25
            global maxstick_rot_y = {stick.y} * -1
            global maxstick_rot_z = {stick.rz} * -0.5

            local rot = eulerAngles maxstick_rot_x maxstick_rot_y maxstick_rot_z
            local tm = obj.transform
            preTranslate tm [maxstick_accel, 0, 0]
            preRotate tm (eulerToQuat rot)
            obj.transform = tm

            slidertime += {t}
        )
        else
            print "ERROR: No object selected."
    )
)