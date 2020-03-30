# noinspection PyShadowingBuiltins
class S1Api(object):
    base_url = "https://www.s1s1s1.com"
    maker_id = 3152

    def get_actor_image(self):
        return "{}}/contents/actress/{}/{}.jpg".format(self.base_url, id, id)

    def get_video_image(self, id):
        return "{}/contents/works/{}/{}-ps.jpg".format(self.base_url, id, id)
