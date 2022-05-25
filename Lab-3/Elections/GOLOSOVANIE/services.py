def path_to_directory(instance, filename):
    return 'photos/Elections/{0}/{1}/{2}'.format(instance.last_name, instance.first_name, filename)

def user_path_to_directory(instance, filename):
    return 'photos/users/{0}/{1}'.format(instance.nick_name, filename)
