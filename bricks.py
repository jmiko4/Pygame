class Bricks:
    def_init_(self, space):
        for x in range(10):
            for y in range(10):
                body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
                body.position = x * 110 + 90, y * 30 + 500
                shape = pymunk.Segment(body, (0, 0), (100, 0), 8)
                shape.elasticity = 0.98
                shape.collision_type = collision_type = collision_types['brick']
                space.add(body, shape)