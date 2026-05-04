class Post:
    """
    Represents a post (mail).
    """

    count = 0

    def __init__(self, sender, receiver):
        """
        Constructor.
        """
        self.sender = sender
        self.receiver = receiver
        Post.count += 1

    def send(self):
        """
        Sends post.
        """
        return "Post sent"

    def info(self):
        """
        Post info.
        """
        return f"{self.sender} -> {self.receiver}"


class ExpressPost(Post):
    """
    Inherited Post class.
    """

    def __init__(self, sender="A", receiver="B", speed="fast"):
        """
        Default constructor.
        """
        super().__init__(sender, receiver)
        self.speed = speed

    def delivery(self):
        """
        Delivery speed.
        """
        return f"Delivery speed: {self.speed}"


if __name__ == "__main__":
    p = ExpressPost()
    print(p.send())
    print(p.info())
    print(p.delivery())
    print(Post.count)