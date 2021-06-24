import user
from post import Post

app_user_one = user.User("nn@nn.com", "Nana Jas", "pwd1", "DevOps enginer")

app_user_one.get_user_info()
app_user_one.change_job_title("Robot Engineer")
app_user_one.get_user_info()

app_user_two = user.User("jj@jj.com", "Jaja Noka", "pwd2", "DevOps trainer")
app_user_two.get_user_info()

new_post = Post("on a secret mission today", app_user_two.name)
new_post.get_post_info()