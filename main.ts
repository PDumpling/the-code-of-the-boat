controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    sprites.createProjectileFromSprite(img`
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
    `, mySprite, 100, 0)
})


sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function(sprite: Sprite, otherSprite: Sprite) {
    
})

let mySprite2: Sprite = null
scene.setBackgroundColor(3)
let mySprite = sprites.create(img`
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
    `, 0)
controller.moveSprite(mySprite)
tiles.setTilemap(tilemap`level1`)
scene.cameraFollowSprite(mySprite)
game.onUpdateInterval(2000, function () {
    mySprite2 = sprites.create(img`
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
        `, 0)
})
