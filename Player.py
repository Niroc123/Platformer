import arcade

RIGHT_FACING = 0
LEFT_FACING = 1

UPDATES_PER_FRAME = 7

SPRITE_SCALING_PLAYER = 1


def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, mirrored=True)
    ]





class PlayerCharacter(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.cur_texture = 0
        self.cur_attack_texture = 0
        self.character_face_direction = RIGHT_FACING
        self.scale = SPRITE_SCALING_PLAYER

        self.attack = False
        self.pog = 0
        self.jumping = False

        self.idle_texture_pair = load_texture_pair("Sprites/Characters/Striker_idle.png")
        self.jump_texture_pair = load_texture_pair("Sprites/Characters/Jumping.png")

        # walking left and right
        self.walk_textureslr = []
        for i in range(5):
            texture = load_texture_pair("Sprites/Characters/Running" + str(i) + ".png")
            self.walk_textureslr.append(texture)

        self.attack_texture = []
        for i in range(3):
            textureattack = load_texture_pair("Sprites/Characters/punch" + str(i) + ".png")
            self.attack_texture.append(textureattack)

        self.texture = self.idle_texture_pair[0]


    def on_key_press(self, key):

        if key == arcade.key.N or key == arcade.key.KEY_1:
            self.attack = True



    def on_key_release(self, key):
        if key == arcade.key.N or key == arcade.key.KEY_1:


            print("3")



    def update_animation(self, delta_time: float = 1/60):

        if self.attack:
            self.cur_attack_texture += 1
            if self.cur_attack_texture > 3 * UPDATES_PER_FRAME:
                self.cur_attack_texture = 0
                self.attack = False
            self.texture = self.attack_texture[self.cur_attack_texture // UPDATES_PER_FRAME][
                        self.character_face_direction]


        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return

        if self.change_x < 0 or self.change_x > 0 :
            # Walking animation
            self.cur_texture += 1
            if self.cur_texture > 3 * UPDATES_PER_FRAME:
                self.cur_texture = 0
            self.texture = self.walk_textureslr[self.cur_texture // UPDATES_PER_FRAME][self.character_face_direction]

        if self.change_y > 0 :
            self.texture = self.jump_texture_pair[self.character_face_direction]
            return
        elif self.change_y < 0 :
            self.texture = self.jump_texture_pair[self.character_face_direction]
            return

        if self.attack:
            print("5")




