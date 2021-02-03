def on_a_pressed():
    sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . f . . . . . . . .
                    . . . . . . f . . . . . . . . .
                    . . . . . f . . . . . . . . . .
                    . . . . . f . . . . . . . . . .
                    . . . . . f . . . . . . . . . .
                    . . . . . f . . . . . . . . . .
                    . . . . . . f . . . . . . . . .
                    . . . . . . . f . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
        """),
        mySprite,
        100,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

mySprite2: Sprite = None
scene.set_background_color(3)
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . f f f f f f f . . . . . . 
            . . f 3 3 3 3 3 3 3 f . . . . . 
            . f 3 3 3 3 3 3 3 3 3 f . . . . 
            f 3 3 3 3 3 3 3 3 1 3 3 f . . . 
            f 3 3 1 f 3 3 1 f 3 1 3 f . . . 
            f 3 3 3 3 3 3 3 3 3 1 3 f . . . 
            f 3 3 3 3 3 3 3 3 3 1 3 f . . . 
            f 3 3 3 3 3 3 3 3 3 1 3 f . . . 
            f 3 3 3 f f f f f 3 1 3 f . . . 
            f 3 3 3 3 3 3 3 3 1 3 3 f . . . 
            . f 3 3 3 3 3 3 3 3 3 f . . . . 
            . . f 3 3 3 3 3 3 3 f . . . . . 
            . . . f f f f f f f . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    0)
controller.move_sprite(mySprite)
tiles.set_tilemap(tilemap("""
    level1
"""))
scene.camera_follow_sprite(mySprite)

def on_update_interval():
    global mySprite2
    mySprite2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . f f f f f f f . . . . . 
                    . . . f 2 2 2 2 2 2 2 f . . . . 
                    . . f 2 2 2 2 2 2 2 1 2 f . . . 
                    . f 2 2 2 2 2 2 2 2 2 1 2 f . . 
                    . f 2 2 2 f 2 2 2 f 2 1 2 f . . 
                    . f 2 2 2 2 2 2 2 2 2 1 2 f . . 
                    . f 2 2 2 2 2 2 2 2 2 1 2 f . . 
                    . f 2 2 f 2 2 2 2 2 f 1 2 f . . 
                    . f 2 2 2 f f f f f 2 1 2 f . . 
                    . f 2 2 2 2 2 2 2 2 2 1 2 f . . 
                    . . f 2 2 2 2 2 2 2 1 2 f . . . 
                    . . . f 2 2 2 2 2 2 2 f . . . . 
                    . . . . f f f f f f f . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        0)
game.on_update_interval(2000, on_update_interval)
