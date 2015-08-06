(
    with undo off (
        local obj = selection[1]
        if obj != undefined then (

            local accel = {stick.z}
            local rot_x = {stick.y}
            local rot_y = {stick.rz} * -1
            local rot_z = {stick.x} * -1

            local tm = obj.transform
            preTranslate tm [0, 0, accel]
            preRotate tm (eulerToQuat (eulerAngles rot_x rot_y rot_z))
            obj.transform = tm

            slidertime += {t}
        )
        else
            print "ERROR: No object selected."
    )
)