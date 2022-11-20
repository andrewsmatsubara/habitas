from django_unicorn.components import UnicornView
from ..models import Tree, Post


class PostsView(UnicornView):
    tree: Tree = None
    posts: Post = None
    author: str = ""
    content: str = ""

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
        print(self.content)
        Post.objects.create(
            tree=self.tree,
            author=self.author,
            content=self.content
        )
        print(self.tree)
        print(self.author)
        print(self.content)
        #reset
        self.author = ""
        self.content = ""
        self.posts = Post.objects.filter(tree=self.tree)
