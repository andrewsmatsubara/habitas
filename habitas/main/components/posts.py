from django_unicorn.components import UnicornView
from ..models import Tree, Post
SPECIALIZED_PASSWORD = "123456"


class PostsView(UnicornView):
    tree: Tree = None
    posts: Post = None
    author: str = ""
    specialized: bool = False
    password: str = ""
    content: str = ""
    error: str = ""

    def mount(self):
        # self.tree = Tree.objects.get(id=self.request.id)
        self.posts = Post.objects.filter(tree=self.tree)
        # self.posts = Post.objects.none()
        return super().mount()

    def update(self, id):
        self.tree = Tree.objects.get(id=int(id))
        self.posts = Post.objects.filter(tree=self.tree)

    def submit(self):
        print(self.tree)
        print(self.author)
        print(self.specialized)
        print(self.password)
        print(self.content)
        if not self.author or not self.content:
            self.error = "Forneça seu nome e o comentário"
        elif self.specialized and self.password != SPECIALIZED_PASSWORD:
            self.error = "Senha incorreta"
        else:
            Post.objects.create(
                tree=self.tree,
                author=self.author,
                content=self.content,
                specialized=self.specialized
            )
            #reset
            self.author = ""
            self.specialized = False
            self.password = ""
            self.content = ""
            self.error = ""
        self.posts = Post.objects.filter(tree=self.tree)
