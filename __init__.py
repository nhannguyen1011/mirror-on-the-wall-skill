from mycroft import MycroftSkill, intent_file_handler


class MirrorOnTheWall(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('wall.the.on.mirror.intent')
    def handle_wall_the_on_mirror(self, message):
        self.speak_dialog('wall.the.on.mirror')


def create_skill():
    return MirrorOnTheWall()

