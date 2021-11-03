import common.validators as validators
import common.models as models

validators.is_json('{anil}')
validators.is_date('2021-11-03')

print('**main.py**')
print('validators.bool_value:', validators.boolean_value)
print('validators.pi:', validators.pi)

for k in list(globals().keys()):
    print(k)

print('validators.pi:', validators.pi)
#print('validators.num_values:', validators.numeric_value)

new_post = models.posts_pkg.Post()
new_user = models.users_pkg.User()
print(new_post)


