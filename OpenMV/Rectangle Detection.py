# Untitled - By: ronal - Tue Apr 11 2023

import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)

clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot()

    for r in img.find_rects(threshold = 10000):
        img.draw_rectangle(r.rect(), color = 255,0,0))
        for p in r.corners(): img.draw_circle(p[0], p[1],5, color = (0,255,0))
        print(r)

    print(clock.fps())
