# import arcade
import Striker
from Striker import *
# import math

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1000
SCREEN_TITLE = "Pla1tformer"
VIEWPORT_MARGIN = 350

SPRITE_SCALING_ATTACK = 0.25
SPRITE_SCALING_PLAYER = 1
SPRITE_SCALING_WALL = 0.6

MOVEMENT_SPEED = 5
JUMP_SPEED = 15
GRAVITY = 0.5

RIGHT_FACING = 0
LEFT_FACING = 1

UPDATES_PER_FRAME = 7

def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, mirrored=True)
    ]



class GameView(arcade.View):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__()

        self.timer = 0
        self.platform_list = None
        self.player_sprite = None
        self.player_list = None
        self.player = None
        self.view_left = 0
        self.view_bottom = 0
        self.background_list = None
        self.attack_texture = None
        self.player_bullet_list = None
        self.bullet_count = 1


        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.jump_needs_reset = False
        self.attack_key_pressed = False




        self.cur_texture = 0
        self.character_face_direction = RIGHT_FACING


    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player = Striker.PlayerCharacter
        self.player_bullet_list = arcade.SpriteList()


        self.attack_texture = []
        for i in range(3):
            texture = load_texture_pair("Sprites/Characters/punch"+ str(i) + ".png")
            self.attack_texture.append(texture)


        # arcade.Sprite("Sprites/Player_Ball.png", SPRITE_SCALING_PLAYER)
        self.player_sprite = Striker.PlayerCharacter()
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 185
        self.player_list.append(self.player_sprite)




        self.platform_list = arcade.SpriteList()
        self.background = arcade.SpriteList()

        map_name = "Arena.tmx"

        my_map = arcade.tilemap.read_tmx(map_name)

        platform_layer_name = "platform"

        background_layer_name = "background"

        self.platform_list = arcade.tilemap.process_layer(map_object=my_map,
                                                          layer_name=platform_layer_name,
                                                          scaling=SPRITE_SCALING_WALL)



        self.background_list = arcade.tilemap.process_layer(my_map, background_layer_name, SPRITE_SCALING_WALL)

        if my_map.background_color:
            arcade.set_background_color(my_map.background_color)

        self.physics_engine = \
            arcade.PhysicsEnginePlatformer(self.player_sprite,
                                           self.platform_list,
                                           gravity_constant=GRAVITY,)



    def on_show(self):
        self.setup()

    def on_draw(self):
        arcade.start_render()

        self.player_bullet_list.draw()
        # self.background_list.draw()
        self.platform_list.draw()
        self.player_list.draw()

    def process_keychange(self):
        """
        Called when we change a key up/down or we move on/off a ladder.
        """
        # Process up/down
        if self.up_pressed and not self.down_pressed:
            if self.physics_engine.is_on_ladder():
                self.player_sprite.change_y = MOVEMENT_SPEED
            elif self.physics_engine.can_jump(y_distance=10) and not self.jump_needs_reset:
                self.player_sprite.change_y = JUMP_SPEED
                self.jump_needs_reset = True

        elif self.down_pressed and not self.up_pressed:
            if self.physics_engine.is_on_ladder():
                self.player_sprite.change_y = -MOVEMENT_SPEED

        # Process up/down when on a ladder and no movement
        if self.physics_engine.is_on_ladder():
            if not self.up_pressed and not self.down_pressed:
                self.player_sprite.change_y = 0
            elif self.up_pressed and self.down_pressed:
                self.player_sprite.change_y = 0

        # Process left/right
        if self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        else:
            self.player_sprite.change_x = 0

        if self.attack_key_pressed:
            player_bullet = arcade.Sprite("sprites/energy -1.png.png", SPRITE_SCALING_ATTACK)

            # Position the bullet at the player's current location
            p_start_x = self.player_sprite.center_x
            p_start_y = self.player_sprite.center_y
            if self.character_face_direction == 0:

                player_bullet.center_x = p_start_x + 30
                player_bullet.center_y = p_start_y + 15
            elif self.character_face_direction == 1:

                player_bullet.center_x = p_start_x - 30
                player_bullet.center_y = p_start_y + 15

            # Get from the mouse the destination location for the bullet
            # IMPORTANT! If you have a scrolling screen, you will also need
            # to add in self.view_bottom and self.view_left.

            # Add the bullet to the appropriate lists
            self.player_bullet_list.append(player_bullet)






    def on_key_press(self, key, modifiers):

        self.player.on_key_press(self, key)
        

        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = True
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True

        elif key == arcade.key.M or key == arcade.key.KEY_1:
            self.attack_key_pressed = True



        self.process_keychange()

    def on_key_release(self, key, modifiers):

        self.player.on_key_release(self, key)

        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = False
            self.jump_needs_reset = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False
        elif key == arcade.key.M or key == arcade.key.KEY_1:
            self.attack_key_pressed = False

        self.process_keychange()




    def on_update(self, delta_time):

        self.physics_engine.update()
        self.player_list.update_animation()
        self.player_list.update()
        self.player_bullet_list.update()

        changed = False


        if self.physics_engine.can_jump():
            self.player_sprite.can_jump = False
        else:
            self.player_sprite.can_jump = True

        for bullet in self.player_bullet_list:
            if self.timer == 0.5:
                bullet.remove_from_sprite_lists()

        self.timer +=0.1
        if self. timer > 0.5:
            self.timer = 0

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

        if self.player_sprite.center_y < -50:
            arcade.close_window()


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT,SCREEN_TITLE)
    game_view = GameView()
    window.show_view(game_view)
    arcade.run()


main()